#!/bin/bash
# Deployment script for Email Spam Detection System

echo "=========================================="
echo "Email Spam Detection - Deployment Script"
echo "=========================================="
echo ""

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Check if Git is initialized
if [ ! -d ".git" ]; then
    echo -e "${BLUE}Initializing Git repository...${NC}"
    git init
    echo -e "${GREEN}✓ Git initialized${NC}"
else
    echo -e "${GREEN}✓ Git already initialized${NC}"
fi

# Add all files
echo -e "${BLUE}Adding files to Git...${NC}"
git add .
echo -e "${GREEN}✓ Files added${NC}"

# Commit
echo -e "${BLUE}Creating commit...${NC}"
git commit -m "Deploy: Email Spam Detection System"
echo -e "${GREEN}✓ Commit created${NC}"

# Ask for GitHub repository URL
echo ""
echo "=========================================="
echo "GitHub Repository Setup"
echo "=========================================="
echo ""
echo "Please create a new repository on GitHub:"
echo "1. Go to https://github.com/new"
echo "2. Create repository named: email-spam-detection"
echo "3. Don't initialize with README"
echo ""
read -p "Enter your GitHub repository URL (e.g., https://github.com/username/email-spam-detection.git): " REPO_URL

if [ -z "$REPO_URL" ]; then
    echo -e "${RED}✗ No repository URL provided${NC}"
    exit 1
fi

# Add remote
echo -e "${BLUE}Adding remote repository...${NC}"
git remote remove origin 2>/dev/null
git remote add origin "$REPO_URL"
echo -e "${GREEN}✓ Remote added${NC}"

# Rename branch to main
echo -e "${BLUE}Setting branch to main...${NC}"
git branch -M main
echo -e "${GREEN}✓ Branch set to main${NC}"

# Push to GitHub
echo -e "${BLUE}Pushing to GitHub...${NC}"
git push -u origin main
echo -e "${GREEN}✓ Pushed to GitHub${NC}"

echo ""
echo "=========================================="
echo "Deployment Options"
echo "=========================================="
echo ""
echo "Your code is now on GitHub!"
echo ""
echo "Choose deployment platform:"
echo "1. Vercel (Recommended for serverless)"
echo "2. Render (Recommended for full-stack)"
echo "3. Both"
echo ""
read -p "Enter choice (1/2/3): " DEPLOY_CHOICE

case $DEPLOY_CHOICE in
    1)
        echo ""
        echo "=========================================="
        echo "Deploying to Vercel"
        echo "=========================================="
        echo ""
        echo "Steps:"
        echo "1. Go to https://vercel.com"
        echo "2. Sign in with GitHub"
        echo "3. Click 'Add New Project'"
        echo "4. Import your repository: email-spam-detection"
        echo "5. Click 'Deploy'"
        echo ""
        echo "Your app will be live at: https://your-project.vercel.app"
        ;;
    2)
        echo ""
        echo "=========================================="
        echo "Deploying to Render"
        echo "=========================================="
        echo ""
        echo "Steps:"
        echo "1. Go to https://render.com"
        echo "2. Sign in with GitHub"
        echo "3. Click 'New +' → 'Web Service'"
        echo "4. Connect your repository: email-spam-detection"
        echo "5. Configure:"
        echo "   - Build Command: pip install -r requirements.txt && python -c \"import nltk; nltk.download('stopwords'); nltk.download('punkt')\" && python src/model_training.py"
        echo "   - Start Command: gunicorn app:app"
        echo "6. Click 'Create Web Service'"
        echo ""
        echo "Your app will be live at: https://your-app.onrender.com"
        ;;
    3)
        echo ""
        echo "=========================================="
        echo "Deploying to Both Platforms"
        echo "=========================================="
        echo ""
        echo "Vercel Steps:"
        echo "1. Go to https://vercel.com"
        echo "2. Sign in with GitHub"
        echo "3. Click 'Add New Project'"
        echo "4. Import your repository"
        echo "5. Click 'Deploy'"
        echo ""
        echo "Render Steps:"
        echo "1. Go to https://render.com"
        echo "2. Sign in with GitHub"
        echo "3. Click 'New +' → 'Web Service'"
        echo "4. Connect your repository"
        echo "5. Use the configuration from render.yaml"
        echo "6. Click 'Create Web Service'"
        ;;
    *)
        echo -e "${RED}Invalid choice${NC}"
        exit 1
        ;;
esac

echo ""
echo "=========================================="
echo "Deployment Complete!"
echo "=========================================="
echo ""
echo -e "${GREEN}✓ Code pushed to GitHub${NC}"
echo -e "${GREEN}✓ Ready for deployment${NC}"
echo ""
echo "For detailed instructions, see DEPLOYMENT_GUIDE.md"
echo ""
echo "Happy Deploying! 🚀"
