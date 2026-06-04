from flask import Flask, render_template, request, session
from ProductionCode import command_line
from ProductionCode import game_command_line

from Data import datasource

app = Flask(__name__)

app.secret_key = "hello"

@app.route('/')
def index():
    return render_template('index.html')

#helper function for game_play()
def get_randomLocation():
    connection = datasource.connect()
    randomLocation = datasource.get_random_location(connection)
    randomLocation = randomLocation[0]
    randomLocation = randomLocation[0] #getting the singular string from the array
    print(randomLocation)
    return randomLocation

#another helper function for game_play()
def top_5Animals(location):
    connection = datasource.connect()
    return datasource.get_top5Animals(connection, location)

@app.route('/game', methods=['GET', 'POST'])
def game_play():
    '''This route will randomly choose a location and ask the user to guess the top species there'''
    result_message = None
    location = get_randomLocation()
    listOfTop5Animals= top_5Animals(location)
    mostCommonAnimal = listOfTop5Animals[0]
    mostCommonAnimalName = mostCommonAnimal[0]
    mostCommonAnimalCount = mostCommonAnimal[1]

    #submit a guess
    if request.method == 'POST':
        user_guess = request.form.get('guess')
        correct_answer = session.get('correct_answer')
        correct_answer_count = session.get('correct_answer_count')

        if user_guess == correct_answer:
            result_message = f"Correct! {user_guess} is the most common."
        else:
            result_message = f"Incorrect, the most commonly reported animal is:  {correct_answer} reported  {correct_answer_count} times."
        
    session['correct_answer'] = mostCommonAnimalName
    session['correct_answer_count'] = mostCommonAnimalCount

    return render_template('game.html', 
                        location=location, 
                        options=(animal[0] for animal in listOfTop5Animals),
                        message=result_message)

@app.route('/leaderboard/<animal_name>')
def show_leaderboard(animal_name=""):
    """Displays the top 100 contributors for a given animal."""
    connection = datasource.connect()
    result = datasource.get_leaderboard(connection, animal_name)
    return render_template('leaderboard.html', animal_name=animal_name, result=result, max_display=100)    

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
