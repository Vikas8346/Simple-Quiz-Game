# Quiz Game - Quick Reference

## 🎮 Menu Options

### 1. Play Quiz (Default Questions)
- 10 built-in general knowledge questions
- Questions are randomized each time
- Perfect for quick play without API setup

### 2. Play Custom Quiz (AI-Generated) 🤖
**Requirements**: Gemini API key configured

**Steps**:
1. Enter your topic (anything you want!)
2. Choose number of questions (1-20)
3. Wait for AI to generate questions
4. Play and enjoy!

**Topic Ideas**:
```
✅ Python Programming
✅ Machine Learning Basics
✅ Web Development
✅ World History
✅ Biology
✅ Mathematics
✅ Movies & Entertainment
✅ Sports
✅ Space & Astronomy
✅ Current Events
```

### 3. View High Scores
- See top 10 scores
- Shows player name, score, and date/time
- Tracks both default and AI-generated quiz scores

### 4. Configure API Key
- Set up your Gemini API key
- Creates config.json automatically
- Test connection immediately

### 5. Exit
- Safely close the game

---

## 🔑 First-Time Setup (5 minutes)

1. **Install dependency**:
   ```powershell
   pip install google-generativeai
   ```

2. **Get API key**: https://makersuite.google.com/app/apikey

3. **Configure** (choose one):
   - Option A: Run game → Menu option 4
   - Option B: Create `config.json`:
     ```json
     {
         "gemini_api_key": "YOUR_KEY_HERE"
     }
     ```

4. **Play**: `python quiz_game.py`

---

## 📝 Sample Quiz Session

```
Enter the quiz topic: Artificial Intelligence
How many questions do you want? (1-20): 5

🤖 Generating 5 questions about 'Artificial Intelligence'...
⏳ Please wait, this may take a few seconds...

✓ Successfully generated 5 questions!

Enter your name: Alex

Question 1/5:
What does AI stand for?
A) Automated Intelligence
B) Artificial Intelligence
C) Advanced Integration
D) Algorithmic Innovation

Your answer (A/B/C/D): B
✓ Correct!
```

---

## 💡 Tips & Tricks

### Getting Best Results from AI:
- **Be specific**: "Python list comprehensions" vs "Python"
- **Add context**: "Beginner Python Programming"
- **Try categories**: "2024 World News", "Classical Music Composers"

### Question Difficulty:
The AI naturally creates mixed difficulty. For specific levels:
- "Easy Python basics"
- "Advanced JavaScript concepts"
- "Expert-level Machine Learning"

### Multiple Attempts:
- Generate same topic multiple times = different questions!
- Challenge friends to beat your high score

---

## ⚡ Quick Commands

```powershell
# Run the game
python quiz_game.py

# Install dependencies
pip install -r requirements.txt

# Check Python version
python --version
```

---

## 🆘 Common Issues

| Issue | Solution |
|-------|----------|
| Module not found | `pip install google-generativeai` |
| API not configured | Create config.json with your API key |
| Failed to generate | Check internet connection & API key |
| Invalid JSON error | Regenerate questions (rare AI formatting issue) |

---

## 🎯 Challenge Ideas

1. **Topic Master**: Score 100% on 5 different topics
2. **Marathon**: Complete 20 questions without mistakes
3. **Speed Run**: Answer 10 questions as fast as possible
4. **Learning Path**: Create progressive quizzes (Beginner → Advanced)
5. **Friend Challenge**: Compete for high scores on same topic

---

**Ready to play? Run `python quiz_game.py` and have fun! 🚀**
