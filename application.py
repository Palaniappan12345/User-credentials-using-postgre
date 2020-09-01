from flask import Flask, jsonify

import database
from base import app

from controllers import *

app.register_blueprint(api)

# This line should not be here
database.init_app(app)

@app.route("/")
def home():
    return "Welcome To Postgre"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5090, debug=True)