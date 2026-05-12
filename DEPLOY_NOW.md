# 🚀 Deploy Your App NOW!

Quick 3-step deployment guide.

---

## ⚡ Quick Deploy (Choose One)

### Option 1: Deploy to Vercel (2 minutes)

1. **Run deployment script:**
   ```bash
   # Windows
   deploy.bat
   
   # macOS/Linux
   chmod +x deploy.sh
   ./deploy.sh
   ```

2. **Follow prompts** to push to GitHub

3. **Go to [Vercel](https://vercel.com)**
   - Sign in with GitHub
   - Click "Add New Project"
   - Select `email-spam-detection`
   - Click "Deploy"

4. **Done!** Your app is live at `https://your-project.vercel.app`

---

### Option 2: Deploy to Render (5 minutes)

1. **Run deployment script:**
   ```bash
   # Windows
   deploy.bat
   
   # macOS/Linux
   chmod +x deploy.sh
   ./deploy.sh
   ```

2. **Follow prompts** to push to GitHub

3. **Go to [Render](https://render.com)**
   - Sign in with GitHub
   - Click "New +" → "Web Service"
   - Select `email-spam-detection`
   - **Build Command:**
     ```
     pip install -r requirements.txt && python -c "import nltk; nltk.download('stopwords'); nltk.download('punkt')" && python src/model_training.py
     ```
   - **Start Command:**
     ```
     gunicorn app:app
     ```
   - Click "Create Web Service"

4. **Done!** Your app is live at `https://your-app.onrender.com`

---

## 📋 Manual Deployment (If scripts don't work)

### Step 1: Push to GitHub

```bash
# Initialize Git
git init

# Add files
git add .

# Commit
git commit -m "Initial commit"

# Create repository on GitHub: https://github.com/new
# Then add remote (replace YOUR_USERNAME):
git remote add origin https://github.com/YOUR_USERNAME/email-spam-detection.git

# Push
git branch -M main
git push -u origin main
```

### Step 2: Deploy to Vercel

1. Go to https://vercel.com
2. Sign in with GitHub
3. Click "Add New Project"
4. Import `email-spam-detection`
5. Click "Deploy"

### Step 3: Deploy to Render

1. Go to https://render.com
2. Sign in with GitHub
3. Click "New +" → "Web Service"
4. Connect `email-spam-detection`
5. Use configuration from `render.yaml`
6. Click "Create Web Service"

---

## ✅ Verify Deployment

Test your deployed app:

```bash
# Replace with your actual URL
curl https://your-app-url.com/health
```

---

## 🎉 Success!

Your Email Spam Detection System is now live and accessible worldwide!

**Share your deployment URL:**
- Vercel: `https://your-project.vercel.app`
- Render: `https://your-app.onrender.com`

---

## 📚 Need More Help?

- **Detailed Guide:** See `DEPLOYMENT_GUIDE.md`
- **GitHub Setup:** See `GITHUB_SETUP.md`
- **Troubleshooting:** See `DEPLOYMENT_GUIDE.md` → Troubleshooting section

---

**Happy Deploying!** 🚀
