import json
from flask import Flask, request, render_template
import random

data = []

# Load the data from the JSON file
with open('list.json', 'r') as f:
    data = json.load(f)

start_num = 0
end_num = len(data) -1

app = Flask(__name__)
random_numbers = []

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        #start_num = int(request.form['start_num'])
        #end_num = int(request.form['end_num'])
        random_num = generate_unique_random(start_num, end_num)
        if random_num == 'game over':
            return 'GAME OVER'
        if random_num >= len(data):
            return 'Index out of range! : ' + str(random_num)
        return render_template('result.html', element=data[random_num])
    return render_template('home.html')

@app.route('/skip')
def skip():
    #random_numbers = set(list(random_numbers)[:-1])
    #print('skipping')
    #print(random_numbers.pop())
    random_num = generate_unique_random(start_num, end_num)
    if random_num >= len(data):
        return 'Index out of range!'
    return render_template('result.html', element=data[random_num])

@app.route('/new_game')
def new_game():
    random_numbers.clear()
    return 'New game started <br> <a href="/">Generate a new random number</a>'

def generate_unique_random(start_num, end_num):
    valid_range = [num for num in range(start_num, end_num+1) if num not in random_numbers]
    if not valid_range:
        #print(random_numbers)
        return 'game over'
        #random_numbers.clear()
        #valid_range = range(start_num, end_num+1)
    rand_num = random.choice(valid_range)
    random_numbers.append(rand_num)
    #print('rand_num', rand_num)
    #print('random_numbers', random_numbers)
    #print('valid', valid_range)
    return rand_num

if __name__ == '__main__':
    app.run("0.0.0.0", port="8000")
