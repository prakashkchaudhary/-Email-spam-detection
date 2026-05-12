"""
Model Training Module
Trains multiple ML models and selects the best one
"""

import pandas as pd
import numpy as np
import joblib
import os
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    confusion_matrix, classification_report
)
import warnings
warnings.filterwarnings('ignore')

from preprocessing import TextPreprocessor
from feature_extraction import FeatureExtractor


class SpamDetectionTrainer:
    """
    Spam detection model trainer
    """
    
    def __init__(self):
        """Initialize trainer with models"""
        self.models = {
            'Naive Bayes': MultinomialNB(),
            'Logistic Regression': LogisticRegression(max_iter=1000, random_state=42),
            'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42),
            'SVM': SVC(kernel='linear', probability=True, random_state=42)
        }
        self.results = {}
        self.best_model = None
        self.best_model_name = None
        self.preprocessor = TextPreprocessor()
        self.feature_extractor = FeatureExtractor(method='tfidf', max_features=3000)
    
    def load_data(self, filepath='data/raw/spam.csv'):
        """
        Load and prepare dataset
        
        Args:
            filepath (str): Path to dataset file
            
        Returns:
            tuple: (X_train, X_test, y_train, y_test)
        """
        print("Loading dataset...")
        
        # Try to load the dataset
        try:
            df = pd.read_csv(filepath, encoding='latin-1')
        except FileNotFoundError:
            print(f"Dataset not found at {filepath}")
            print("Creating sample dataset for demonstration...")
            df = self._create_sample_dataset()
        
        # Clean dataset
        df = self._clean_dataset(df)
        
        # Preprocess text
        print("Preprocessing text...")
        df['processed_text'] = df['text'].apply(self.preprocessor.preprocess)
        
        # Split data
        X_train, X_test, y_train, y_test = train_test_split(
            df['processed_text'], df['label'],
            test_size=0.2, random_state=42, stratify=df['label']
        )
        
        print(f"Training samples: {len(X_train)}")
        print(f"Testing samples: {len(X_test)}")
        print(f"Spam ratio: {(df['label'] == 1).sum() / len(df) * 100:.2f}%")
        
        return X_train, X_test, y_train, y_test
    
    def _clean_dataset(self, df):
        """Clean and prepare dataset"""
        # Handle different dataset formats
        if 'v1' in df.columns and 'v2' in df.columns:
            df = df[['v1', 'v2']]
            df.columns = ['label', 'text']
        elif 'label' not in df.columns or 'text' not in df.columns:
            # Assume first two columns are label and text
            df = df.iloc[:, :2]
            df.columns = ['label', 'text']
        
        # Remove null values
        df = df.dropna()
        
        # Remove duplicates
        df = df.drop_duplicates()
        
        # Convert labels to numerical
        df['label'] = df['label'].map({'ham': 0, 'spam': 1})
        
        # If labels are already numeric, ensure they're 0 and 1
        if df['label'].dtype != 'int64':
            df['label'] = df['label'].astype(int)
        
        return df
    
    def _create_sample_dataset(self):
        """Create sample dataset for demonstration"""
        spam_messages = [
            "Congratulations! You've won $1000. Call now!",
            "URGENT! Your account will be closed. Click here immediately.",
            "Free entry to win iPhone. Text WIN to 12345",
            "You have been selected for a cash prize. Claim now!",
            "Hot singles in your area. Click to meet them!",
            "Get rich quick! Make $5000 per week from home.",
            "Your loan has been approved. Call us now!",
            "Congratulations! You've won a free vacation to Hawaii!",
            "WINNER! You've been chosen for a $500 gift card.",
            "Act now! Limited time offer. Buy now and save 90%!",
        ] * 10
        
        ham_messages = [
            "Hey, are we still meeting for lunch tomorrow?",
            "Can you send me the report by end of day?",
            "Thanks for your help with the project.",
            "Meeting rescheduled to 3 PM. See you then.",
            "Happy birthday! Hope you have a great day!",
            "Don't forget to pick up milk on your way home.",
            "The presentation went well. Thanks for your support.",
            "Can you review this document when you get a chance?",
            "Looking forward to seeing you at the conference.",
            "Please confirm your attendance for tomorrow's meeting.",
        ] * 10
        
        df = pd.DataFrame({
            'label': ['spam'] * len(spam_messages) + ['ham'] * len(ham_messages),
            'text': spam_messages + ham_messages
        })
        
        # Save sample dataset
        os.makedirs('data/raw', exist_ok=True)
        df.to_csv('data/raw/spam.csv', index=False)
        print("Sample dataset created and saved to data/raw/spam.csv")
        
        return df
    
    def train_models(self, X_train, X_test, y_train, y_test):
        """
        Train all models and evaluate
        
        Args:
            X_train, X_test: Training and testing features
            y_train, y_test: Training and testing labels
        """
        print("\nExtracting features...")
        X_train_features = self.feature_extractor.fit_transform(X_train)
        X_test_features = self.feature_extractor.transform(X_test)
        
        # Save vectorizer
        self.feature_extractor.save_vectorizer('models/vectorizer.pkl')
        
        print("\nTraining models...")
        best_accuracy = 0
        
        for name, model in self.models.items():
            print(f"\nTraining {name}...")
            
            # Train model
            model.fit(X_train_features, y_train)
            
            # Make predictions
            y_pred = model.predict(X_test_features)
            
            # Calculate metrics
            accuracy = accuracy_score(y_test, y_pred)
            precision = precision_score(y_test, y_pred)
            recall = recall_score(y_test, y_pred)
            f1 = f1_score(y_test, y_pred)
            
            # Store results
            self.results[name] = {
                'model': model,
                'accuracy': accuracy,
                'precision': precision,
                'recall': recall,
                'f1_score': f1,
                'predictions': y_pred
            }
            
            print(f"Accuracy: {accuracy:.4f}")
            print(f"Precision: {precision:.4f}")
            print(f"Recall: {recall:.4f}")
            print(f"F1-Score: {f1:.4f}")
            
            # Track best model
            if accuracy > best_accuracy:
                best_accuracy = accuracy
                self.best_model = model
                self.best_model_name = name
        
        print(f"\n{'='*50}")
        print(f"Best Model: {self.best_model_name}")
        print(f"Best Accuracy: {best_accuracy:.4f}")
        print(f"{'='*50}")
        
        # Save best model
        self._save_best_model()
        
        # Generate reports
        self._generate_reports(y_test)
    
    def _save_best_model(self):
        """Save the best performing model"""
        os.makedirs('models', exist_ok=True)
        model_path = 'models/best_model.pkl'
        joblib.dump(self.best_model, model_path)
        
        # Save model metadata
        metadata = {
            'model_name': self.best_model_name,
            'accuracy': self.results[self.best_model_name]['accuracy'],
            'precision': self.results[self.best_model_name]['precision'],
            'recall': self.results[self.best_model_name]['recall'],
            'f1_score': self.results[self.best_model_name]['f1_score']
        }
        joblib.dump(metadata, 'models/model_metadata.pkl')
        
        print(f"\nBest model saved to {model_path}")
    
    def _generate_reports(self, y_test):
        """Generate evaluation reports and visualizations"""
        os.makedirs('reports', exist_ok=True)
        
        # 1. Accuracy Comparison Chart
        self._plot_accuracy_comparison()
        
        # 2. Confusion Matrix for best model
        self._plot_confusion_matrix(y_test)
        
        # 3. Classification Report
        self._save_classification_report(y_test)
        
        # 4. Model Comparison Table
        self._save_comparison_table()
        
        print("\nReports generated in 'reports/' directory")
    
    def _plot_accuracy_comparison(self):
        """Plot accuracy comparison of all models"""
        plt.figure(figsize=(12, 6))
        
        models = list(self.results.keys())
        metrics = ['accuracy', 'precision', 'recall', 'f1_score']
        
        x = np.arange(len(models))
        width = 0.2
        
        for i, metric in enumerate(metrics):
            values = [self.results[model][metric] for model in models]
            plt.bar(x + i * width, values, width, label=metric.replace('_', ' ').title())
        
        plt.xlabel('Models', fontsize=12, fontweight='bold')
        plt.ylabel('Score', fontsize=12, fontweight='bold')
        plt.title('Model Performance Comparison', fontsize=14, fontweight='bold')
        plt.xticks(x + width * 1.5, models, rotation=45, ha='right')
        plt.legend()
        plt.ylim(0, 1.1)
        plt.grid(axis='y', alpha=0.3)
        plt.tight_layout()
        plt.savefig('reports/accuracy_comparison.png', dpi=300, bbox_inches='tight')
        plt.close()
    
    def _plot_confusion_matrix(self, y_test):
        """Plot confusion matrix for best model"""
        y_pred = self.results[self.best_model_name]['predictions']
        cm = confusion_matrix(y_test, y_pred)
        
        plt.figure(figsize=(8, 6))
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
                    xticklabels=['Ham', 'Spam'],
                    yticklabels=['Ham', 'Spam'])
        plt.title(f'Confusion Matrix - {self.best_model_name}', 
                  fontsize=14, fontweight='bold')
        plt.ylabel('Actual', fontsize=12, fontweight='bold')
        plt.xlabel('Predicted', fontsize=12, fontweight='bold')
        plt.tight_layout()
        plt.savefig('reports/confusion_matrix.png', dpi=300, bbox_inches='tight')
        plt.close()
    
    def _save_classification_report(self, y_test):
        """Save classification report to file"""
        y_pred = self.results[self.best_model_name]['predictions']
        report = classification_report(y_test, y_pred, 
                                       target_names=['Ham', 'Spam'])
        
        with open('reports/classification_report.txt', 'w') as f:
            f.write(f"Classification Report - {self.best_model_name}\n")
            f.write("=" * 60 + "\n\n")
            f.write(report)
    
    def _save_comparison_table(self):
        """Save model comparison table"""
        with open('reports/model_comparison.txt', 'w') as f:
            f.write("Model Performance Comparison\n")
            f.write("=" * 80 + "\n\n")
            f.write(f"{'Model':<20} {'Accuracy':<12} {'Precision':<12} {'Recall':<12} {'F1-Score':<12}\n")
            f.write("-" * 80 + "\n")
            
            for name, results in self.results.items():
                f.write(f"{name:<20} {results['accuracy']:<12.4f} "
                       f"{results['precision']:<12.4f} {results['recall']:<12.4f} "
                       f"{results['f1_score']:<12.4f}\n")
            
            f.write("\n" + "=" * 80 + "\n")
            f.write(f"Best Model: {self.best_model_name}\n")


def main():
    """Main training function"""
    print("=" * 60)
    print("Email Spam Detection - Model Training")
    print("=" * 60)
    
    # Initialize trainer
    trainer = SpamDetectionTrainer()
    
    # Load data
    X_train, X_test, y_train, y_test = trainer.load_data()
    
    # Train models
    trainer.train_models(X_train, X_test, y_train, y_test)
    
    print("\n" + "=" * 60)
    print("Training completed successfully!")
    print("=" * 60)


if __name__ == "__main__":
    main()
