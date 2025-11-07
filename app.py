"""
Web-based Quiz Game using Flask
"""

from flask import Flask, render_template, request, jsonify, session
import json
import random
import os
from datetime import datetime
import google.generativeai as genai

app = Flask(__name__)
app.secret_key = 'your-secret-key-here-change-in-production'

class QuizGame:
    def __init__(self):
        self.high_score_file = "high_scores.json"
        self.api_key = None
        self.model = None
        self.ai_error = None
        self.setup_gemini_api()
    
    def setup_gemini_api(self):
        """Setup Google Gemini API"""
        try:
            self.ai_error = None
            # Try to get API key from environment variable first (for Vercel/production)
            # Then fall back to config.json (for local development)
            self.api_key = os.environ.get('GEMINI_API_KEY')
            
            if not self.api_key and os.path.exists("config.json"):
                with open("config.json", 'r') as f:
                    config = json.load(f)
                    self.api_key = config.get("gemini_api_key")

            if self.api_key:
                genai.configure(api_key=self.api_key)
                try:
                    # Some accounts / API keys may not have access to certain Gemini models.
                    # If the model is not found (NOT_FOUND) we'll catch the exception and
                    # disable AI features while keeping the web app functional.
                    self.model = genai.GenerativeModel('gemini-2.0-flash-exp')
                    print("✓ Gemini API configured successfully!")
                except Exception as e:
                    # Save a helpful error message for diagnostics and UI
                    err = str(e)
                    self.ai_error = err
                    print(f"⚠ Gemini model not available or API error: {err}")
                    self.model = None
            else:
                print("⚠ No API key found. AI question generation will be disabled.")
                self.model = None
        except Exception as e:
            self.ai_error = str(e)
            print(f"⚠ Error setting up Gemini API: {e}")
            self.model = None
    
    def get_default_questions(self):
        """Get default quiz questions"""
        questions = [
            {
                "question": "What is the capital of France?",
                "options": ["London", "Berlin", "Paris", "Madrid"],
                "answer": 2
            },
            {
                "question": "Which planet is known as the Red Planet?",
                "options": ["Venus", "Mars", "Jupiter", "Saturn"],
                "answer": 1
            },
            {
                "question": "What is 2 + 2?",
                "options": ["3", "4", "5", "6"],
                "answer": 1
            },
            {
                "question": "Who wrote 'Romeo and Juliet'?",
                "options": ["Charles Dickens", "Mark Twain", "William Shakespeare", "Jane Austen"],
                "answer": 2
            },
            {
                "question": "What is the largest ocean on Earth?",
                "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
                "answer": 3
            },
            {
                "question": "Which programming language is known for its use in data science?",
                "options": ["Java", "Python", "C++", "Ruby"],
                "answer": 1
            },
            {
                "question": "What year did World War II end?",
                "options": ["1943", "1944", "1945", "1946"],
                "answer": 2
            },
            {
                "question": "What is the smallest prime number?",
                "options": ["0", "1", "2", "3"],
                "answer": 2
            },
            {
                "question": "Which element has the chemical symbol 'O'?",
                "options": ["Gold", "Oxygen", "Osmium", "Carbon"],
                "answer": 1
            },
            {
                "question": "What is the speed of light?",
                "options": ["300,000 km/s", "150,000 km/s", "450,000 km/s", "600,000 km/s"],
                "answer": 0
            }
        ]
        return random.sample(questions, len(questions))
    
    def generate_ai_questions(self, topic, num_questions):
        """Generate questions using Gemini API"""
        if not self.model:
            # Model is not available; capture a helpful reason if possible
            print("❌ Gemini API is not configured. Cannot generate AI questions.")
            return None
        
        try:
            prompt = f"""Generate {num_questions} multiple choice quiz questions about {topic}.

For each question, provide:
1. The question text
2. Four options
3. The correct answer index (0-3)

Format your response as a valid JSON array with this exact structure:
[
    {{
        "question": "Question text here?",
        "options": ["First option", "Second option", "Third option", "Fourth option"],
        "answer": 2
    }}
]

Make the questions engaging and educational. Ensure variety in difficulty levels.
Return ONLY the JSON array, no additional text or markdown formatting."""

            response = self.model.generate_content(prompt)
            response_text = response.text.strip()
            
            # Remove markdown code blocks if present
            if response_text.startswith("```json"):
                response_text = response_text[7:]
            elif response_text.startswith("```"):
                response_text = response_text[3:]
            
            if response_text.endswith("```"):
                response_text = response_text[:-3]
            
            response_text = response_text.strip()
            questions = json.loads(response_text)
            return questions

        except json.JSONDecodeError as e:
            print(f"❌ Error parsing AI response: {e}")
            self.ai_error = f"AI response not valid JSON: {e}"
            return None
        except Exception as e:
            # Capture errors like NOT_FOUND (model not found) or permission issues
            err = str(e)
            print(f"❌ Error generating questions: {err}")
            self.ai_error = err
            return None
    
    def load_high_scores(self):
        """Load high scores from JSON file"""
        try:
            if os.path.exists(self.high_score_file):
                with open(self.high_score_file, 'r') as f:
                    return json.load(f)
        except Exception as e:
            print(f"Error loading high scores: {e}")
        return []
    
    def save_high_score(self, name, score, total):
        """Save a new high score"""
        try:
            high_scores = self.load_high_scores()
            entry = {
                "name": name,
                "score": score,
                "total": total,
                "percentage": round((score / total) * 100, 1),
                "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            high_scores.append(entry)
            
            with open(self.high_score_file, 'w') as f:
                json.dump(high_scores, f, indent=4)
            
            return True
        except Exception as e:
            print(f"Error saving high score: {e}")
            return False

# Initialize game
game = QuizGame()

@app.route('/')
def index():
    """Main page"""
    return render_template('index.html')

@app.route('/start-quiz', methods=['POST'])
def start_quiz():
    """Start a new quiz"""
    data = request.json
    quiz_type = data.get('type', 'default')
    
    if quiz_type == 'default':
        questions = game.get_default_questions()
        session['questions'] = questions
        session['current_question'] = 0
        session['score'] = 0
        return jsonify({'success': True, 'total_questions': len(questions)})
    
    elif quiz_type == 'custom':
        topic = data.get('topic', '')
        num_questions = int(data.get('num_questions', 5))
        
        if not game.model:
            return jsonify({'success': False, 'error': 'AI features not configured'})
        
        questions = game.generate_ai_questions(topic, num_questions)
        
        if questions:
            session['questions'] = questions
            session['current_question'] = 0
            session['score'] = 0
            return jsonify({'success': True, 'total_questions': len(questions)})
        else:
            return jsonify({'success': False, 'error': 'Failed to generate questions'})
    
    return jsonify({'success': False, 'error': 'Invalid quiz type'})

@app.route('/get-question', methods=['GET'])
def get_question():
    """Get current question"""
    questions = session.get('questions', [])
    current = session.get('current_question', 0)
    
    if current >= len(questions):
        return jsonify({'done': True})
    
    question = questions[current]
    return jsonify({
        'done': False,
        'question_number': current + 1,
        'total_questions': len(questions),
        'question': question['question'],
        'options': question['options']
    })

@app.route('/submit-answer', methods=['POST'])
def submit_answer():
    """Submit answer and get result"""
    data = request.json
    answer_index = int(data.get('answer', -1))
    
    questions = session.get('questions', [])
    current = session.get('current_question', 0)
    score = session.get('score', 0)
    
    if current >= len(questions):
        return jsonify({'error': 'No more questions'})
    
    question = questions[current]
    correct_answer = question['answer']
    is_correct = (answer_index == correct_answer)
    
    if is_correct:
        score += 1
        session['score'] = score
    
    session['current_question'] = current + 1
    
    return jsonify({
        'correct': is_correct,
        'correct_answer': correct_answer,
        'score': score
    })

@app.route('/finish-quiz', methods=['POST'])
def finish_quiz():
    """Finish quiz and save score"""
    data = request.json
    player_name = data.get('name', 'Anonymous')
    
    score = session.get('score', 0)
    questions = session.get('questions', [])
    total = len(questions)
    percentage = round((score / total) * 100, 1) if total > 0 else 0
    
    # Save high score
    game.save_high_score(player_name, score, total)
    
    # Get feedback
    if percentage == 100:
        feedback = "🏆 Perfect score! You're a genius!"
    elif percentage >= 80:
        feedback = "🌟 Excellent work!"
    elif percentage >= 60:
        feedback = "👍 Good job!"
    elif percentage >= 40:
        feedback = "📚 Not bad, but keep studying!"
    else:
        feedback = "💪 Keep practicing, you'll get better!"
    
    # Clear session
    session.pop('questions', None)
    session.pop('current_question', None)
    session.pop('score', None)
    
    return jsonify({
        'score': score,
        'total': total,
        'percentage': percentage,
        'feedback': feedback
    })

@app.route('/high-scores')
def high_scores():
    """Get high scores"""
    scores = game.load_high_scores()
    sorted_scores = sorted(scores, key=lambda x: x['percentage'], reverse=True)[:10]
    return jsonify(sorted_scores)

@app.route('/check-ai-status')
def check_ai_status():
    """Check if AI features are available"""
    return jsonify({'available': game.model is not None, 'error': getattr(game, 'ai_error', None)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
