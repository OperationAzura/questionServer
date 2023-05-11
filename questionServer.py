import json
from flask import Flask, request, render_template, session
import random
from gameStateClass import GameState

data = []

# Load the data from the JSON file
with open('list.json', 'r') as f:
    data = json.load(f)

start_num = 0
end_num = len(data) -1

app = Flask(__name__)
app.secret_key = 'abc'

random_numbers = []

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        gameState = GameState.fromDict(session['gameState'])
        random_num = generate_unique_random(start_num, end_num, gameState)
        print('xxxxxxxxxxxxxxxxx')
        print(gameState.numbers)
        session['gameState'] = gameState.__dict__
        if random_num == 'game over':
            return 'GAME OVER'
        if random_num >= len(data):
            return 'Index out of range! : ' + str(random_num)
        return render_template('result.html', player1=gameState.players[0], player2=gameState.players[1], element=data[random_num])
    return render_template('home.html')

@app.route('/skip')
def skip():
    gameState = GameState.fromDict(session['gameState'])
    random_num = generate_unique_random(start_num, end_num)
    print('xxxxxxxxx')
    print(gameState.numbers)
    if random_num >= len(data):
        return 'Index out of range!'
    return render_template('result.html', player1=gameState.players[0], player2=gameState.players[1], element=data[random_num])

@app.route('/startNewGame')
def start_new_game():
    return render_template('startNewGame.html')

@app.route('/newGame', methods=['POST'])
def new_game():
    #clear the game data
    random_numbers.clear()
    player1 = request.form['player1']
    player2 = request.form['player2']
    
    gameState = GameState([player1,player2])
    session['gameState'] = gameState.__dict__
    return render_template('result.html', player1=player1, player2=player2)

def generate_unique_random(start_num, end_num, gameState):
    random_numbers = gameState.numbers
    valid_range = [num for num in range(start_num, end_num+1) if num not in random_numbers]
    if not valid_range:
        return 'game over'
    rand_num = random.choice(valid_range)
    random_numbers.append(rand_num)
    gameState.numbers = random_numbers
    return rand_num

#save_game saves the state of the current game
def save_game(obj):
    pass

def save_to_json(obj, filename):
    with open(filename, 'w') as f:
        json.dump(obj, f)

if __name__ == '__main__':
    app.run("0.0.0.0", port="8000")
