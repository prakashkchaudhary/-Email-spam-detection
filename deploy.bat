@echo off
REM Deployment script for Email Spam Detection System (Windows)

echo ==========================================
echo Email Spam Detection - Deployment Script
echo ==========================================
echo.

REM Check if Git is initialized
if not exist ".git\" (
    echo Initializing Git repository...
    git init
    echo [OK] Git initialized
) else (
    echo [OK] Git already initialized
)

REM Add all files
echo Adding files to Git...
git add .
echo [OK] Files added

REM Commit
echo Creating commit...
git commit -m "Deploy: Email Spam Detection System"
echo [OK] Commit created

REM Ask for GitHub repository URL
echo.
echo ==========================================
echo GitHub Repository Setup
echo ==========================================
echo.
echo Please create a new repository on GitHub:
echo 1. Go to https://github.com/new
echo 2. Create repository named: email-spam-detection
echo 3. Don't initialize with README
echo.
set /p REPO_URL="Enter your GitHub repository URL: "

if "%REPO_URL%"=="" (
    echo [ERROR] No repository URL provided
    pause
    exit /b 1
)

REM Add remote
echo Adding remote repository...
git remote remove origin 2>nul
git remote add origin %REPO_URL%
echo [OK] Remote added

REM Rename branch to main
echo Setting branch to main...
git branch -M main
echo [OK] Branch set to main

REM Push to GitHub
echo Pushing to GitHub...
git push -u origin main
echo [OK] Pushed to GitHub

echo.
echo ==========================================
echo Deployment Options
echo ==========================================
echo.
echo Your code is now on GitHub!
echo.
echo Choose deployment platform:
echo 1. Vercel (Recommended for serverless)
echo 2. Render (Recommended for full-stack)
echo 3. Both
echo.
set /p DEPLOY_CHOICE="Enter choice (1/2/3): "

if "%DEPLOY_CHOICE%"=="1" (
    echo.
    echo ==========================================
    echo Deploying to Vercel
    echo ==========================================
    echo.
    echo Steps:
    echo 1. Go to https://vercel.com
    echo 2. Sign in with GitHub
    echo 3. Click 'Add New Project'
    echo 4. Import your repository: email-spam-detection
    echo 5. Click 'Deploy'
    echo.
    echo Your app will be live at: https://your-project.vercel.app
)

if "%DEPLOY_CHOICE%"=="2" (
    echo.
    echo ==========================================
    echo Deploying to Render
    echo ==========================================
    echo.
    echo Steps:
    echo 1. Go to https://render.com
    echo 2. Sign in with GitHub
    echo 3. Click 'New +' -^> 'Web Service'
    echo 4. Connect your repository: email-spam-detection
    echo 5. Configure build and start commands
    echo 6. Click 'Create Web Service'
    echo.
    echo Your app will be live at: https://your-app.onrender.com
)

if "%DEPLOY_CHOICE%"=="3" (
    echo.
    echo ==========================================
    echo Deploying to Both Platforms
    echo ==========================================
    echo.
    echo Follow the steps for both Vercel and Render above
)

echo.
echo ==========================================
echo Deployment Complete!
echo ==========================================
echo.
echo [OK] Code pushed to GitHub
echo [OK] Ready for deployment
echo.
echo For detailed instructions, see DEPLOYMENT_GUIDE.md
echo.
echo Happy Deploying! 🚀
echo.
pause
