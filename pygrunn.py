from flask import Flask
from flask.templating import render_template
from util import setup_db
import os

app = Flask(__name__)
setup_db(app, database="pygrunn", user=os.environ['USER'])

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
