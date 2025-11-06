"""
Quiz Game with High Score Tracking
A simple quiz game that randomizes questions and stores high scores
Now featuring AI-powered question generation using Google Gemini API
"""

import json
import random
import os
from datetime import datetime
import google.generativeai as genai

class QuizGame:
    def __init__(self):
        self.score = 0
        self.questions = []
        self.high_scores = []
        self.high_score_file = "high_scores.json"
        self.api_key = None
        self.model = None
        self.load_questions()
        self.load_high_scores()
        self.setup_gemini_api()
    
    def setup_gemini_api(self):
        """Setup Google Gemini API"""
        try:
            # Try to load API key from config file
            if os.path.exists("config.json"):
                with open("config.json", 'r') as f:
                    config = json.load(f)
                    self.api_key = config.get("gemini_api_key")
            
            if self.api_key:
                genai.configure(api_key=self.api_key)
                self.model = genai.GenerativeModel('gemini-1.5-flash')
                print("✓ Gemini API configured successfully!")
            else:
                print("⚠ No API key found. AI question generation will be disabled.")
                print("To enable AI features, add your API key to config.json")
        except Exception as e:
            print(f"⚠ Error setting up Gemini API: {e}")
            self.model = None
    
    def generate_ai_questions(self, topic, num_questions):
        """Generate questions using Gemini API"""
        if not self.model:
            print("❌ Gemini API is not configured. Cannot generate AI questions.")
            return None
        
        try:
            prompt = f"""Generate {num_questions} multiple choice quiz questions about {topic}.

For each question, provide:
1. The question text
2. Four options labeled A, B, C, D
3. The correct answer (just the letter: A, B, C, or D)

Format your response as a valid JSON array with this exact structure:
[
    {{
        "question": "Question text here?",
        "options": ["A) First option", "B) Second option", "C) Third option", "D) Fourth option"],
        "answer": "C"
    }}
]

Make the questions engaging and educational. Ensure variety in difficulty levels.
Return ONLY the JSON array, no additional text or markdown formatting."""

            print(f"\n🤖 Generating {num_questions} questions about '{topic}'...")
            print("⏳ Please wait, this may take a few seconds...\n")
            
            response = self.model.generate_content(prompt)
            
            # Extract JSON from response
            response_text = response.text.strip()
            
            # Remove markdown code blocks if present
            if response_text.startswith("```json"):
                response_text = response_text[7:]
            elif response_text.startswith("```"):
                response_text = response_text[3:]
            
            if response_text.endswith("```"):
                response_text = response_text[:-3]
            
            response_text = response_text.strip()
            
            # Parse JSON
            questions = json.loads(response_text)
            
            print(f"✓ Successfully generated {len(questions)} questions!\n")
            return questions
            
        except json.JSONDecodeError as e:
            print(f"❌ Error parsing AI response: {e}")
            print("The AI response was not in valid JSON format.")
            return None
        except Exception as e:
            print(f"❌ Error generating questions: {e}")
            return None
    
    def load_questions(self):
        """Load quiz questions from the questions database"""
        self.questions = [
            {
                "question": "What is the capital of France?",
                "options": ["A) London", "B) Berlin", "C) Paris", "D) Madrid"],
                "answer": "C"
            },
            {
                "question": "Which planet is known as the Red Planet?",
                "options": ["A) Venus", "B) Mars", "C) Jupiter", "D) Saturn"],
                "answer": "B"
            },
            {
                "question": "What is 2 + 2?",
                "options": ["A) 3", "B) 4", "C) 5", "D) 6"],
                "answer": "B"
            },
            {
                "question": "Who wrote 'Romeo and Juliet'?",
                "options": ["A) Charles Dickens", "B) Mark Twain", "C) William Shakespeare", "D) Jane Austen"],
                "answer": "C"
            },
            {
                "question": "What is the largest ocean on Earth?",
                "options": ["A) Atlantic Ocean", "B) Indian Ocean", "C) Arctic Ocean", "D) Pacific Ocean"],
                "answer": "D"
            },
            {
                "question": "Which programming language is known for its use in data science?",
                "options": ["A) Java", "B) Python", "C) C++", "D) Ruby"],
                "answer": "B"
            },
            {
                "question": "What year did World War II end?",
                "options": ["A) 1943", "B) 1944", "C) 1945", "D) 1946"],
                "answer": "C"
            },
            {
                "question": "What is the smallest prime number?",
                "options": ["A) 0", "B) 1", "C) 2", "D) 3"],
                "answer": "C"
            },
            {
                "question": "Which element has the chemical symbol 'O'?",
                "options": ["A) Gold", "B) Oxygen", "C) Osmium", "D) Carbon"],
                "answer": "B"
            },
            {
                "question": "What is the speed of light?",
                "options": ["A) 300,000 km/s", "B) 150,000 km/s", "C) 450,000 km/s", "D) 600,000 km/s"],
                "answer": "A"
            }
        ]
    
    def load_high_scores(self):
        """Load high scores from JSON file"""
        try:
            if os.path.exists(self.high_score_file):
                with open(self.high_score_file, 'r') as f:
                    self.high_scores = json.load(f)
        except Exception as e:
            print(f"Error loading high scores: {e}")
            self.high_scores = []
    
    def save_high_scores(self):
        """Save high scores to JSON file"""
        try:
            with open(self.high_score_file, 'w') as f:
                json.dump(self.high_scores, f, indent=4)
        except Exception as e:
            print(f"Error saving high scores: {e}")
    
    def display_high_scores(self):
        """Display the top 10 high scores"""
        print("\n" + "="*50)
        print("HIGH SCORES LEADERBOARD".center(50))
        print("="*50)
        
        if not self.high_scores:
            print("No high scores yet! Be the first to set a record!")
        else:
            sorted_scores = sorted(self.high_scores, key=lambda x: x['score'], reverse=True)[:10]
            for i, entry in enumerate(sorted_scores, 1):
                print(f"{i}. {entry['name']}: {entry['score']} points - {entry['date']}")
        print("="*50 + "\n")
    
    def add_high_score(self, name, score):
        """Add a new high score entry"""
        entry = {
            "name": name,
            "score": score,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.high_scores.append(entry)
        self.save_high_scores()
    
    def play_game(self, custom_questions=None):
        """Main game loop"""
        print("\n" + "="*50)
        print("WELCOME TO THE QUIZ GAME!".center(50))
        print("="*50)
        print("\nAnswer the questions by typing A, B, C, or D")
        print("Let's see how many you can get right!\n")
        
        # Get player name
        player_name = input("Enter your name: ").strip()
        if not player_name:
            player_name = "Anonymous"
        
        # Use custom questions if provided, otherwise use default questions
        if custom_questions:
            quiz_questions = custom_questions
        else:
            # Randomize questions
            quiz_questions = random.sample(self.questions, len(self.questions))
        
        self.score = 0
        total_questions = len(quiz_questions)
        
        # Ask each question
        for i, q in enumerate(quiz_questions, 1):
            print(f"\nQuestion {i}/{total_questions}:")
            print(q["question"])
            for option in q["options"]:
                print(option)
            
            # Get user answer
            while True:
                answer = input("\nYour answer (A/B/C/D): ").strip().upper()
                if answer in ['A', 'B', 'C', 'D']:
                    break
                print("Invalid input! Please enter A, B, C, or D.")
            
            # Check answer
            if answer == q["answer"]:
                print("✓ Correct!")
                self.score += 1
            else:
                print(f"✗ Wrong! The correct answer was {q['answer']}")
        
        # Display final score
        print("\n" + "="*50)
        print("GAME OVER!".center(50))
        print("="*50)
        print(f"\n{player_name}, you scored: {self.score}/{total_questions}")
        
        percentage = (self.score / total_questions) * 100
        print(f"Percentage: {percentage:.1f}%")
        
        # Performance feedback
        if percentage == 100:
            print("🏆 Perfect score! You're a genius!")
        elif percentage >= 80:
            print("🌟 Excellent work!")
        elif percentage >= 60:
            print("👍 Good job!")
        elif percentage >= 40:
            print("📚 Not bad, but keep studying!")
        else:
            print("💪 Keep practicing, you'll get better!")
        
        # Save high score
        self.add_high_score(player_name, self.score)
        print(f"\nYour score has been saved!")
    
    def play_custom_quiz(self):
        """Play quiz with AI-generated questions"""
        if not self.model:
            print("\n❌ AI question generation is not available.")
            print("Please configure your Gemini API key in config.json")
            print("\nSteps to get API key:")
            print("1. Visit: https://makersuite.google.com/app/apikey")
            print("2. Create a new API key")
            print("3. Create a config.json file with:")
            print('   {"gemini_api_key": "YOUR_API_KEY_HERE"}')
            return
        
        print("\n" + "="*50)
        print("AI-POWERED CUSTOM QUIZ".center(50))
        print("="*50)
        
        # Get topic from user
        topic = input("\nEnter the quiz topic (e.g., Python Programming, World History, Science): ").strip()
        if not topic:
            print("❌ Topic cannot be empty!")
            return
        
        # Get number of questions
        while True:
            try:
                num_questions = int(input("How many questions do you want? (1-20): ").strip())
                if 1 <= num_questions <= 20:
                    break
                else:
                    print("❌ Please enter a number between 1 and 20.")
            except ValueError:
                print("❌ Please enter a valid number.")
        
        # Generate questions
        ai_questions = self.generate_ai_questions(topic, num_questions)
        
        if ai_questions:
            # Play the game with AI-generated questions
            self.play_game(custom_questions=ai_questions)
        else:
            print("❌ Failed to generate questions. Please try again.")
    
    def main_menu(self):
        """Display main menu and handle user choices"""
        while True:
            print("\n" + "="*50)
            print("QUIZ GAME MENU".center(50))
            print("="*50)
            print("\n1. Play Quiz (Default Questions)")
            print("2. Play Custom Quiz (AI-Generated) 🤖")
            print("3. View High Scores")
            print("4. Configure API Key")
            print("5. Exit")
            
            choice = input("\nEnter your choice (1-5): ").strip()
            
            if choice == "1":
                self.play_game()
            elif choice == "2":
                self.play_custom_quiz()
            elif choice == "3":
                self.display_high_scores()
            elif choice == "4":
                self.configure_api_key()
            elif choice == "5":
                print("\nThank you for playing! Goodbye!")
                break
            else:
                print("\nInvalid choice! Please enter 1-5.")
    
    def configure_api_key(self):
        """Configure Gemini API key"""
        print("\n" + "="*50)
        print("CONFIGURE GEMINI API KEY".center(50))
        print("="*50)
        print("\nTo get your free API key:")
        print("1. Visit: https://makersuite.google.com/app/apikey")
        print("2. Sign in with your Google account")
        print("3. Click 'Create API Key'")
        print("4. Copy the API key")
        
        api_key = input("\nEnter your Gemini API key (or press Enter to cancel): ").strip()
        
        if not api_key:
            print("❌ API key configuration cancelled.")
            return
        
        try:
            # Save to config file
            config = {"gemini_api_key": api_key}
            with open("config.json", 'w') as f:
                json.dump(config, f, indent=4)
            
            print("✓ API key saved successfully!")
            
            # Reconfigure the API
            self.api_key = api_key
            genai.configure(api_key=self.api_key)
            self.model = genai.GenerativeModel('gemini-2.0-flash-exp')
            
            print("✓ Gemini API configured and ready to use!")
            
        except Exception as e:
            print(f"❌ Error saving API key: {e}")

def main():
    """Main entry point of the program"""
    game = QuizGame()
    game.main_menu()

if __name__ == "__main__":
    main()
