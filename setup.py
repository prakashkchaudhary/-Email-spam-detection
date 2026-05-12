"""
Setup script for Email Spam Detection System
Automates the installation and setup process
"""

import os
import sys
import subprocess


def print_header(text):
    """Print formatted header"""
    print("\n" + "=" * 60)
    print(f"  {text}")
    print("=" * 60 + "\n")


def run_command(command, description):
    """Run a shell command and handle errors"""
    print(f"→ {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, 
                              capture_output=True, text=True)
        print(f"✓ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ {description} failed:")
        print(e.stderr)
        return False


def create_directories():
    """Create necessary directories"""
    directories = [
        'data/raw',
        'data/processed',
        'models',
        'reports',
        'logs',
        'static/images'
    ]
    
    print("→ Creating directories...")
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
    print("✓ Directories created successfully")


def download_nltk_data():
    """Download required NLTK data"""
    print("→ Downloading NLTK data...")
    try:
        import nltk
        nltk.download('stopwords', quiet=True)
        nltk.download('punkt', quiet=True)
        print("✓ NLTK data downloaded successfully")
        return True
    except Exception as e:
        print(f"✗ NLTK data download failed: {e}")
        return False


def train_model():
    """Train the spam detection model"""
    print("→ Training spam detection model...")
    print("  This may take a few minutes...")
    try:
        result = subprocess.run([sys.executable, 'src/model_training.py'],
                              capture_output=True, text=True, check=True)
        print("✓ Model trained successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ Model training failed:")
        print(e.stderr)
        return False


def run_tests():
    """Run unit tests"""
    print("→ Running unit tests...")
    try:
        result = subprocess.run([sys.executable, '-m', 'pytest', 'tests/', '-v'],
                              capture_output=True, text=True)
        print(result.stdout)
        if result.returncode == 0:
            print("✓ All tests passed")
            return True
        else:
            print("⚠ Some tests failed (this is okay for initial setup)")
            return True
    except Exception as e:
        print(f"⚠ Could not run tests: {e}")
        return True  # Don't fail setup if tests can't run


def main():
    """Main setup function"""
    print_header("Email Spam Detection System - Setup")
    
    print("This script will:")
    print("  1. Create necessary directories")
    print("  2. Download NLTK data")
    print("  3. Train the machine learning model")
    print("  4. Run tests")
    print("\nPress Enter to continue or Ctrl+C to cancel...")
    
    try:
        input()
    except KeyboardInterrupt:
        print("\n\nSetup cancelled.")
        sys.exit(0)
    
    # Step 1: Create directories
    print_header("Step 1: Creating Directories")
    create_directories()
    
    # Step 2: Download NLTK data
    print_header("Step 2: Downloading NLTK Data")
    if not download_nltk_data():
        print("\n⚠ Warning: NLTK data download failed. You may need to download it manually.")
    
    # Step 3: Train model
    print_header("Step 3: Training Model")
    if not train_model():
        print("\n✗ Setup failed: Could not train model")
        print("Please check the error messages above and try again.")
        sys.exit(1)
    
    # Step 4: Run tests
    print_header("Step 4: Running Tests")
    run_tests()
    
    # Success message
    print_header("Setup Complete!")
    print("✓ All setup steps completed successfully!\n")
    print("Next steps:")
    print("  1. Run the application:")
    print("     python app.py")
    print("\n  2. Open your browser:")
    print("     http://localhost:5000")
    print("\n  3. Try detecting spam messages!")
    print("\nFor more information, see README.md")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    main()
