

from . import api
from flask import jsonify


@api.route("/base")
def home():

    result = {
        'who' : 'base'
    }

    return jsonify(result)