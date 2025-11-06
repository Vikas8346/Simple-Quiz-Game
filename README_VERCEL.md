# Deploy Quiz Game to Vercel

## Quick Deploy Steps

### 1. Install Vercel CLI
```bash
npm install -g vercel
```

### 2. Login to Vercel
```bash
vercel login
```

### 3. Deploy
```bash
vercel --prod
```

## Environment Variables (Optional - for AI features)

In Vercel Dashboard, add:
- `GEMINI_API_KEY`: Your Google Gemini API key
- `SECRET_KEY`: A random secret key for Flask sessions

## Files Added for Vercel

- `vercel.json` - Vercel configuration
- `api/index.py` - Serverless function entry point
- `.vercelignore` - Files to exclude from deployment

## How It Works

- Vercel treats `api/index.py` as a serverless function
- All routes are handled by Flask
- Templates are served from the `templates/` directory
- High scores are stored in `/tmp` (temporary storage on Vercel)

## Post-Deployment

After deployment, you'll get a URL like:
`https://your-project-name.vercel.app`

Visit that URL to play the quiz game!

## Note on High Scores

High scores on Vercel are stored in temporary storage and will be reset periodically. For persistent storage, consider using:
- Vercel KV
- MongoDB Atlas
- PostgreSQL
- Any cloud database service
