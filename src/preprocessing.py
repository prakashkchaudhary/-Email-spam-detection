"""
Text Preprocessing Module
Handles all text cleaning and preprocessing operations
"""

import re
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# Download required NLTK data
try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords', quiet=True)

try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt', quiet=True)


class TextPreprocessor:
    """
    Text preprocessing class for email spam detection
    """
    
    def __init__(self):
        """Initialize preprocessor with stemmer and stopwords"""
        self.stemmer = PorterStemmer()
        self.stop_words = set(stopwords.words('english'))
    
    def lowercase_text(self, text):
        """Convert text to lowercase"""
        return text.lower()
    
    def remove_urls(self, text):
        """Remove URLs from text"""
        url_pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
        return re.sub(url_pattern, '', text)
    
    def remove_emails(self, text):
        """Remove email addresses from text"""
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        return re.sub(email_pattern, '', text)
    
    def remove_phone_numbers(self, text):
        """Remove phone numbers from text"""
        phone_pattern = r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b'
        return re.sub(phone_pattern, '', text)
    
    def remove_punctuation(self, text):
        """Remove punctuation from text"""
        return text.translate(str.maketrans('', '', string.punctuation))
    
    def remove_special_characters(self, text):
        """Remove special characters and digits"""
        return re.sub(r'[^a-zA-Z\s]', '', text)
    
    def tokenize(self, text):
        """Tokenize text into words"""
        return text.split()
    
    def remove_stopwords(self, tokens):
        """Remove stopwords from token list"""
        return [word for word in tokens if word not in self.stop_words]
    
    def stem_words(self, tokens):
        """Apply stemming to tokens"""
        return [self.stemmer.stem(word) for word in tokens]
    
    def preprocess(self, text):
        """
        Complete preprocessing pipeline
        
        Args:
            text (str): Raw text to preprocess
            
        Returns:
            str: Preprocessed text
        """
        # Convert to string if not already
        text = str(text)
        
        # Step 1: Lowercase
        text = self.lowercase_text(text)
        
        # Step 2: Remove URLs
        text = self.remove_urls(text)
        
        # Step 3: Remove emails
        text = self.remove_emails(text)
        
        # Step 4: Remove phone numbers
        text = self.remove_phone_numbers(text)
        
        # Step 5: Remove punctuation
        text = self.remove_punctuation(text)
        
        # Step 6: Remove special characters
        text = self.remove_special_characters(text)
        
        # Step 7: Tokenize
        tokens = self.tokenize(text)
        
        # Step 8: Remove stopwords
        tokens = self.remove_stopwords(tokens)
        
        # Step 9: Stemming
        tokens = self.stem_words(tokens)
        
        # Step 10: Join tokens back to string
        processed_text = ' '.join(tokens)
        
        return processed_text


def preprocess_text(text):
    """
    Convenience function for preprocessing single text
    
    Args:
        text (str): Text to preprocess
        
    Returns:
        str: Preprocessed text
    """
    preprocessor = TextPreprocessor()
    return preprocessor.preprocess(text)


if __name__ == "__main__":
    # Test preprocessing
    sample_text = "URGENT! You've WON $1000!!! Call 123-456-7890 or visit http://example.com NOW!!!"
    preprocessor = TextPreprocessor()
    processed = preprocessor.preprocess(sample_text)
    print(f"Original: {sample_text}")
    print(f"Processed: {processed}")
