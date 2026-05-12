# Email Spam Detection - Command Reference

Quick reference for all commands used in the project.

## 📦 Installation Commands

### Create Virtual Environment
```bash
# Windows
python -m venv venv

# macOS/Linux
python3 -m venv venv
```

### Activate Virtual Environment
```bash
# Windows (Command Prompt)
venv\Scripts\activate

# Windows (PowerShell)
venv\Scripts\Activate.ps1

# macOS/Linux
source venv/bin/activate
```

### Deactivate Virtual Environment
```bash
deactivate
```

### Install Dependencies
```bash
# Install all requirements
pip install -r requirements.txt

# Install specific package
pip install flask

# Upgrade pip
python -m pip install --upgrade pip
```

### Download NLTK Data
```bash
# Quick method
python -c "import nltk; nltk.download('stopwords'); nltk.download('punkt')"

# Interactive method
python
>>> import nltk
>>> nltk.download('stopwords')
>>> nltk.download('punkt')
>>> exit()
```

## 🤖 Model Commands

### Train Model
```bash
# Train all models and select best
python src/model_training.py

# With output redirection
python src/model_training.py > training_log.txt
```

### Test Prediction
```bash
# Run prediction tests
python src/prediction.py

# Test preprocessing
python src/preprocessing.py

# Test feature extraction
python src/feature_extraction.py
```

## 🚀 Application Commands

### Run Application
```bash
# Standard run
python app.py

# With specific port
python app.py --port 5001

# With debug mode
FLASK_DEBUG=1 python app.py
```

### Run with Gunicorn (Production)
```bash
# Basic
gunicorn app:app

# With workers
gunicorn -w 4 app:app

# With specific port
gunicorn -w 4 -b 0.0.0.0:5000 app:app

# With logging
gunicorn -w 4 --access-logfile - --error-logfile - app:app
```

## 🧪 Testing Commands

### Run All Tests
```bash
# Using pytest
python -m pytest tests/

# With verbose output
python -m pytest tests/ -v

# With coverage
python -m pytest tests/ --cov=src

# Specific test file
python -m pytest tests/test_prediction.py
```

### Run Specific Tests
```bash
# Run single test class
python -m pytest tests/test_prediction.py::TestTextPreprocessing

# Run single test method
python -m pytest tests/test_prediction.py::TestTextPreprocessing::test_lowercase
```

### Direct Test Execution
```bash
# Run test file directly
python tests/test_prediction.py
```

## 📊 Data Commands

### Check Dataset
```bash
# View first few lines
head data/raw/spam.csv

# Count lines
wc -l data/raw/spam.csv

# Windows equivalent
type data\raw\spam.csv | more
```

### Data Analysis
```bash
# Run Jupyter notebook
jupyter notebook notebooks/spam_detection_analysis.ipynb

# Convert notebook to HTML
jupyter nbconvert --to html notebooks/spam_detection_analysis.ipynb
```

## 🔍 Debugging Commands

### Check Python Version
```bash
python --version
python3 --version
```

### Check Installed Packages
```bash
# List all packages
pip list

# Show specific package
pip show flask

# Check outdated packages
pip list --outdated
```

### Check File Structure
```bash
# List files (Unix/Linux/macOS)
ls -la
tree

# Windows
dir
tree /F
```

### View Logs
```bash
# View application logs (if logging enabled)
tail -f logs/app.log

# Windows
type logs\app.log
```

## 🌐 API Commands

### Test API with curl

#### Predict Endpoint
```bash
# POST request
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{"message": "Congratulations! You won $1000"}'

# Windows (PowerShell)
Invoke-RestMethod -Uri http://localhost:5000/predict `
  -Method Post `
  -ContentType "application/json" `
  -Body '{"message": "Congratulations! You won $1000"}'
```

#### Health Check
```bash
curl http://localhost:5000/health

# Windows
Invoke-RestMethod -Uri http://localhost:5000/health
```

#### Model Info
```bash
curl http://localhost:5000/model-info

# Windows
Invoke-RestMethod -Uri http://localhost:5000/model-info
```

#### History
```bash
curl http://localhost:5000/history

# Windows
Invoke-RestMethod -Uri http://localhost:5000/history
```

### Test API with Python
```python
import requests

# Predict
response = requests.post(
    'http://localhost:5000/predict',
    json={'message': 'Your message here'}
)
print(response.json())

# Health check
response = requests.get('http://localhost:5000/health')
print(response.json())
```

## 🚢 Deployment Commands

### Git Commands
```bash
# Initialize repository
git init

# Add files
git add .

# Commit
git commit -m "Initial commit"

# Add remote
git remote add origin <repository-url>

# Push
git push -u origin main
```

### Heroku Commands
```bash
# Login
heroku login

# Create app
heroku create your-app-name

# Deploy
git push heroku main

# View logs
heroku logs --tail

# Open app
heroku open

# Set environment variable
heroku config:set VARIABLE_NAME=value

# Scale dynos
heroku ps:scale web=1
```

### Render Commands
```bash
# Deploy via dashboard (no CLI needed)
# Or use render.yaml for configuration
```

### Railway Commands
```bash
# Install CLI
npm install -g @railway/cli

# Login
railway login

# Initialize
railway init

# Deploy
railway up
```

## 🔧 Maintenance Commands

### Update Dependencies
```bash
# Update all packages
pip install --upgrade -r requirements.txt

# Update specific package
pip install --upgrade flask

# Generate new requirements
pip freeze > requirements.txt
```

### Clean Project
```bash
# Remove Python cache (Unix/Linux/macOS)
find . -type d -name "__pycache__" -exec rm -r {} +
find . -type f -name "*.pyc" -delete

# Windows
for /d /r . %d in (__pycache__) do @if exist "%d" rd /s /q "%d"
del /s /q *.pyc
```

### Backup
```bash
# Create backup
tar -czf backup.tar.gz email-spam-detection/

# Windows (using 7-Zip)
7z a backup.7z email-spam-detection\
```

## 📝 Code Quality Commands

### Linting
```bash
# Install flake8
pip install flake8

# Run linter
flake8 src/ app.py

# With specific rules
flake8 --max-line-length=100 src/
```

### Formatting
```bash
# Install black
pip install black

# Format code
black src/ app.py

# Check without modifying
black --check src/
```

### Type Checking
```bash
# Install mypy
pip install mypy

# Run type checker
mypy src/
```

## 🔒 Security Commands

### Check for Vulnerabilities
```bash
# Install safety
pip install safety

# Check dependencies
safety check

# Check requirements file
safety check -r requirements.txt
```

### Generate Secret Key
```bash
# Python
python -c "import secrets; print(secrets.token_hex(32))"

# OpenSSL
openssl rand -hex 32
```

## 📊 Performance Commands

### Profile Application
```bash
# Install profiler
pip install py-spy

# Profile running application
py-spy top --pid <process-id>

# Generate flame graph
py-spy record -o profile.svg -- python app.py
```

### Memory Usage
```bash
# Install memory profiler
pip install memory_profiler

# Profile memory
python -m memory_profiler src/model_training.py
```

## 🛠️ Utility Commands

### Port Management
```bash
# Check port usage (Unix/Linux/macOS)
lsof -i :5000

# Kill process on port
kill -9 $(lsof -t -i:5000)

# Windows
netstat -ano | findstr :5000
taskkill /PID <PID> /F
```

### Environment Variables
```bash
# Set environment variable (Unix/Linux/macOS)
export FLASK_ENV=production

# Windows (Command Prompt)
set FLASK_ENV=production

# Windows (PowerShell)
$env:FLASK_ENV="production"

# Load from .env file
pip install python-dotenv
```

### File Operations
```bash
# Create directories
mkdir -p data/raw data/processed models reports

# Windows
mkdir data\raw data\processed models reports

# Copy files
cp source.txt destination.txt

# Windows
copy source.txt destination.txt

# Move files
mv old_name.txt new_name.txt

# Windows
move old_name.txt new_name.txt
```

## 🎯 Quick Commands

### One-Line Setup
```bash
# Complete setup in one command
python -m venv venv && source venv/bin/activate && pip install -r requirements.txt && python src/model_training.py && python app.py
```

### Quick Test
```bash
# Test everything quickly
python -m pytest tests/ -v && python app.py
```

### Quick Deploy
```bash
# Commit and deploy
git add . && git commit -m "Update" && git push heroku main
```

## 📱 Mobile Testing Commands

### Using ngrok
```bash
# Install ngrok
# Download from https://ngrok.com

# Expose local server
ngrok http 5000

# Use the provided URL to test on mobile
```

## 🔄 Automation Commands

### Run Setup Script
```bash
# Automated setup
python setup.py

# Windows batch script
run.bat

# Unix/Linux/macOS shell script
chmod +x run.sh
./run.sh
```

### Scheduled Tasks
```bash
# Cron job (Unix/Linux/macOS)
# Edit crontab
crontab -e

# Add line to run daily at 2 AM
0 2 * * * cd /path/to/project && python src/model_training.py

# Windows Task Scheduler
# Use Task Scheduler GUI or schtasks command
```

## 📚 Documentation Commands

### Generate Documentation
```bash
# Install Sphinx
pip install sphinx

# Initialize
sphinx-quickstart docs

# Build HTML docs
cd docs && make html
```

### View Documentation
```bash
# Open in browser (Unix/Linux/macOS)
open docs/_build/html/index.html

# Windows
start docs\_build\html\index.html
```

## 🎓 Learning Commands

### Interactive Python
```bash
# Start Python REPL
python

# Import and test modules
>>> from src.preprocessing import TextPreprocessor
>>> preprocessor = TextPreprocessor()
>>> preprocessor.preprocess("Test message")
```

### IPython
```bash
# Install IPython
pip install ipython

# Start IPython
ipython

# Better REPL with autocomplete and syntax highlighting
```

---

## 📋 Command Cheat Sheet

### Most Used Commands
```bash
# Setup
pip install -r requirements.txt
python src/model_training.py

# Run
python app.py

# Test
python -m pytest tests/

# Deploy
git push heroku main
```

### Troubleshooting Commands
```bash
# Check everything
python --version
pip list
python src/prediction.py
python -m pytest tests/
```

---

**Save this file for quick reference!** 📌

For more details, see the full documentation in `README.md` and other guide files.
