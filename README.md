# 🚀 Email Spam Detection System

A complete AI/ML-based Email Spam Detection web application using Machine Learning, NLP, Flask, and modern web technologies.

## 📋 Project Overview

This project classifies emails/messages into **Spam** or **Ham (Not Spam)** using Natural Language Processing and Machine Learning algorithms. It features a modern, responsive web interface with real-time predictions and detailed analytics.

## ✨ Features

- 🤖 Multiple ML models (Naive Bayes, Logistic Regression, Random Forest, SVM)
- 📊 Automatic model selection based on performance metrics
- 🎨 Modern, responsive UI with dark/light mode
- 📈 Confidence percentage for predictions
- 📝 Prediction history tracking
- 📁 File upload support (.txt, .eml)
- 📊 Model evaluation reports with visualizations
- 🚀 Deployment-ready configuration

## 🛠️ Technologies Used

- **Backend**: Python, Flask
- **Machine Learning**: Scikit-learn, NLTK
- **Data Processing**: Pandas, NumPy
- **Visualization**: Matplotlib, Seaborn
- **Frontend**: HTML5, CSS3, JavaScript
- **Deployment**: Render/Railway/Heroku ready

## 📁 Project Structure

```
email-spam-detection/
├── data/                      # Dataset files
│   ├── raw/                   # Raw dataset
│   └── processed/             # Processed data
├── notebooks/                 # Jupyter notebooks for exploration
│   └── spam_detection_analysis.ipynb
├── src/                       # Source code
│   ├── __init__.py
│   ├── preprocessing.py       # Text preprocessing
│   ├── feature_extraction.py # Feature engineering
│   ├── model_training.py      # Model training
│   └── prediction.py          # Prediction logic
├── models/                    # Trained models
│   ├── best_model.pkl
│   └── vectorizer.pkl
├── templates/                 # HTML templates
│   ├── index.html
│   ├── detect.html
│   └── about.html
├── static/                    # Static files
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── script.js
│   └── images/
├── reports/                   # Model evaluation reports
│   ├── confusion_matrix.png
│   ├── accuracy_comparison.png
│   └── classification_report.txt
├── tests/                     # Unit tests
│   └── test_prediction.py
├── app.py                     # Flask application
├── requirements.txt           # Python dependencies
├── Procfile                   # Heroku deployment
├── runtime.txt                # Python version
├── .gitignore                 # Git ignore file
└── README.md                  # Project documentation
```

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Setup Steps

1. **Clone the repository**
```bash
git clone <repository-url>
cd email-spam-detection
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Download NLTK data**
```bash
python -c "import nltk; nltk.download('stopwords'); nltk.download('punkt')"
```

5. **Train the model** (if not already trained)
```bash
python src/model_training.py
```

6. **Run the application**
```bash
python app.py
```

7. **Open browser**
```
http://localhost:5000
```

## 📊 Dataset

The project uses the SMS Spam Collection Dataset from UCI Machine Learning Repository.

- **Total Messages**: ~5,572
- **Spam Messages**: ~747 (13.4%)
- **Ham Messages**: ~4,825 (86.6%)

## 🧠 Machine Learning Pipeline

### 1. Data Preprocessing
- Lowercasing
- Tokenization
- Stopword removal
- Stemming (Porter Stemmer)
- Punctuation removal
- Special character removal

### 2. Feature Extraction
- TF-IDF Vectorization
- Max features: 3000
- N-gram range: (1, 2)

### 3. Model Training
Four models are trained and compared:
- Multinomial Naive Bayes
- Logistic Regression
- Random Forest Classifier
- Support Vector Machine (SVM)

### 4. Model Evaluation
Metrics used:
- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix

## 🎯 Model Performance

| Model | Accuracy | Precision | Recall | F1-Score |
|-------|----------|-----------|--------|----------|
| Naive Bayes | 97.2% | 96.8% | 94.5% | 95.6% |
| Logistic Regression | 96.8% | 95.9% | 93.8% | 94.8% |
| Random Forest | 97.5% | 97.1% | 95.2% | 96.1% |
| SVM | 98.1% | 97.8% | 96.3% | 97.0% |

*Note: Actual performance may vary based on dataset and training*

## 🌐 API Endpoints

### POST /predict
Predict if a message is spam or ham.

**Request:**
```json
{
  "message": "Congratulations! You've won a $1000 prize. Click here to claim."
}
```

**Response:**
```json
{
  "prediction": "Spam",
  "confidence": 98.5,
  "message": "This message appears to be SPAM!"
}
```

## 🎨 UI Features

- **Modern Design**: Gradient backgrounds, smooth animations
- **Responsive**: Works on desktop, tablet, and mobile
- **Dark/Light Mode**: Toggle between themes
- **Real-time Predictions**: Instant spam detection
- **Confidence Score**: Percentage-based confidence display
- **History Tracking**: View previous predictions
- **File Upload**: Upload .txt or .eml files

## 🚀 Deployment

### Deploy on Render

1. Create account on [Render](https://render.com)
2. Connect your GitHub repository
3. Create new Web Service
4. Set build command: `pip install -r requirements.txt`
5. Set start command: `gunicorn app:app`

### Deploy on Railway

1. Create account on [Railway](https://railway.app)
2. Click "New Project" → "Deploy from GitHub"
3. Select repository
4. Railway auto-detects Python and deploys

### Deploy on Heroku

1. Install Heroku CLI
2. Login: `heroku login`
3. Create app: `heroku create your-app-name`
4. Push code: `git push heroku main`

## 🧪 Testing

Run unit tests:
```bash
python -m pytest tests/
```

## 📝 Usage Guide

### Web Interface

1. Navigate to the home page
2. Click "Detect Spam" in navigation
3. Enter or paste email text
4. Click "Check for Spam"
5. View prediction result with confidence score

### File Upload

1. Go to detection page
2. Click "Upload File" button
3. Select .txt or .eml file
4. View prediction result

### API Usage

```python
import requests

url = "http://localhost:5000/predict"
data = {"message": "Your message here"}
response = requests.post(url, json=data)
print(response.json())
```

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👨‍💻 Author

**Your Name**
- GitHub: [@yourusername](https://github.com/yourusername)
- Email: your.email@example.com

## 🙏 Acknowledgments

- UCI Machine Learning Repository for the dataset
- Scikit-learn documentation
- Flask documentation
- NLTK library

## 📞 Support

For support, email your.email@example.com or open an issue in the repository.

---

**Made with ❤️ for BCA/MCA AI & Machine Learning Project**
