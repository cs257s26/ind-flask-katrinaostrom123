
from flask import Flask, render_template, request, session
from command_line import *
from game_command_line import *
app = Flask(__name__)

app.secret_key = "hello"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/game', methods=['GET', 'POST'])
def game_play():
    result_message = None
    
    #submit a guess
    if request.method == 'POST':
        user_guess = request.form.get('guess')
        correct_answer = session.get('correct_answer')
        correct_answer_count = session.get('correct_answer_count')

        if user_guess == correct_answer:
            result_message = f"Correct! {user_guess} is the most common."
        else:
            result_message = f"Incorrect, the most commonly reported animal is:  {correct_answer} reported  {correct_answer_count} times."
            
    #generate a new question
    data = load_data()
    current_game = game(data)
    session['correct_answer'] = current_game['correctAnimal']
    session['correct_answer_count'] = current_game['correctCount']
    
    return render_template('game.html', 
                           location=current_game['location'], 
                           options=current_game['options'],
                           message=result_message)


@app.route('/leaderboard/<animal_name>')
def show_leaderboard(animal_name=""):
    creature_of_interest = animal_name
    data = load_data()
    username_counts, username_key_storage = create_leaderboard(creature_of_interest, data)
    return render_template('leaderboard.html', animal_name=animal_name, username_key_storage=username_key_storage, username_counts=username_counts, max_display=100)    
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
