# How to Run the Quiz Game

## Prerequisites
- Python 3.6 or higher installed on your system
- Internet connection (for AI-generated questions)
- Google Gemini API key (free - for AI features)

## Installation

### Step 1: Install Dependencies
Open a terminal in the project directory and run:
```powershell
pip install -r requirements.txt
```

This will install the Google Generative AI library.

### Step 2: Configure Gemini API (Optional - for AI features)

1. Get your free API key:
   - Visit: https://makersuite.google.com/app/apikey
   - Sign in with your Google account
   - Click "Create API Key"
   - Copy the generated API key

2. Create a `config.json` file in the project directory:
   ```json
   {
       "gemini_api_key": "YOUR_API_KEY_HERE"
   }
   ```
   
   Or use the in-app configuration option (Menu Option 4)

**Note**: The game will work without API key, but AI question generation will be disabled.

## Running the Game

### Option 1: Using Command Line
1. Open a terminal/command prompt
2. Navigate to the project directory:
   ```
   cd c:\Users\PRINCE\Documents\GitHub\Simple-Quiz-Game
   ```
3. Run the game:
   ```
   python quiz_game.py
   ```

### Option 2: Using VS Code
1. Open the project folder in VS Code
2. Open `quiz_game.py`
3. Press F5 or click "Run" to start the game

## How to Play

### Menu Options:
1. **Play Quiz (Default Questions)** - Play with 10 built-in questions
2. **Play Custom Quiz (AI-Generated)** 🤖 - Generate questions on any topic
3. **View High Scores** - See the leaderboard
4. **Configure API Key** - Set up your Gemini API key
5. **Exit** - Close the game

### Playing Default Quiz:
1. Choose option 1 from the main menu
2. Enter your name
3. Answer each question by typing A, B, C, or D
4. View your score and feedback

### Playing Custom AI Quiz:
1. Choose option 2 from the main menu
2. Enter the topic you want to be quizzed on (e.g., "Python Programming", "World History", "Biology")
3. Specify how many questions you want (1-20)
4. Wait for AI to generate questions
5. Answer the questions and view your score

## Features
- **Default Questions**: 10 built-in general knowledge questions
- **AI-Generated Questions**: Create unlimited quizzes on any topic using Gemini 2.0 Flash
- **Randomized Questions**: Questions appear in a different order each time
- **High Score Tracking**: Your scores are automatically saved to `high_scores.json`
- **Leaderboard**: View the top 10 high scores
- **Performance Feedback**: Get encouraging feedback based on your score
- **Customizable Topics**: Ask questions about anything you want to learn

## Files in the Project
- `quiz_game.py` - Main game file
- `requirements.txt` - Python dependencies
- `config.json` - API key configuration (you create this)
- `config.json.example` - Example configuration file
- `high_scores.json` - Automatically created when you first play (stores high scores)
- `.gitignore` - Git ignore file (keeps API keys safe)

## Troubleshooting

### "ModuleNotFoundError: No module named 'google.generativeai'"
Run: `pip install -r requirements.txt`

### "API key not configured"
1. Make sure you created `config.json` in the project directory
2. Verify your API key is correct
3. Check that the file format matches the example

### "Failed to generate questions"
1. Check your internet connection
2. Verify your API key is valid
3. Make sure you haven't exceeded API rate limits

Enjoy the game! 🎮
