# Deployment Guide - Vercel & Render

Complete guide for deploying your Email Spam Detection System to Vercel and Render.

---

## 🚀 Quick Deploy

### Option 1: Deploy to Vercel (Recommended for Frontend)
[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone)

### Option 2: Deploy to Render (Recommended for Full-Stack)
[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy)

---

## 📋 Prerequisites

Before deploying, ensure you have:

- ✅ Git installed
- ✅ GitHub account
- ✅ Vercel account (for Vercel deployment)
- ✅ Render account (for Render deployment)
- ✅ All files committed to Git

---

## 🔧 Step 1: Initialize Git Repository

### 1.1 Initialize Git (if not already done)

```bash
git init
```

### 1.2 Add all files

```bash
git add .
```

### 1.3 Create initial commit

```bash
git commit -m "Initial commit: Email Spam Detection System"
```

### 1.4 Create GitHub repository

1. Go to [GitHub](https://github.com/new)
2. Create a new repository named `email-spam-detection`
3. **Don't** initialize with README (we already have one)
4. Click "Create repository"

### 1.5 Connect to GitHub

```bash
# Replace YOUR_USERNAME with your GitHub username
git remote add origin https://github.com/YOUR_USERNAME/email-spam-detection.git
git branch -M main
git push -u origin main
```

---

## 🌐 Step 2: Deploy to Vercel

### Method 1: Deploy via Vercel Dashboard (Easiest)

1. **Go to [Vercel](https://vercel.com)**
2. **Sign in** with GitHub
3. **Click "Add New Project"**
4. **Import your GitHub repository**
   - Select `email-spam-detection`
5. **Configure Project:**
   - Framework Preset: `Other`
   - Build Command: Leave default
   - Output Directory: Leave default
6. **Environment Variables** (Optional):
   ```
   FLASK_ENV=production
   PYTHON_VERSION=3.11
   ```
7. **Click "Deploy"**
8. **Wait 2-5 minutes** for deployment
9. **Access your app** at: `https://your-project.vercel.app`

### Method 2: Deploy via Vercel CLI

```bash
# Install Vercel CLI
npm install -g vercel

# Login to Vercel
vercel login

# Deploy
vercel

# Follow the prompts:
# - Set up and deploy? Yes
# - Which scope? Your account
# - Link to existing project? No
# - Project name? email-spam-detection
# - Directory? ./
# - Override settings? No

# Deploy to production
vercel --prod
```

### Vercel Configuration

The `vercel.json` file is already configured:

```json
{
  "version": 2,
  "builds": [
    {
      "src": "app.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "app.py"
    }
  ]
}
```

---

## 🎨 Step 3: Deploy to Render

### Method 1: Deploy via Render Dashboard (Recommended)

1. **Go to [Render](https://render.com)**
2. **Sign in** with GitHub
3. **Click "New +"** → **"Web Service"**
4. **Connect GitHub repository**
   - Select `email-spam-detection`
5. **Configure Service:**

   **Basic Settings:**
   - Name: `email-spam-detection`
   - Region: Choose closest to you
   - Branch: `main`
   - Runtime: `Python 3`

   **Build & Deploy:**
   - Build Command:
     ```bash
     pip install -r requirements.txt && python -c "import nltk; nltk.download('stopwords'); nltk.download('punkt')" && python src/model_training.py
     ```
   - Start Command:
     ```bash
     gunicorn app:app
     ```

   **Environment Variables:**
   ```
   PYTHON_VERSION=3.11.7
   FLASK_ENV=production
   ```

   **Plan:**
   - Select `Free` plan

6. **Click "Create Web Service"**
7. **Wait 5-10 minutes** for build and deployment
8. **Access your app** at: `https://your-app.onrender.com`

### Method 2: Deploy via render.yaml (Infrastructure as Code)

The `render.yaml` file is already configured. Render will automatically detect it.

1. Go to [Render Dashboard](https://dashboard.render.com)
2. Click "New +" → "Blueprint"
3. Connect your repository
4. Render will detect `render.yaml` and configure automatically
5. Click "Apply"

---

## 🔐 Step 4: Environment Variables

### For Vercel:

1. Go to your project dashboard
2. Click "Settings" → "Environment Variables"
3. Add:
   ```
   FLASK_ENV=production
   SECRET_KEY=your-secret-key-here
   ```

### For Render:

1. Go to your web service dashboard
2. Click "Environment"
3. Add:
   ```
   FLASK_ENV=production
   SECRET_KEY=your-secret-key-here
   PYTHON_VERSION=3.11.7
   ```

### Generate Secret Key:

```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

---

## 📊 Step 5: Verify Deployment

### Check Deployment Status

**Vercel:**
- Dashboard: https://vercel.com/dashboard
- Logs: Click on your project → "Deployments" → Select deployment → "View Logs"

**Render:**
- Dashboard: https://dashboard.render.com
- Logs: Click on your service → "Logs" tab

### Test Your Application

1. **Home Page:**
   ```
   https://your-app-url.com/
   ```

2. **Health Check:**
   ```
   https://your-app-url.com/health
   ```

3. **API Test:**
   ```bash
   curl -X POST https://your-app-url.com/predict \
     -H "Content-Type: application/json" \
     -d '{"message": "Congratulations! You won $1000"}'
   ```

---

## 🔄 Step 6: Continuous Deployment

Both Vercel and Render support automatic deployments:

### Enable Auto-Deploy:

1. **Push changes to GitHub:**
   ```bash
   git add .
   git commit -m "Update feature"
   git push origin main
   ```

2. **Automatic deployment** will trigger on both platforms

3. **Monitor deployment** in respective dashboards

---

## 🐛 Troubleshooting

### Common Issues

#### 1. Build Fails on Vercel

**Problem:** Python version mismatch

**Solution:**
- Ensure `runtime.txt` has: `python-3.11.7`
- Check Vercel build logs

#### 2. Build Fails on Render

**Problem:** Dependencies installation fails

**Solution:**
```bash
# Update requirements.txt with compatible versions
pip freeze > requirements.txt
git add requirements.txt
git commit -m "Update dependencies"
git push
```

#### 3. Model Not Found Error

**Problem:** Model files not generated during build

**Solution:**
- Ensure build command includes: `python src/model_training.py`
- Check if NLTK data is downloaded in build command

#### 4. Application Crashes on Startup

**Problem:** Port configuration

**Solution:**
- Ensure `app.py` uses: `port = int(os.environ.get('PORT', 5000))`
- Check environment variables

#### 5. Static Files Not Loading

**Problem:** Static file paths incorrect

**Solution:**
- Ensure paths in templates use: `{{ url_for('static', filename='css/style.css') }}`
- Check static folder structure

---

## 📈 Performance Optimization

### For Vercel:

1. **Enable Caching:**
   - Vercel automatically caches static assets
   - Model files are cached between builds

2. **Optimize Build Time:**
   - Use `vercel.json` to configure build settings
   - Cache Python dependencies

### For Render:

1. **Use Persistent Disk (Paid plans):**
   - Store model files on persistent disk
   - Faster subsequent deployments

2. **Optimize Build:**
   - Use Docker for faster builds (optional)
   - Cache dependencies

---

## 🔒 Security Best Practices

### 1. Environment Variables

Never commit sensitive data:
```bash
# Use .env file locally (already in .gitignore)
FLASK_ENV=production
SECRET_KEY=your-secret-key
```

### 2. HTTPS

Both Vercel and Render provide free SSL certificates automatically.

### 3. Rate Limiting

Add rate limiting to prevent abuse:
```python
from flask_limiter import Limiter

limiter = Limiter(app, key_func=lambda: request.remote_addr)

@app.route('/predict', methods=['POST'])
@limiter.limit("10 per minute")
def predict():
    # Your code
```

---

## 📊 Monitoring

### Vercel Analytics

1. Go to project dashboard
2. Click "Analytics"
3. View:
   - Page views
   - Response times
   - Error rates

### Render Metrics

1. Go to service dashboard
2. Click "Metrics"
3. View:
   - CPU usage
   - Memory usage
   - Request count
   - Response times

---

## 💰 Cost Comparison

### Vercel Free Tier:
- ✅ 100 GB bandwidth/month
- ✅ Unlimited deployments
- ✅ Automatic HTTPS
- ✅ Global CDN
- ⚠️ Serverless functions (may have cold starts)

### Render Free Tier:
- ✅ 750 hours/month
- ✅ Automatic HTTPS
- ✅ Persistent service
- ⚠️ Sleeps after 15 min inactivity
- ⚠️ 512 MB RAM

### Recommendation:
- **Vercel:** Best for static sites and serverless
- **Render:** Best for full-stack apps with persistent processes

---

## 🎯 Custom Domain

### Vercel:

1. Go to project settings
2. Click "Domains"
3. Add your domain
4. Update DNS records:
   ```
   Type: CNAME
   Name: www
   Value: cname.vercel-dns.com
   ```

### Render:

1. Go to service settings
2. Click "Custom Domains"
3. Add your domain
4. Update DNS records:
   ```
   Type: CNAME
   Name: www
   Value: your-app.onrender.com
   ```

---

## 📝 Deployment Checklist

Before deploying:

- [ ] All files committed to Git
- [ ] Repository pushed to GitHub
- [ ] `requirements.txt` updated
- [ ] `vercel.json` configured (for Vercel)
- [ ] `render.yaml` configured (for Render)
- [ ] Environment variables set
- [ ] Secret key generated
- [ ] `.gitignore` includes sensitive files
- [ ] Model training works locally
- [ ] Application runs locally
- [ ] All tests pass

After deploying:

- [ ] Application accessible via URL
- [ ] Health check endpoint works
- [ ] Spam detection works
- [ ] Static files load correctly
- [ ] No errors in logs
- [ ] SSL certificate active
- [ ] Custom domain configured (optional)

---

## 🆘 Support

### Vercel Support:
- Documentation: https://vercel.com/docs
- Community: https://github.com/vercel/vercel/discussions
- Support: support@vercel.com

### Render Support:
- Documentation: https://render.com/docs
- Community: https://community.render.com
- Support: support@render.com

---

## 🎉 Success!

Your Email Spam Detection System is now deployed and accessible worldwide!

**Next Steps:**
1. Share your deployment URL
2. Monitor application performance
3. Collect user feedback
4. Iterate and improve

---

**Deployment URLs:**
- Vercel: `https://your-project.vercel.app`
- Render: `https://your-app.onrender.com`

**Happy Deploying!** 🚀
