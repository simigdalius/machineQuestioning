import sqlite3
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# Βοηθητική συνάρτηση για σύνδεση στη Βάση
def get_db_connection():
    conn = sqlite3.connect('machineQuestioning.db')
    conn.row_factory = sqlite3.Row  # Για να παίρνουμε τα αποτελέσματα σαν dictionary
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/questions', methods=['GET'])
def get_questions():
    conn = get_db_connection()
    # Ζητάμε όλα τα πεδία ΕΚΤΟΣ από τη σωστή απάντηση και την επεξήγηση (αυτά μένουν κρυφά στον server)
    rows = conn.execute('SELECT id, chapter, question, option_1, option_2, option_3, option_4 FROM questions').fetchall()
    conn.close()

    safe_questions = []
    for row in rows:
        safe_questions.append({
            "id": row['id'],
            "chapter": row['chapter'],
            "question": row['question'],
            "options": [row['option_1'], row['option_2'], row['option_3'], row['option_4']]
        })
        
    return jsonify(safe_questions)

@app.route('/api/check', methods=['POST'])
def check_answer():
    data = request.get_json()
    question_id = data.get('id')
    user_answer = data.get('answer_index')

    conn = get_db_connection()
    # Βρίσκουμε τη σωστή απάντηση και την επεξήγηση για το συγκεκριμένο ID
    row = conn.execute('SELECT correct_index, explanation FROM questions WHERE id = ?', (question_id,)).fetchone()
    conn.close()

    if not row:
        return jsonify({"error": "Η ερώτηση δεν βρέθηκε"}), 404

    is_correct = (user_answer == row['correct_index'])

    return jsonify({
        "is_correct": is_correct,
        "correct_index": row['correct_index'],
        "explanation": row['explanation']
    })

if __name__ == '__main__':
    app.run(debug=True)