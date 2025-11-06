# 🚀 Quick Setup Guide - Gemini API Integration

## Step 1: Get Your Free Gemini API Key

1. **Visit Google AI Studio**: https://makersuite.google.com/app/apikey
   - Or go to: https://aistudio.google.com/apikey

2. **Sign in** with your Google account

3. **Click "Create API Key"**
   - Choose "Create API key in new project" (recommended)
   - Or select an existing project

4. **Copy the API key** - it will look something like:
   ```
   AIzaSyD-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
   ```

## Step 2: Configure the API Key

### Option A: Create config.json file manually

Create a file named `config.json` in the project directory with:

```json
{
    "gemini_api_key": "YOUR_API_KEY_HERE"
}
```

Replace `YOUR_API_KEY_HERE` with your actual API key.

### Option B: Use in-app configuration

1. Run the game: `python quiz_game.py`
2. Choose option **4. Configure API Key**
3. Paste your API key when prompted
4. The game will automatically create the config.json file

## Step 3: Start Playing!

Run the game and choose option 2 to generate AI-powered quizzes:

```powershell
python quiz_game.py
```

## Example Usage

```
Enter the quiz topic: Python Programming
How many questions do you want? (1-20): 5

🤖 Generating 5 questions about 'Python Programming'...
⏳ Please wait, this may take a few seconds...

✓ Successfully generated 5 questions!
```

## Sample Topics You Can Try

- **Programming**: Python Programming, JavaScript Basics, Data Structures
- **Science**: Biology, Chemistry, Physics, Astronomy
- **History**: World War II, Ancient Rome, American History
- **Mathematics**: Algebra, Calculus, Geometry
- **General Knowledge**: Geography, Literature, Movies
- **Technology**: Artificial Intelligence, Cloud Computing, Cybersecurity

## Important Notes

⚠️ **Security**: Never share your API key publicly or commit config.json to Git
✅ The `.gitignore` file is already configured to exclude config.json
🆓 Gemini API has a generous free tier
📊 Rate limits apply to free tier (check Google AI Studio for details)

## Troubleshooting

### "API key not configured"
- Make sure config.json exists in the project root
- Check that the JSON format is correct
- Verify there are no extra spaces or quotes

### "Failed to generate questions"
- Check your internet connection
- Verify the API key is valid (test it in Google AI Studio)
- You might have hit rate limits - wait a few minutes

### Module not found error
```powershell
pip install google-generativeai
```

## API Usage Limits (Free Tier)

- **Gemini 2.0 Flash**: 15 requests per minute
- Plenty for personal quiz games!
- Check current limits: https://ai.google.dev/pricing

Enjoy creating unlimited quizzes on any topic! 🎉
