from turtle import title
from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():

    posts = [
        {
            'author' : {'username' : 'John'},
            'body' : 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }, 
        {
            'author': {'username': 'Ипполит'},
            'body': 'Какая гадость эта ваша заливная рыба!!'
        },
        {
            'author': {'username': 'Геннадий'},
            'body': 'Привет!'
        }
    ]

    user = {'username' : 'Fedor'}

    return render_template('index.html', title = "Studying Flask", user = user, posts = posts)
