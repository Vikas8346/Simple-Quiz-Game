# Quiz Game with High Score Tracking

A Python-based quiz game powered by **Google Gemini 2.0 Flash** AI that demonstrates basic Python programming concepts including file handling, randomization, API integration, and data persistence.

## 🎮 Project Overview

This is a mini project demonstrating **Basics of Python Programming** through an interactive quiz game. The game features **AI-powered question generation** using Google's Gemini 2.0 Flash model, allowing you to create unlimited quizzes on any topic, plus persistent high score tracking using JSON file storage.

## ✨ Features

- **AI-Powered Question Generation** 🤖: Create unlimited quizzes on ANY topic using Google Gemini 2.0 Flash
- **Custom Topics**: Ask questions about Python, History, Science, Math, or anything else
- **Flexible Question Count**: Choose from 1 to 20 questions per quiz
- **10 Default Questions**: Built-in questions covering general knowledge
- **Randomized Questions**: Questions appear in different orders each time you play
- **High Score System**: Automatically saves and tracks player scores
- **Leaderboard**: Displays top 10 high scores with player names and timestamps
- **User-Friendly Interface**: Clean console-based UI with clear instructions
- **Performance Feedback**: Encouraging messages based on your quiz performance
- **Easy API Configuration**: Set up Gemini API directly from the app

## 🛠️ Python Concepts Demonstrated

This project showcases the following Python programming fundamentals:

1. **Object-Oriented Programming (OOP)**
   - Classes and methods
   - Instance variables
   - Encapsulation

2. **File Handling**
   - Reading from JSON files
   - Writing to JSON files
   - File existence checking
   - Error handling for file operations

3. **Data Structures**
   - Lists and dictionaries
   - Nested data structures
   - List comprehensions

4. **Control Flow**
   - While loops
   - For loops
   - If-elif-else statements
   - Input validation

5. **Built-in Modules**
   - `json` - JSON data handling
   - `random` - Question randomization
   - `os` - File system operations
   - `datetime` - Timestamp creation

6. **External Libraries**
   - `google.generativeai` - Gemini API integration for AI question generation

7. **String Formatting**
   - f-strings
   - String methods (strip, upper, center)

8. **API Integration**
   - REST API calls
   - JSON parsing
   - Error handling for network operations

## 📁 Project Structure

```
Simple-Quiz-Game/
│
├── quiz_game.py          # Main game file
├── requirements.txt      # Python dependencies
├── config.json           # API key configuration (you create this)
├── config.json.example   # Example config file
├── high_scores.json      # High scores data (auto-generated)
├── .gitignore           # Git ignore file
├── SETUP_GUIDE.md       # Detailed Gemini API setup guide
├── how_to_run.md        # Detailed running instructions
└── README.md            # This file
```

## 🚀 How to Run

### Prerequisites
- Python 3.6 or higher
- Internet connection (for AI features)
- Google Gemini API key (free)

### Quick Start
1. Clone or download this repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Get your free Gemini API key from: https://makersuite.google.com/app/apikey
4. Create `config.json`:
   ```json
   {
       "gemini_api_key": "YOUR_API_KEY_HERE"
   }
   ```
5. Run the game:
   ```bash
   python quiz_game.py
   ```

📖 **Detailed Guides**:
- [SETUP_GUIDE.md](SETUP_GUIDE.md) - Complete Gemini API setup instructions
- [QUICK_START.md](QUICK_START.md) - Quick reference and tips
- [how_to_run.md](how_to_run.md) - Detailed running instructions
- [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md) - Full feature overview

## 🎯 How to Play

1. **Start the Game**: Run `quiz_game.py`
2. **Main Menu**: Choose from:
   - **Option 1**: Play Quiz (Default Questions) - 10 built-in questions
   - **Option 2**: Play Custom Quiz (AI-Generated) 🤖 - Create your own topic
   - **Option 3**: View High Scores - See the leaderboard
   - **Option 4**: Configure API Key - Set up Gemini API
   - **Option 5**: Exit - Close the game
3. **For Custom Quiz**:
   - Enter any topic (e.g., "Python Programming", "World War II", "Biology")
   - Choose number of questions (1-20)
   - Wait for AI to generate questions
4. **Answer Questions**: Type A, B, C, or D for each question
5. **View Results**: See your score and performance feedback
6. **Check Leaderboard**: View the top scores

## 📊 Sample Output

### Main Menu
```
==================================================
                 QUIZ GAME MENU
==================================================

1. Play Quiz (Default Questions)
2. Play Custom Quiz (AI-Generated) 🤖
3. View High Scores
4. Configure API Key
5. Exit
```

### AI Custom Quiz
```
==================================================
            AI-POWERED CUSTOM QUIZ
==================================================

Enter the quiz topic: Python Programming
How many questions do you want? (1-20): 5

🤖 Generating 5 questions about 'Python Programming'...
⏳ Please wait, this may take a few seconds...

✓ Successfully generated 5 questions!

==================================================
        WELCOME TO THE QUIZ GAME!
==================================================

Enter your name: John

Question 1/5:
What is the correct way to create a list in Python?
A) list = []
B) list = ()
C) list = {}
D) list = <>

Your answer (A/B/C/D): A
✓ Correct!
```

## 🏆 High Score System

- Scores are automatically saved after each game
- Stored in `high_scores.json` file
- Includes player name, score, and timestamp
- Leaderboard shows top 10 scores

## 🔧 Customization

You can easily customize the game by:

1. **Use Different AI Model**: Change `gemini-2.0-flash-exp` to other Gemini models
2. **Adding More Default Questions**: Edit the `load_questions()` method in `quiz_game.py`
3. **Adjust Question Limit**: Modify the range in `play_custom_quiz()` (currently 1-20)
4. **Customize AI Prompts**: Edit the prompt in `generate_ai_questions()` for different question styles
5. **Adjusting Feedback Messages**: Edit the performance feedback section
6. **Modifying Leaderboard Size**: Change the slice value in `display_high_scores()`

## 📚 Learning Outcomes

By studying this project, you will learn:

- How to structure a Python program using classes
- How to integrate external APIs (Google Gemini)
- How to handle user input with validation
- How to work with JSON files for data persistence
- How to randomize data using the `random` module
- How to format output for better user experience
- Error handling best practices for both file operations and API calls
- Working with dates and timestamps
- API key management and security
- Parsing and validating AI-generated responses

## 🤝 Contributing

Feel free to fork this project and add your own features! Some ideas:
- Add difficulty level selection for AI questions
- Include timed questions with countdown
- Save quiz history and analytics
- Implement a GUI using tkinter or PyQt
- Add sound effects and animations
- Create a multiplayer mode
- Support for different languages
- Export questions to PDF or text files
- Add image-based questions using Gemini Vision

## 📝 License

This project is open source and available for educational purposes.

## 👨‍💻 Author

Created as a mini project to demonstrate basics of Python programming.

---

**Happy Quizzing! 🎉**