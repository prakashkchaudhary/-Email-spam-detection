@echo off
REM Windows batch script to run the Email Spam Detection application

echo ========================================
echo Email Spam Detection System
echo ========================================
echo.

REM Check if virtual environment exists
if not exist "venv\" (
    echo Creating virtual environment...
    python -m venv venv
    echo.
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate
echo.

REM Install dependencies if needed
if not exist "venv\Lib\site-packages\flask\" (
    echo Installing dependencies...
    pip install -r requirements.txt
    echo.
)

REM Check if model exists
if not exist "models\best_model.pkl" (
    echo Model not found. Training model...
    python src\model_training.py
    echo.
)

REM Run the application
echo Starting application...
echo.
echo Application will be available at: http://localhost:5000
echo Press Ctrl+C to stop the server
echo.
python app.py

pause
