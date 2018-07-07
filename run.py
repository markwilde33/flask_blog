import os
from flask import Flask, render_template, url_for

app = Flask(__name__)

posts = [
    {
        'author': 'Sparky fucking Wilde',
        'title': 'Blog Post 1',
        'content': '1st post content',
        'posted_on': '06 July, 2018'
    },
    {
        'author': 'Robert Albert "bert bert" Leyden',
        'title': 'Blog Post 2',
        'content': '2nd post content',
        'posted_on': '07 July, 2018'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='Shit Yeah')
    
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)