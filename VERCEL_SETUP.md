# Fix Vercel "AI features not configured" Error

## Problem
Your Vercel app at https://simple-quiz-game-ten.vercel.app/ shows "Error: AI features not configured" because it needs the Gemini API key.

## Solution - Add Environment Variable in Vercel

### Step-by-Step Instructions:

1. **Go to your Vercel dashboard**
   - Visit: https://vercel.com/dashboard
   - Find your project: `simple-quiz-game-ten`

2. **Open Project Settings**
   - Click on your project name
   - Click "Settings" tab at the top

3. **Add Environment Variable**
   - In the left sidebar, click "Environment Variables"
   - Click "Add New" or the input field
   - Enter:
     - **Key**: `GEMINI_API_KEY`
     - **Value**: `AIzaSyDJsO9hcG8oWYr1YnfPhLW-DBZyt6-Hke4`
     - **Environment**: Check all boxes (Production, Preview, Development)
   - Click "Save"

4. **Redeploy**
   - Go to "Deployments" tab
   - Click the three dots (...) next to the latest deployment
   - Click "Redeploy"
   - OR just wait - Vercel will auto-deploy since we just pushed new code to GitHub

5. **Verify**
   - Wait 1-2 minutes for deployment to complete
   - Visit: https://simple-quiz-game-ten.vercel.app/
   - The AI Custom Quiz feature should now work!

## Alternative: Quick Redeploy from Command Line

If you have Vercel CLI installed:

```bash
# Login to Vercel
vercel login

# Link this project
cd /workspaces/Simple-Quiz-Game
vercel link

# Add environment variable
vercel env add GEMINI_API_KEY

# Paste your API key when prompted: AIzaSyDJsO9hcG8oWYr1YnfPhLW-DBZyt6-Hke4

# Redeploy
vercel --prod
```

## What Changed

The app now reads the API key from:
1. **Environment variable** `GEMINI_API_KEY` (for Vercel/production) ✅
2. **config.json file** (for local development) ✅

This means:
- Vercel deployment works when you set the environment variable
- Local development still works with your config.json file
- Your API key is secure (not committed to GitHub)

## Expected Result

After adding the environment variable and redeploying:
- ✅ Default Quiz works
- ✅ AI-Powered Custom Quiz works (can generate questions on any topic)
- ✅ High Scores work
- ✅ No "AI features not configured" error

---

**Your Vercel App**: https://simple-quiz-game-ten.vercel.app/
**GitHub Repo**: https://github.com/Vikas8346/Simple-Quiz-Game
