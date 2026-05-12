"""
Flask Web Application for Email Spam Detection
"""

from flask import Flask, render_template, request, jsonify, session
import os
import sys
from datetime import datetime

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from prediction import SpamPredictor

# Initialize Flask app
app = Flask(__name__)
app.secret_key = 'your-secret-key-change-in-production'

# Initialize predictor
try:
    predictor = SpamPredictor()
    MODEL_LOADED = True
except FileNotFoundError as e:
    print(f"Warning: {e}")
    print("Please run 'python src/model_training.py' to train the model first.")
    MODEL_LOADED = False


@app.route('/')
def index():
    """Home page"""
    return render_template('index.html')


@app.route('/detect')
def detect():
    """Spam detection page"""
    if not MODEL_LOADED:
        return render_template('detect.html', error="Model not loaded. Please train the model first.")
    return render_template('detect.html')


@app.route('/about')
def about():
    """About page"""
    return render_template('about.html')


@app.route('/predict', methods=['POST'])
def predict():
    """
    API endpoint for spam prediction
    
    Expected JSON:
    {
        "message": "text to classify"
    }
    
    Returns JSON:
    {
        "prediction": "Spam" or "Ham",
        "confidence": 95.5,
        "message": "result message",
        "timestamp": "2024-01-01 12:00:00"
    }
    """
    if not MODEL_LOADED:
        return jsonify({
            'error': 'Model not loaded',
            'message': 'Please train the model first by running: python src/model_training.py'
        }), 500
    
    try:
        # Get message from request
        data = request.get_json()
        
        if not data or 'message' not in data:
            return jsonify({
                'error': 'Invalid request',
                'message': 'Please provide a message to classify'
            }), 400
        
        message = data['message'].strip()
        
        if not message:
            return jsonify({
                'error': 'Empty message',
                'message': 'Please provide a non-empty message'
            }), 400
        
        # Make prediction
        result = predictor.predict(message)
        
        # Add timestamp
        result['timestamp'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        # Store in session history
        if 'history' not in session:
            session['history'] = []
        
        history_entry = {
            'message': message[:100] + '...' if len(message) > 100 else message,
            'prediction': result['prediction'],
            'confidence': result['confidence'],
            'timestamp': result['timestamp']
        }
        
        session['history'].insert(0, history_entry)
        session['history'] = session['history'][:10]  # Keep last 10 predictions
        session.modified = True
        
        return jsonify(result)
    
    except Exception as e:
        return jsonify({
            'error': 'Prediction failed',
            'message': str(e)
        }), 500


@app.route('/history')
def history():
    """Get prediction history"""
    if 'history' not in session:
        return jsonify([])
    return jsonify(session['history'])


@app.route('/clear-history', methods=['POST'])
def clear_history():
    """Clear prediction history"""
    session['history'] = []
    session.modified = True
    return jsonify({'message': 'History cleared'})


@app.route('/model-info')
def model_info():
    """Get model information"""
    if not MODEL_LOADED:
        return jsonify({
            'error': 'Model not loaded',
            'message': 'Please train the model first'
        }), 500
    
    info = predictor.get_model_info()
    return jsonify(info)


@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'model_loaded': MODEL_LOADED,
        'timestamp': datetime.now().isoformat()
    })


@app.errorhandler(404)
def not_found(e):
    """Handle 404 errors"""
    return render_template('index.html'), 404


@app.errorhandler(500)
def server_error(e):
    """Handle 500 errors"""
    return jsonify({
        'error': 'Internal server error',
        'message': str(e)
    }), 500


if __name__ == '__main__':
    # Create necessary directories
    os.makedirs('models', exist_ok=True)
    os.makedirs('data/raw', exist_ok=True)
    os.makedirs('reports', exist_ok=True)
    
    # Run app
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_ENV', 'development') != 'production'
    app.run(host='0.0.0.0', port=port, debug=debug)
