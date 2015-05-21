from flask import Flask
from util import setup_db
import os

app = Flask(__name__)
setup_db(app, database="pygrunn", user=os.environ['USER'])

from pygrunn.pygrunn1 import *
from pygrunn.pygrunn2 import *
from pygrunn.pygrunn3 import *
from pygrunn.pygrunn5 import *

if __name__ == '__main__':
    app.run(debug=True)
