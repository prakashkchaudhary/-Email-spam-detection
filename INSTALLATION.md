# Installation Guide - Email Spam Detection System

Complete step-by-step installation guide for the Email Spam Detection project.

## Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.8 or higher** ([Download Python](https://www.python.org/downloads/))
- **pip** (Python package manager - comes with Python)
- **Git** (optional, for cloning repository)
- **Virtual environment** (recommended)

## Installation Steps

### 1. Download/Clone the Project

**Option A: Clone from Git**
```bash
git clone <repository-url>
cd email-spam-detection
```

**Option B: Download ZIP**
- Download the project ZIP file
- Extract to your desired location
- Open terminal/command prompt in the project directory

### 2. Create Virtual Environment (Recommended)

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

You should see `(venv)` in your terminal prompt.

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

This will install all required packages:
- Flask (web framework)
- scikit-learn (machine learning)
- nltk (natural language processing)
- pandas, numpy (data processing)
- matplotlib, seaborn (visualization)

### 4. Download NLTK Data

Run the following Python commands:

```bash
python -c "import nltk; nltk.download('stopwords'); nltk.download('punkt')"
```

Or run Python interactively:
```python
import nltk
nltk.download('stopwords')
nltk.download('punkt')
```

### 5. Prepare Dataset

**Option A: Use Sample Dataset (Automatic)**
The system will automatically create a sample dataset if none exists.

**Option B: Use Real Dataset**
1. Download the SMS Spam Collection Dataset from [UCI Repository](https://archive.ics.uci.edu/ml/datasets/SMS+Spam+Collection)
2. Place the `spam.csv` file in `data/raw/` directory
3. Ensure the CSV has columns: `label` (spam/ham) and `text` (message)

### 6. Train the Model

```bash
python src/model_training.py
```

This will:
- Load and preprocess the dataset
- Train multiple ML models
- Select the best performing model
- Save the model and vectorizer to `models/` directory
- Generate evaluation reports in `reports/` directory

Expected output:
```
Loading dataset...
Preprocessing text...
Training samples: 4457
Testing samples: 1115
Training models...
Best Model: SVM
Best Accuracy: 0.9810
```

### 7. Run the Application

```bash
python app.py
```

The application will start on `http://localhost:5000`

You should see:
```
Model loaded from models/best_model.pkl
Vectorizer loaded from models/vectorizer.pkl
 * Running on http://0.0.0.0:5000
```

### 8. Access the Application

Open your web browser and navigate to:
```
http://localhost:5000
```

## Verification

### Test the Installation

1. **Check Python version:**
```bash
python --version
```
Should show Python 3.8 or higher

2. **Check installed packages:**
```bash
pip list
```
Should show Flask, scikit-learn, nltk, etc.

3. **Test model prediction:**
```bash
python src/prediction.py
```

4. **Run unit tests:**
```bash
python -m pytest tests/
```

## Troubleshooting

### Common Issues

#### 1. ModuleNotFoundError

**Problem:** `ModuleNotFoundError: No module named 'flask'`

**Solution:**
```bash
pip install -r requirements.txt
```

#### 2. NLTK Data Not Found

**Problem:** `LookupError: Resource stopwords not found`

**Solution:**
```bash
python -c "import nltk; nltk.download('stopwords'); nltk.download('punkt')"
```

#### 3. Model Not Found

**Problem:** `FileNotFoundError: Model not found at models/best_model.pkl`

**Solution:**
```bash
python src/model_training.py
```

#### 4. Port Already in Use

**Problem:** `OSError: [Errno 48] Address already in use`

**Solution:**
```bash
# Use a different port
python app.py --port 5001
```

Or kill the process using port 5000:
```bash
# Windows
netstat -ano | findstr :5000
taskkill /PID <PID> /F

# macOS/Linux
lsof -ti:5000 | xargs kill -9
```

#### 5. Permission Denied

**Problem:** `PermissionError: [Errno 13] Permission denied`

**Solution:**
- Run terminal as administrator (Windows)
- Use `sudo` (macOS/Linux)
- Check file permissions

#### 6. SSL Certificate Error

**Problem:** `SSL: CERTIFICATE_VERIFY_FAILED`

**Solution:**
```bash
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt
```

## Directory Structure After Installation

```
email-spam-detection/
├── data/
│   ├── raw/
│   │   └── spam.csv              # Dataset
│   └── processed/
├── models/
│   ├── best_model.pkl            # Trained model
│   ├── vectorizer.pkl            # TF-IDF vectorizer
│   └── model_metadata.pkl        # Model info
├── reports/
│   ├── confusion_matrix.png      # Evaluation charts
│   ├── accuracy_comparison.png
│   └── classification_report.txt
├── venv/                         # Virtual environment
└── ... (other files)
```

## Next Steps

After successful installation:

1. **Explore the Web Interface**
   - Visit http://localhost:5000
   - Try the spam detection feature
   - Test with different messages

2. **Review the Code**
   - Check `src/` directory for implementation
   - Read `notebooks/` for analysis

3. **Customize the Project**
   - Add more training data
   - Experiment with different models
   - Modify the UI/UX

4. **Deploy to Production**
   - See deployment guides for Render, Railway, or Heroku
   - Configure environment variables
   - Set up monitoring

## Additional Resources

- **Flask Documentation:** https://flask.palletsprojects.com/
- **Scikit-learn Documentation:** https://scikit-learn.org/
- **NLTK Documentation:** https://www.nltk.org/
- **Project README:** See README.md for detailed information

## Support

If you encounter any issues:

1. Check the troubleshooting section above
2. Review error messages carefully
3. Search for similar issues online
4. Contact: your.email@example.com

## Uninstallation

To remove the project:

1. Deactivate virtual environment:
```bash
deactivate
```

2. Delete project directory:
```bash
# Be careful with this command!
rm -rf email-spam-detection/
```

3. Remove Python packages (if needed):
```bash
pip uninstall -r requirements.txt -y
```

---

**Installation Complete!** 🎉

You're now ready to use the Email Spam Detection System.
