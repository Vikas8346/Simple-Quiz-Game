# Vercel Deployment Guide

## Deploy to Vercel

1. **Install Vercel CLI** (if not already installed):
```bash
npm install -g vercel
```

2. **Login to Vercel**:
```bash
vercel login
```

3. **Deploy the project**:
```bash
vercel
```

4. **Set Environment Variables** (during deployment or in Vercel dashboard):
   - `GEMINI_API_KEY`: Your Google Gemini API key
   - `SECRET_KEY`: A random secret key for Flask sessions

5. **For production deployment**:
```bash
vercel --prod
```

## Environment Variables

Go to your Vercel project dashboard:
1. Click on "Settings"
2. Go to "Environment Variables"
3. Add these variables:
   - `GEMINI_API_KEY` = Your Gemini API key
   - `SECRET_KEY` = Any random string for session security

## Alternative: Deploy via Vercel Website

1. Go to https://vercel.com
2. Click "Add New" > "Project"
3. Import your GitHub repository
4. Vercel will auto-detect the configuration
5. Add environment variables in the deployment settings
6. Click "Deploy"

## Post-Deployment

Your quiz game will be available at: `https://your-project-name.vercel.app`

The API key will be read from environment variables, so your actual key remains secure.
