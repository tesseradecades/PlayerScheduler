from flask import Flask, render_template
from schedulemaker import Player, generate_schedule

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/schedule')
def schedule():
    players = {
        Player("Nathan"), 
        Player("Frank"), 
        Player("Gabriel"), 
        Player("Adam"),
        Player("Nolan"),
        Player("Steven"),
        Player("Heather")
        }
    schedule = generate_schedule(players,21)
    return render_template('schedule.html',schedule=schedule)

if __name__ == '__main__':
   app.run(debug = True)