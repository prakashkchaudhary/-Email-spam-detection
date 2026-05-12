"""
Unit Tests for Spam Detection System
"""

import unittest
import sys
import os

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from preprocessing import TextPreprocessor, preprocess_text
from feature_extraction import FeatureExtractor


class TestTextPreprocessing(unittest.TestCase):
    """Test text preprocessing functions"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.preprocessor = TextPreprocessor()
    
    def test_lowercase(self):
        """Test lowercase conversion"""
        text = "HELLO WORLD"
        result = self.preprocessor.lowercase_text(text)
        self.assertEqual(result, "hello world")
    
    def test_remove_urls(self):
        """Test URL removal"""
        text = "Check this http://example.com website"
        result = self.preprocessor.remove_urls(text)
        self.assertNotIn("http://example.com", result)
    
    def test_remove_emails(self):
        """Test email removal"""
        text = "Contact me at test@example.com"
        result = self.preprocessor.remove_emails(text)
        self.assertNotIn("test@example.com", result)
    
    def test_remove_phone_numbers(self):
        """Test phone number removal"""
        text = "Call me at 123-456-7890"
        result = self.preprocessor.remove_phone_numbers(text)
        self.assertNotIn("123-456-7890", result)
    
    def test_remove_punctuation(self):
        """Test punctuation removal"""
        text = "Hello, World!"
        result = self.preprocessor.remove_punctuation(text)
        self.assertNotIn(",", result)
        self.assertNotIn("!", result)
    
    def test_tokenize(self):
        """Test tokenization"""
        text = "hello world"
        result = self.preprocessor.tokenize(text)
        self.assertEqual(result, ["hello", "world"])
    
    def test_remove_stopwords(self):
        """Test stopword removal"""
        tokens = ["this", "is", "a", "test"]
        result = self.preprocessor.remove_stopwords(tokens)
        self.assertNotIn("is", result)
        self.assertNotIn("a", result)
        self.assertIn("test", result)
    
    def test_stem_words(self):
        """Test stemming"""
        tokens = ["running", "runs", "runner"]
        result = self.preprocessor.stem_words(tokens)
        # All should stem to similar root
        self.assertTrue(all(len(word) < 6 for word in result))
    
    def test_full_preprocessing(self):
        """Test complete preprocessing pipeline"""
        text = "URGENT! Call 123-456-7890 or visit http://example.com NOW!!!"
        result = self.preprocessor.preprocess(text)
        
        # Should be lowercase
        self.assertEqual(result, result.lower())
        
        # Should not contain URLs or phone numbers
        self.assertNotIn("http", result)
        self.assertNotIn("123", result)
        
        # Should not be empty
        self.assertTrue(len(result) > 0)


class TestFeatureExtraction(unittest.TestCase):
    """Test feature extraction functions"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.extractor = FeatureExtractor(method='tfidf', max_features=100)
        self.sample_texts = [
            "win free money now",
            "meeting scheduled for tomorrow",
            "claim your prize today"
        ]
    
    def test_tfidf_initialization(self):
        """Test TF-IDF vectorizer initialization"""
        self.assertEqual(self.extractor.method, 'tfidf')
        self.assertEqual(self.extractor.max_features, 100)
    
    def test_count_initialization(self):
        """Test Count vectorizer initialization"""
        extractor = FeatureExtractor(method='count', max_features=50)
        self.assertEqual(extractor.method, 'count')
        self.assertEqual(extractor.max_features, 50)
    
    def test_invalid_method(self):
        """Test invalid method raises error"""
        with self.assertRaises(ValueError):
            FeatureExtractor(method='invalid')
    
    def test_fit_transform(self):
        """Test fit_transform method"""
        features = self.extractor.fit_transform(self.sample_texts)
        
        # Check shape
        self.assertEqual(features.shape[0], len(self.sample_texts))
        self.assertLessEqual(features.shape[1], 100)
    
    def test_transform(self):
        """Test transform method"""
        # First fit
        self.extractor.fit_transform(self.sample_texts)
        
        # Then transform new data
        new_texts = ["win money"]
        features = self.extractor.transform(new_texts)
        
        self.assertEqual(features.shape[0], 1)
    
    def test_get_feature_names(self):
        """Test getting feature names"""
        self.extractor.fit_transform(self.sample_texts)
        feature_names = self.extractor.get_feature_names()
        
        self.assertTrue(len(feature_names) > 0)
        self.assertIsInstance(feature_names[0], str)


class TestSpamDetectionIntegration(unittest.TestCase):
    """Integration tests for spam detection"""
    
    def test_spam_message_preprocessing(self):
        """Test preprocessing of typical spam message"""
        spam_message = "CONGRATULATIONS!!! You've WON $1000! Call 123-456-7890 NOW!!!"
        processed = preprocess_text(spam_message)
        
        # Should be processed
        self.assertNotEqual(spam_message, processed)
        self.assertEqual(processed, processed.lower())
        self.assertTrue(len(processed) > 0)
    
    def test_ham_message_preprocessing(self):
        """Test preprocessing of typical ham message"""
        ham_message = "Hey, can we meet for coffee tomorrow at 3 PM?"
        processed = preprocess_text(ham_message)
        
        # Should be processed
        self.assertNotEqual(ham_message, processed)
        self.assertEqual(processed, processed.lower())
        self.assertTrue(len(processed) > 0)
    
    def test_empty_message(self):
        """Test handling of empty message"""
        empty_message = ""
        processed = preprocess_text(empty_message)
        
        # Should return empty or minimal string
        self.assertEqual(len(processed), 0)
    
    def test_special_characters_only(self):
        """Test message with only special characters"""
        special_message = "!@#$%^&*()"
        processed = preprocess_text(special_message)
        
        # Should be empty or very short after processing
        self.assertTrue(len(processed) < 5)


class TestEdgeCases(unittest.TestCase):
    """Test edge cases and error handling"""
    
    def setUp(self):
        self.preprocessor = TextPreprocessor()
    
    def test_none_input(self):
        """Test None input handling"""
        result = self.preprocessor.preprocess(None)
        self.assertIsInstance(result, str)
    
    def test_numeric_input(self):
        """Test numeric input handling"""
        result = self.preprocessor.preprocess(12345)
        self.assertIsInstance(result, str)
    
    def test_very_long_text(self):
        """Test very long text processing"""
        long_text = "word " * 10000
        result = self.preprocessor.preprocess(long_text)
        self.assertIsInstance(result, str)
    
    def test_unicode_characters(self):
        """Test unicode character handling"""
        unicode_text = "Hello 你好 مرحبا"
        result = self.preprocessor.preprocess(unicode_text)
        self.assertIsInstance(result, str)
    
    def test_mixed_case_with_numbers(self):
        """Test mixed case with numbers"""
        mixed_text = "Test123Message456"
        result = self.preprocessor.preprocess(mixed_text)
        # Numbers should be removed
        self.assertNotIn("123", result)
        self.assertNotIn("456", result)


def run_tests():
    """Run all tests"""
    # Create test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add test classes
    suite.addTests(loader.loadTestsFromTestCase(TestTextPreprocessing))
    suite.addTests(loader.loadTestsFromTestCase(TestFeatureExtraction))
    suite.addTests(loader.loadTestsFromTestCase(TestSpamDetectionIntegration))
    suite.addTests(loader.loadTestsFromTestCase(TestEdgeCases))
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Return exit code
    return 0 if result.wasSuccessful() else 1


if __name__ == '__main__':
    exit_code = run_tests()
    sys.exit(exit_code)
