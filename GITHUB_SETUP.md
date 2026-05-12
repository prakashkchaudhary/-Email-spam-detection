# GitHub Setup Guide

Quick guide to push your project to GitHub and deploy.

## 🚀 Quick Setup (5 Minutes)

### Step 1: Create GitHub Repository

1. **Go to GitHub:** https://github.com/new
2. **Repository name:** `email-spam-detection`
3. **Description:** AI-powered Email Spam Detection System
4. **Visibility:** Public (or Private)
5. **DON'T** check "Initialize with README"
6. **Click:** "Create repository"

### Step 2: Push to GitHub

**Option A: Using Deployment Script (Easiest)**

Windows:
```bash
deploy.bat
```

macOS/Linux:
```bash
chmod +x deploy.sh
./deploy.sh
```

**Option B: Manual Commands**

```bash
# Initialize Git (if not done)
git init

# Add all files
git add .

# Create commit
git commit -m "Initial commit: Email Spam Detection System"

# Add remote (replace YOUR_USERNAME)
git remote add origin https://github.com/YOUR_USERNAME/email-spam-detection.git

# Push to GitHub
git branch -M main
git push -u origin main
```

### Step 3: Verify Upload

1. Go to your GitHub repository
2. Refresh the page
3. You should see all your files

---

## 🌐 Deploy to Vercel

### Method 1: One-Click Deploy

1. **Go to:** https://vercel.com
2. **Sign in** with GitHub
3. **Click:** "Add New Project"
4. **Select:** `email-spam-detection` repository
5. **Click:** "Deploy"
6. **Wait** 2-3 minutes
7. **Done!** Your app is live at `https://your-project.vercel.app`

### Method 2: Vercel CLI

```bash
# Install Vercel CLI
npm install -g vercel

# Login
vercel login

# Deploy
vercel

# Deploy to production
vercel --prod
```

---

## 🎨 Deploy to Render

### Method 1: Dashboard Deploy

1. **Go to:** https://render.com
2. **Sign in** with GitHub
3. **Click:** "New +" → "Web Service"
4. **Connect:** `email-spam-detection` repository
5. **Configure:**
   - **Name:** email-spam-detection
   - **Build Command:**
     ```
     pip install -r requirements.txt && python -c "import nltk; nltk.download('stopwords'); nltk.download('punkt')" && python src/model_training.py
     ```
   - **Start Command:**
     ```
     gunicorn app:app
     ```
6. **Click:** "Create Web Service"
7. **Wait** 5-10 minutes
8. **Done!** Your app is live at `https://your-app.onrender.com`

### Method 2: Blueprint Deploy

1. **Go to:** https://dashboard.render.com
2. **Click:** "New +" → "Blueprint"
3. **Connect:** your repository
4. Render detects `render.yaml` automatically
5. **Click:** "Apply"

---

## 🔑 Environment Variables

### For Vercel:

1. Go to project settings
2. Click "Environment Variables"
3. Add:
   ```
   FLASK_ENV=production
   SECRET_KEY=<generate-secret-key>
   ```

### For Render:

1. Go to service dashboard
2. Click "Environment"
3. Add:
   ```
   FLASK_ENV=production
   SECRET_KEY=<generate-secret-key>
   PYTHON_VERSION=3.11.7
   ```

### Generate Secret Key:

```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

---

## ✅ Verify Deployment

### Test URLs:

**Home Page:**
```
https://your-app-url.com/
```

**Health Check:**
```
https://your-app-url.com/health
```

**API Test:**
```bash
curl -X POST https://your-app-url.com/predict \
  -H "Content-Type: application/json" \
  -d '{"message": "Congratulations! You won $1000"}'
```

---

## 🔄 Update Deployment

After making changes:

```bash
# Add changes
git add .

# Commit
git commit -m "Update: description of changes"

# Push
git push origin main
```

Both Vercel and Render will automatically redeploy!

---

## 🐛 Troubleshooting

### Issue: Git push rejected

**Solution:**
```bash
git pull origin main --rebase
git push origin main
```

### Issue: Build fails on Vercel

**Solution:**
- Check build logs in Vercel dashboard
- Ensure `vercel.json` is present
- Verify Python version in `runtime.txt`

### Issue: Build fails on Render

**Solution:**
- Check build logs in Render dashboard
- Verify build command is correct
- Ensure all dependencies in `requirements.txt`

### Issue: Application crashes

**Solution:**
- Check application logs
- Verify environment variables
- Ensure model files are generated during build

---

## 📊 Project Files for Deployment

Your project now includes:

✅ `vercel.json` - Vercel configuration
✅ `render.yaml` - Render configuration  
✅ `wsgi.py` - WSGI entry point
✅ `.gitignore` - Git ignore rules
✅ `.gitattributes` - Git attributes
✅ `Procfile` - Process configuration
✅ `runtime.txt` - Python version
✅ `requirements.txt` - Dependencies
✅ `deploy.sh` - Unix deployment script
✅ `deploy.bat` - Windows deployment script

---

## 🎉 Success Checklist

- [ ] Repository created on GitHub
- [ ] Code pushed to GitHub
- [ ] Deployed to Vercel or Render
- [ ] Application accessible via URL
- [ ] Health check endpoint works
- [ ] Spam detection works
- [ ] Environment variables set
- [ ] SSL certificate active

---

## 📞 Need Help?

- **Vercel Docs:** https://vercel.com/docs
- **Render Docs:** https://render.com/docs
- **GitHub Docs:** https://docs.github.com

---

**Your app is ready to deploy!** 🚀

For detailed instructions, see `DEPLOYMENT_GUIDE.md`
