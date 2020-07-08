from flask import render_template
from flask import request, redirect, url_for

from flask_security import login_required
from flask_login import logout_user

from app import app, db
from admin import University


@app.route("/logout")
def logout():
    logout_user()
    return redirect('index')

@app.route('/')
@login_required
def index():
    obj = db.session.query(University).all()
    return render_template('index.html', n=obj)
    


@app.route('/detail/<int:pk>/')
@login_required
def detail(pk):
    univer = db.session.query(University).filter(University.id==pk).first()
    return render_template('detail.html', univer=univer)

