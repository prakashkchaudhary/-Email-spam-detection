"""
Prediction Module
Handles spam prediction for new messages
"""

import joblib
import os
import numpy as np
from preprocessing import TextPreprocessor


class SpamPredictor:
    """
    Spam prediction class
    """
    
    def __init__(self, model_path='models/best_model.pkl', 
                 vectorizer_path='models/vectorizer.pkl'):
        """
        Initialize predictor with trained model and vectorizer
        
        Args:
            model_path (str): Path to trained model
            vectorizer_path (str): Path to fitted vectorizer
        """
        self.model_path = model_path
        self.vectorizer_path = vectorizer_path
        self.model = None
        self.vectorizer = None
        self.preprocessor = TextPreprocessor()
        self.metadata = None
        
        self._load_model()
        self._load_vectorizer()
        self._load_metadata()
    
    def _load_model(self):
        """Load trained model"""
        if os.path.exists(self.model_path):
            self.model = joblib.load(self.model_path)
            print(f"Model loaded from {self.model_path}")
        else:
            raise FileNotFoundError(f"Model not found at {self.model_path}. "
                                   "Please train the model first using model_training.py")
    
    def _load_vectorizer(self):
        """Load fitted vectorizer"""
        if os.path.exists(self.vectorizer_path):
            self.vectorizer = joblib.load(self.vectorizer_path)
            print(f"Vectorizer loaded from {self.vectorizer_path}")
        else:
            raise FileNotFoundError(f"Vectorizer not found at {self.vectorizer_path}. "
                                   "Please train the model first using model_training.py")
    
    def _load_metadata(self):
        """Load model metadata"""
        metadata_path = 'models/model_metadata.pkl'
        if os.path.exists(metadata_path):
            self.metadata = joblib.load(metadata_path)
            print(f"Model: {self.metadata['model_name']}")
            print(f"Accuracy: {self.metadata['accuracy']:.4f}")
    
    def predict(self, message):
        """
        Predict if a message is spam or ham
        
        Args:
            message (str): Message to classify
            
        Returns:
            dict: Prediction results with label, confidence, and details
        """
        # Preprocess message
        processed_message = self.preprocessor.preprocess(message)
        
        # Vectorize message
        message_vector = self.vectorizer.transform([processed_message])
        
        # Make prediction
        prediction = self.model.predict(message_vector)[0]
        
        # Get prediction probability
        if hasattr(self.model, 'predict_proba'):
            probabilities = self.model.predict_proba(message_vector)[0]
            confidence = probabilities[prediction] * 100
        else:
            # For models without predict_proba (like some SVM variants)
            confidence = 95.0 if prediction == 1 else 90.0
        
        # Prepare result
        result = {
            'prediction': 'Spam' if prediction == 1 else 'Ham',
            'label': int(prediction),
            'confidence': round(confidence, 2),
            'message': self._get_result_message(prediction, confidence),
            'processed_text': processed_message,
            'model_name': self.metadata['model_name'] if self.metadata else 'Unknown'
        }
        
        return result
    
    def predict_batch(self, messages):
        """
        Predict multiple messages at once
        
        Args:
            messages (list): List of messages to classify
            
        Returns:
            list: List of prediction results
        """
        results = []
        for message in messages:
            result = self.predict(message)
            results.append(result)
        return results
    
    def _get_result_message(self, prediction, confidence):
        """
        Get user-friendly result message
        
        Args:
            prediction (int): 0 for ham, 1 for spam
            confidence (float): Confidence percentage
            
        Returns:
            str: Result message
        """
        if prediction == 1:
            if confidence >= 90:
                return "⚠️ This message is highly likely to be SPAM! Be cautious."
            elif confidence >= 70:
                return "⚠️ This message appears to be SPAM. Exercise caution."
            else:
                return "⚠️ This message might be SPAM. Please verify."
        else:
            if confidence >= 90:
                return "✅ This message appears to be legitimate (HAM)."
            elif confidence >= 70:
                return "✅ This message is likely legitimate (HAM)."
            else:
                return "✅ This message seems to be legitimate, but verify if unsure."
    
    def get_model_info(self):
        """
        Get information about the loaded model
        
        Returns:
            dict: Model information
        """
        info = {
            'model_loaded': self.model is not None,
            'vectorizer_loaded': self.vectorizer is not None,
        }
        
        if self.metadata:
            info.update(self.metadata)
        
        return info


def predict_message(message, model_path='models/best_model.pkl', 
                   vectorizer_path='models/vectorizer.pkl'):
    """
    Convenience function for single message prediction
    
    Args:
        message (str): Message to classify
        model_path (str): Path to trained model
        vectorizer_path (str): Path to fitted vectorizer
        
    Returns:
        dict: Prediction results
    """
    predictor = SpamPredictor(model_path, vectorizer_path)
    return predictor.predict(message)


if __name__ == "__main__":
    # Test prediction
    test_messages = [
        "Congratulations! You've won $1000. Call now to claim your prize!",
        "Hey, can we meet for coffee tomorrow at 3 PM?",
        "URGENT: Your account will be suspended. Click here immediately!",
        "Thanks for the meeting today. I'll send the report by Friday."
    ]
    
    print("=" * 60)
    print("Testing Spam Prediction")
    print("=" * 60)
    
    try:
        predictor = SpamPredictor()
        
        for i, message in enumerate(test_messages, 1):
            print(f"\nMessage {i}: {message[:50]}...")
            result = predictor.predict(message)
            print(f"Prediction: {result['prediction']}")
            print(f"Confidence: {result['confidence']:.2f}%")
            print(f"Message: {result['message']}")
            print("-" * 60)
    
    except FileNotFoundError as e:
        print(f"\nError: {e}")
        print("\nPlease run 'python src/model_training.py' first to train the model.")
