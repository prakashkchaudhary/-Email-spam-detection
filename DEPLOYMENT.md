# Deployment Guide - Email Spam Detection System

Complete guide for deploying the Email Spam Detection application to various cloud platforms.

## Table of Contents

1. [Pre-Deployment Checklist](#pre-deployment-checklist)
2. [Deploy to Render](#deploy-to-render)
3. [Deploy to Railway](#deploy-to-railway)
4. [Deploy to Heroku](#deploy-to-heroku)
5. [Environment Variables](#environment-variables)
6. [Post-Deployment](#post-deployment)

---

## Pre-Deployment Checklist

Before deploying, ensure you have:

- ✅ Trained model files in `models/` directory
- ✅ All dependencies listed in `requirements.txt`
- ✅ `Procfile` configured correctly
- ✅ `runtime.txt` specifying Python version
- ✅ Git repository initialized
- ✅ `.gitignore` file configured

### Prepare for Deployment

1. **Train the model locally:**
```bash
python src/model_training.py
```

2. **Test locally:**
```bash
python app.py
```
Visit `http://localhost:5000` to verify everything works.

3. **Commit all changes:**
```bash
git add .
git commit -m "Prepare for deployment"
```

---

## Deploy to Render

[Render](https://render.com) offers free hosting for web applications.

### Step 1: Create Render Account

1. Go to [render.com](https://render.com)
2. Sign up with GitHub account
3. Authorize Render to access your repositories

### Step 2: Create New Web Service

1. Click **"New +"** → **"Web Service"**
2. Connect your GitHub repository
3. Configure the service:

**Settings:**
- **Name:** `email-spam-detection`
- **Environment:** `Python 3`
- **Region:** Choose closest to your users
- **Branch:** `main` or `master`
- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `gunicorn app:app`

### Step 3: Environment Variables

Add these environment variables in Render dashboard:

```
PYTHON_VERSION=3.11.7
PORT=10000
FLASK_ENV=production
```

### Step 4: Deploy

1. Click **"Create Web Service"**
2. Wait for build to complete (5-10 minutes)
3. Access your app at: `https://your-app-name.onrender.com`

### Render Configuration File (Optional)

Create `render.yaml`:

```yaml
services:
  - type: web
    name: email-spam-detection
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: gunicorn app:app
    envVars:
      - key: PYTHON_VERSION
        value: 3.11.7
      - key: FLASK_ENV
        value: production
```

---

## Deploy to Railway

[Railway](https://railway.app) provides simple deployment with automatic builds.

### Step 1: Create Railway Account

1. Go to [railway.app](https://railway.app)
2. Sign up with GitHub
3. Authorize Railway

### Step 2: Deploy from GitHub

1. Click **"New Project"**
2. Select **"Deploy from GitHub repo"**
3. Choose your repository
4. Railway auto-detects Python and deploys

### Step 3: Configure

Railway automatically:
- Installs dependencies from `requirements.txt`
- Runs the app using `Procfile`
- Assigns a public URL

### Step 4: Environment Variables

In Railway dashboard, add:

```
PYTHON_VERSION=3.11.7
FLASK_ENV=production
```

### Step 5: Access Application

1. Go to **"Settings"** → **"Domains"**
2. Click **"Generate Domain"**
3. Access your app at: `https://your-app.up.railway.app`

---

## Deploy to Heroku

[Heroku](https://heroku.com) is a popular platform-as-a-service.

### Step 1: Install Heroku CLI

**Windows:**
Download from [heroku.com/downloads](https://devcenter.heroku.com/articles/heroku-cli)

**macOS:**
```bash
brew tap heroku/brew && brew install heroku
```

**Linux:**
```bash
curl https://cli-assets.heroku.com/install.sh | sh
```

### Step 2: Login to Heroku

```bash
heroku login
```

### Step 3: Create Heroku App

```bash
heroku create your-app-name
```

Or let Heroku generate a name:
```bash
heroku create
```

### Step 4: Add Python Buildpack

```bash
heroku buildpacks:set heroku/python
```

### Step 5: Set Environment Variables

```bash
heroku config:set FLASK_ENV=production
heroku config:set PYTHON_VERSION=3.11.7
```

### Step 6: Deploy

```bash
git push heroku main
```

Or if your branch is `master`:
```bash
git push heroku master
```

### Step 7: Scale Dynos

```bash
heroku ps:scale web=1
```

### Step 8: Open Application

```bash
heroku open
```

### Heroku Logs

View logs:
```bash
heroku logs --tail
```

---

## Environment Variables

### Required Variables

| Variable | Value | Description |
|----------|-------|-------------|
| `FLASK_ENV` | `production` | Flask environment |
| `PYTHON_VERSION` | `3.11.7` | Python version |
| `PORT` | Auto-assigned | Server port |

### Optional Variables

| Variable | Value | Description |
|----------|-------|-------------|
| `SECRET_KEY` | Random string | Flask secret key |
| `MAX_CONTENT_LENGTH` | `16777216` | Max upload size (16MB) |
| `DEBUG` | `False` | Debug mode |

### Setting Environment Variables

**Render:**
Dashboard → Environment → Add Environment Variable

**Railway:**
Dashboard → Variables → New Variable

**Heroku:**
```bash
heroku config:set VARIABLE_NAME=value
```

---

## Post-Deployment

### 1. Verify Deployment

Check these endpoints:

- **Home:** `https://your-app.com/`
- **Detection:** `https://your-app.com/detect`
- **About:** `https://your-app.com/about`
- **Health:** `https://your-app.com/health`

### 2. Test API

```bash
curl -X POST https://your-app.com/predict \
  -H "Content-Type: application/json" \
  -d '{"message": "Congratulations! You won $1000"}'
```

### 3. Monitor Performance

**Render:**
- Dashboard → Metrics
- View CPU, Memory, Response times

**Railway:**
- Dashboard → Metrics
- Monitor deployments and logs

**Heroku:**
```bash
heroku logs --tail
heroku ps
```

### 4. Set Up Custom Domain (Optional)

**Render:**
1. Dashboard → Settings → Custom Domains
2. Add your domain
3. Configure DNS records

**Railway:**
1. Dashboard → Settings → Domains
2. Add custom domain
3. Update DNS

**Heroku:**
```bash
heroku domains:add www.yourdomain.com
```

### 5. Enable HTTPS

All platforms provide free SSL certificates automatically.

---

## Troubleshooting

### Common Issues

#### 1. Application Crashes on Startup

**Check logs:**
```bash
# Render: Dashboard → Logs
# Railway: Dashboard → Deployments → View Logs
# Heroku:
heroku logs --tail
```

**Common causes:**
- Missing dependencies
- Model files not found
- Port configuration issues

**Solution:**
```bash
# Ensure model is trained
python src/model_training.py

# Commit model files
git add models/
git commit -m "Add trained model"
git push
```

#### 2. Module Not Found Error

**Solution:**
Ensure all dependencies are in `requirements.txt`:
```bash
pip freeze > requirements.txt
git add requirements.txt
git commit -m "Update dependencies"
git push
```

#### 3. Port Binding Error

**Solution:**
Ensure `app.py` uses environment PORT:
```python
port = int(os.environ.get('PORT', 5000))
app.run(host='0.0.0.0', port=port)
```

#### 4. Timeout During Build

**Solution:**
- Reduce model size
- Use lighter dependencies
- Increase build timeout in platform settings

#### 5. Out of Memory

**Solution:**
- Upgrade to paid tier
- Optimize model size
- Reduce max_features in TF-IDF

---

## Performance Optimization

### 1. Enable Caching

Add caching to Flask:
```python
from flask_caching import Cache

cache = Cache(app, config={'CACHE_TYPE': 'simple'})

@cache.cached(timeout=300)
def expensive_function():
    pass
```

### 2. Use CDN for Static Files

Host CSS/JS on CDN for faster loading.

### 3. Compress Responses

```python
from flask_compress import Compress

Compress(app)
```

### 4. Database Connection Pooling

If using database, implement connection pooling.

---

## Scaling

### Horizontal Scaling

**Render:**
- Dashboard → Settings → Instance Count

**Railway:**
- Automatically scales based on traffic

**Heroku:**
```bash
heroku ps:scale web=2
```

### Vertical Scaling

Upgrade to higher tier plans for more resources.

---

## Continuous Deployment

### Automatic Deployment

All platforms support automatic deployment from GitHub:

1. Push to main/master branch
2. Platform detects changes
3. Automatically builds and deploys

### Deployment Workflow

```bash
# Make changes
git add .
git commit -m "Update feature"
git push origin main

# Platform automatically deploys
```

---

## Security Best Practices

1. **Use Environment Variables** for sensitive data
2. **Enable HTTPS** (automatic on all platforms)
3. **Set SECRET_KEY** for Flask sessions
4. **Limit Request Size** to prevent abuse
5. **Rate Limiting** to prevent spam
6. **Input Validation** on all endpoints
7. **Regular Updates** of dependencies

---

## Cost Considerations

### Free Tiers

**Render:**
- 750 hours/month free
- Sleeps after 15 min inactivity
- 512 MB RAM

**Railway:**
- $5 free credit/month
- Pay for usage beyond credit

**Heroku:**
- 550-1000 dyno hours/month free
- Sleeps after 30 min inactivity

### Paid Plans

Upgrade for:
- No sleep mode
- More resources
- Custom domains
- Better support

---

## Monitoring & Logging

### Application Monitoring

**Recommended Tools:**
- Sentry (error tracking)
- New Relic (performance)
- Datadog (infrastructure)

### Log Management

**Render/Railway:**
Built-in log viewer in dashboard

**Heroku:**
```bash
heroku logs --tail
heroku logs --source app
```

---

## Backup & Recovery

### Database Backups

If using database:
```bash
# Heroku Postgres
heroku pg:backups:capture
heroku pg:backups:download
```

### Model Versioning

Keep model versions in Git or cloud storage.

---

## Support & Resources

### Platform Documentation

- **Render:** [render.com/docs](https://render.com/docs)
- **Railway:** [docs.railway.app](https://docs.railway.app)
- **Heroku:** [devcenter.heroku.com](https://devcenter.heroku.com)

### Community

- Stack Overflow
- Platform-specific Discord/Slack
- GitHub Issues

---

## Conclusion

Your Email Spam Detection application is now deployed and accessible worldwide! 🎉

For issues or questions:
- Check platform logs
- Review documentation
- Contact support

**Happy Deploying!**
