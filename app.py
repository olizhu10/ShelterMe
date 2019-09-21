from flask import Flask, render_template, request, send_file, redirect, url_for
import sqlite3
import os

app = Flask(__name__, template_folder='templates')

PATH = None

@app.route('/')
def index():
    return render_template('index.html', last_updated=dir_last_updated('static'))

@app.route('/questions', methods=['GET','POST'])
def questions():
    question = request.args.get('question')
    return render_template(question+'.html', last_updated=dir_last_updated('static'))

def dir_last_updated(folder):
    return str(max(os.path.getmtime(os.path.join(root_path, f))
               for root_path, dirs, files in os.walk(folder)
               for f in files))

"""implement google API to locate user"""
def locate():
    return

def path():
    return


if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5000, debug=True)
