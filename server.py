from flask import Flask, render_template
from schedulemaker import Player, generate_schedule, ncr

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
    num_on = 5
    schedule = generate_schedule(players,num_on=5,num_weeks=ncr(len(players),num_on))
    return render_template('schedule.html',schedule=schedule)

if __name__ == '__main__':
   app.run(debug = True)