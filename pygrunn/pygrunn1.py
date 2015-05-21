from app import app
from flask.templating import render_template

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<int:page>')
def index_nr(page):
    return render_template('index%d.html' % page)
