from flask import render_template

from app import app



@app.route('/')
def index():
    n = 'beatch'
    return render_template('index.html', n=n)
    