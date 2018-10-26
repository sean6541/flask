from flask import Flask
app = Flask(__name__)
from flask import abort
from flask.helpers import send_file
import os

app.use_x_sendfile = True

@app.route('/<path:path>')
def main(**kwargs):
    path = '/var/www/cgiserver/static/' + kwargs['path']
    if os.path.isfile(path):
        return send_file(path)
    elif os.path.isdir(path):
        index_file = ''
        if path[-1:] == '/':
            index_file = path + 'index.html'
        else:
            index_file = path + '/index.html'
        if os.path.isfile(index_file):
            return send_file(index_file)
        else:
            abort(404)
    else:
        abort(404)

@app.route('/')
def index():
    path = '/var/www/cgiserver/static/index.html'
    if os.path.isfile(path):
        return send_file(path)
    else:
        abort(404)
