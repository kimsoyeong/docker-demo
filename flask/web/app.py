import time
import os

from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET'])
def hello():
    return 'Flask in a Docker!!! Hello World!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)