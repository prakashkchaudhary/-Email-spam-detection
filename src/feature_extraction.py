"""
Feature Extraction Module
Handles text vectorization using TF-IDF
"""

from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
import joblib
import os


class FeatureExtractor:
    """
    Feature extraction class for converting text to numerical vectors
    """
    
    def __init__(self, method='tfidf', max_features=3000, ngram_range=(1, 2)):
        """
        Initialize feature extractor
        
        Args:
            method (str): 'tfidf' or 'count'
            max_features (int): Maximum number of features
            ngram_range (tuple): N-gram range for feature extraction
        """
        self.method = method
        self.max_features = max_features
        self.ngram_range = ngram_range
        
        if method == 'tfidf':
            self.vectorizer = TfidfVectorizer(
                max_features=max_features,
                ngram_range=ngram_range,
                lowercase=True,
                stop_words='english'
            )
        elif method == 'count':
            self.vectorizer = CountVectorizer(
                max_features=max_features,
                ngram_range=ngram_range,
                lowercase=True,
                stop_words='english'
            )
        else:
            raise ValueError("Method must be 'tfidf' or 'count'")
    
    def fit_transform(self, texts):
        """
        Fit vectorizer and transform texts
        
        Args:
            texts (list): List of text documents
            
        Returns:
            array: Transformed feature matrix
        """
        return self.vectorizer.fit_transform(texts)
    
    def transform(self, texts):
        """
        Transform texts using fitted vectorizer
        
        Args:
            texts (list): List of text documents
            
        Returns:
            array: Transformed feature matrix
        """
        return self.vectorizer.transform(texts)
    
    def get_feature_names(self):
        """Get feature names from vectorizer"""
        return self.vectorizer.get_feature_names_out()
    
    def save_vectorizer(self, filepath='models/vectorizer.pkl'):
        """
        Save vectorizer to file
        
        Args:
            filepath (str): Path to save vectorizer
        """
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        joblib.dump(self.vectorizer, filepath)
        print(f"Vectorizer saved to {filepath}")
    
    def load_vectorizer(self, filepath='models/vectorizer.pkl'):
        """
        Load vectorizer from file
        
        Args:
            filepath (str): Path to load vectorizer from
        """
        self.vectorizer = joblib.load(filepath)
        print(f"Vectorizer loaded from {filepath}")
        return self.vectorizer


def create_and_save_vectorizer(texts, labels, filepath='models/vectorizer.pkl'):
    """
    Create, fit, and save vectorizer
    
    Args:
        texts (list): List of text documents
        labels (list): List of labels
        filepath (str): Path to save vectorizer
        
    Returns:
        tuple: (feature_matrix, vectorizer)
    """
    extractor = FeatureExtractor(method='tfidf', max_features=3000, ngram_range=(1, 2))
    features = extractor.fit_transform(texts)
    extractor.save_vectorizer(filepath)
    
    return features, extractor


def load_and_transform(texts, filepath='models/vectorizer.pkl'):
    """
    Load vectorizer and transform texts
    
    Args:
        texts (list): List of text documents
        filepath (str): Path to vectorizer file
        
    Returns:
        array: Transformed feature matrix
    """
    extractor = FeatureExtractor()
    extractor.load_vectorizer(filepath)
    return extractor.transform(texts)


if __name__ == "__main__":
    # Test feature extraction
    sample_texts = [
        "win free money now",
        "meeting scheduled for tomorrow",
        "claim your prize today"
    ]
    
    extractor = FeatureExtractor(method='tfidf', max_features=100)
    features = extractor.fit_transform(sample_texts)
    
    print(f"Feature matrix shape: {features.shape}")
    print(f"Number of features: {len(extractor.get_feature_names())}")
