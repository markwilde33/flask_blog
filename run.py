import os
from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return "Home Page"

@app.route('/about')
def about():
    return "About Page"
    
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)