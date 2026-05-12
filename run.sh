#!/bin/bash
# Unix/Linux/macOS script to run the Email Spam Detection application

echo "========================================"
echo "Email Spam Detection System"
echo "========================================"
echo ""

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
    echo ""
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate
echo ""

# Install dependencies if needed
if [ ! -d "venv/lib/python*/site-packages/flask" ]; then
    echo "Installing dependencies..."
    pip install -r requirements.txt
    echo ""
fi

# Check if model exists
if [ ! -f "models/best_model.pkl" ]; then
    echo "Model not found. Training model..."
    python src/model_training.py
    echo ""
fi

# Run the application
echo "Starting application..."
echo ""
echo "Application will be available at: http://localhost:5000"
echo "Press Ctrl+C to stop the server"
echo ""
python app.py
