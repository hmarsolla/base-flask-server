import json
import os
import itertools
from functools import reduce
from datetime import datetime
from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.utils import secure_filename

def create_app(config):
    #create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('config')
    app.debug = False
    app.use_reloader=False

    CORS(app)

    @app.route('/')
    def main():
        return jsonify(status={'alive' : True}), 200

    return app