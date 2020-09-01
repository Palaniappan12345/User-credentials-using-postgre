from . import api
from flask import jsonify, request

from models import Name
from database import db
from utils import serialize_db_objects


'''
    http://0.0.0.0:5090/add/city
    http://0.0.0.0:5090/add/city?name=one&state=two
    
    http://0.0.0.0:5090/add/city?name=Toronto&state=Ontario
'''
@api.route("/add/name" , methods =['POST'])
def add_name():

    name = request.values.get('name')
    email = request.values.get('email')
    contact_number = request.values.get('contact_number')
    
    name = Name(name = name, email = email, contact_number = contact_number)

    db.session.add(name)
    db.session.commit()

    return "Successfully added"


'''
    http://0.0.0.0:5090/cities
'''
@api.route("/names")
def get_names():

    names = Name.query.all()

    result = {
        'names' : serialize_db_objects(names)
    }

    return jsonify(result)