from flask import Flask
app = Flask(__name__)
from flask import abort
from flask.helpers import send_file
import os

app.use_x_sendfile = True

@app.route('/<path:path>')
def main(**kwargs):
    path = './static/' + kwargs['path']
    if os.path.isfile(path):
        return send_file(path)
    else:
        abort(404)

@app.route('/')
def index():
    path = './static/index.html'
    if os.path.isfile(path):
        return send_file(path)
    else:
        abort(404)
