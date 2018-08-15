#!/usr/bin/python3

from flup.server.fcgi import WSGIServer
from flask import Flask
app = Flask(__name__)
from werkzeug.contrib.fixers import CGIRootFix
from flask.helpers import send_file

app.use_x_sendfile = True

@app.route('/<path:path>.<string:ext>')
def main(**kwargs):
    path = './static/' + kwargs['path'] + '.' + kwargs['ext']
    return send_file(path)

@app.route('/')
def index():
    return send_file('./static/index.html')

if __name__ == '__main__':
    WSGIServer(CGIRootFix(app)).run()
