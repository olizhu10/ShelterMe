from flask import Flask, render_template, request, send_file, redirect, url_for

from node import Node
from path import ROOT
import sqlite3
import os

app = Flask(__name__, template_folder='templates')
with open('api_key.txt', 'r') as f:
    API_KEY = f.read()

@app.route('/')
def index():
    return render_template('index.html', last_updated=dir_last_updated('static'))

@app.route('/questions', methods=['GET','POST'])
def questions():
    question = request.args.get('question')
    return render_template(question+'.html', last_updated=dir_last_updated('static'),
        API_KEY=API_KEY)

@app.route('/map', methods=['GET','POST'])
def map():
    loc = get_location()
    return render_template('map.html', last_updated=dir_last_updated('static'),
        loc=loc, API_KEY=API_KEY)

@app.route('/results', methods=['GET','POST'])
def results():
    return render_template('results.html', last_updated=dir_last_updated('static'),
        API_KEY=API_KEY)

@app.route('/postmethod', methods = ['POST'])
def get_post_javascript_data():
    jsdata = request.form['javascript_data']
    return jsdata

def dir_last_updated(folder):
    return str(max(os.path.getmtime(os.path.join(root_path, f))
               for root_path, dirs, files in os.walk(folder)
               for f in files))

"""implement google API to locate user"""
def locate():
    return 'Ithaca, NY'

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
    return 'Ithaca, NY'

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5000, debug=True)
