from app import app
from flask import render_template


@app.route('/')
def index():
    name = 'Всем привет!!!'
    return render_template('index.html', n=name)
