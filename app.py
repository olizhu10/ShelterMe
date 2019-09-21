from flask import Flask, render_template, request, send_file, redirect, url_for
<<<<<<< HEAD
=======
from node import Node
from path import ROOT
>>>>>>> 9c348ab328feaab2afb50eeba3b2b4c58f83af42
import sqlite3
import os

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html', last_updated=dir_last_updated('static'))

@app.route('/questions', methods=['GET','POST'])
def questions():
    question = request.args.get('question')
    role = request.args.get('role')
    if role == 'searcher':
        if question == 'location':
            return redirect(url_for())
        elif question == '':
            pass
        elif question == '':
            pass
    else:
        if question == '':
            pass
        elif question == '':
            pass
    return question+role

@app.route('/location', methods=['GET','POST'])
def location():
    return render_template('locationcheck.html', last_updated=dir_last_updated('static'))

def dir_last_updated(folder):
    return str(max(os.path.getmtime(os.path.join(root_path, f))
               for root_path, dirs, files in os.walk(folder)
               for f in files))

"""implement google API to locate user"""
def locate():
    return 'Ithaca, NY'

<<<<<<< HEAD



=======
"""finds the next page in the sequence depending on user input"""
@app.route('/next')
def next(current):
    try:
        request.form['ind']
    except:
        return PATH[current].children()[0].val()

"""retrieves location from database"""
@app.route('/location')
def get_location():
    return
>>>>>>> 9c348ab328feaab2afb50eeba3b2b4c58f83af42



if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5000, debug=True)
