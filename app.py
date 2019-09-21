from flask import Flask, render_template, request, send_file, redirect, url_for
import sqlite3

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return 'Hello World'

@app.route('/questions')
def questions():
    user = request.args.get('question')
    return user





if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5000, debug=True)
