import sys
from typing import List

from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/hello')
def hello():

    return f'Hello!\nPython {sys.version}\n'
