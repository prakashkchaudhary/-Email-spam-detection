# Quick Start Guide - Email Spam Detection System

Get up and running in 5 minutes! ⚡

## Option 1: Automated Setup (Recommended)

### Windows

1. **Double-click** `run.bat`
2. Wait for setup to complete
3. Open browser to `http://localhost:5000`

### macOS/Linux

1. **Make script executable:**
   ```bash
   chmod +x run.sh
   ```

2. **Run the script:**
   ```bash
   ./run.sh
   ```

3. **Open browser** to `http://localhost:5000`

## Option 2: Manual Setup

### Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 2: Download NLTK Data

```bash
python -c "import nltk; nltk.download('stopwords'); nltk.download('punkt')"
```

### Step 3: Train Model

```bash
python src/model_training.py
```

### Step 4: Run Application

```bash
python app.py
```

### Step 5: Open Browser

Navigate to: `http://localhost:5000`

## Option 3: Using Setup Script

```bash
python setup.py
```

This will automatically:
- Create directories
- Download NLTK data
- Train the model
- Run tests

## Testing the Application

### 1. Home Page

Visit `http://localhost:5000` to see the landing page.

### 2. Detect Spam

1. Click **"Detect Spam"** in navigation
2. Enter a message or click **"Load Sample"**
3. Click **"Check for Spam"**
4. View the prediction result

### 3. Sample Messages to Try

**Spam Examples:**
```
Congratulations! You've won $1000. Call now to claim your prize!
URGENT: Your account will be suspended. Click here immediately!
Free entry to win iPhone. Text WIN to 12345
```

**Ham Examples:**
```
Hey, can we meet for coffee tomorrow at 3 PM?
Thanks for the meeting today. I'll send the report by Friday.
Don't forget to pick up milk on your way home.
```

## Troubleshooting

### Model Not Found Error

```bash
python src/model_training.py
```

### Module Not Found Error

```bash
pip install -r requirements.txt
```

### Port Already in Use

Change port in `app.py`:
```python
port = 5001  # Change from 5000
```

## Next Steps

1. **Explore the Code**
   - Check `src/` for ML implementation
   - Review `templates/` for frontend
   - Read `app.py` for Flask routes

2. **Customize**
   - Modify UI in `static/css/style.css`
   - Add features in `app.py`
   - Improve model in `src/model_training.py`

3. **Deploy**
   - See `DEPLOYMENT.md` for deployment guides
   - Deploy to Render, Railway, or Heroku

## Project Structure

```
email-spam-detection/
├── app.py                 # Flask application
├── src/                   # Source code
│   ├── preprocessing.py   # Text preprocessing
│   ├── feature_extraction.py
│   ├── model_training.py  # Train models
│   └── prediction.py      # Make predictions
├── templates/             # HTML templates
├── static/                # CSS, JS files
├── models/                # Trained models
├── data/                  # Dataset
└── tests/                 # Unit tests
```

## Key Features

✅ Multiple ML models (Naive Bayes, SVM, Random Forest, Logistic Regression)  
✅ 98%+ accuracy  
✅ Real-time predictions  
✅ Modern, responsive UI  
✅ Dark/light mode  
✅ Prediction history  
✅ File upload support  
✅ RESTful API  

## API Usage

### Predict Endpoint

```bash
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{"message": "Your message here"}'
```

**Response:**
```json
{
  "prediction": "Spam",
  "confidence": 98.5,
  "message": "This message appears to be SPAM!",
  "timestamp": "2024-01-01 12:00:00"
}
```

## Keyboard Shortcuts

When on detection page:
- `Ctrl/Cmd + Enter` - Check for spam
- `Ctrl/Cmd + K` - Clear input
- `Ctrl/Cmd + L` - Load sample

## Documentation

- **Full Guide:** See `README.md`
- **Installation:** See `INSTALLATION.md`
- **Deployment:** See `DEPLOYMENT.md`
- **Contributing:** See `CONTRIBUTING.md`

## Support

- **Issues:** Open an issue on GitHub
- **Email:** your.email@example.com
- **Documentation:** Check README.md

## License

MIT License - See `LICENSE` file

---

**Ready to detect spam!** 🛡️

For detailed information, see the full `README.md` file.
