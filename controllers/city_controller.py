from . import api
from flask import jsonify, request

from models import City
from database import db
from utils import serialize_db_objects


'''
    http://0.0.0.0:5090/add/city
    http://0.0.0.0:5090/add/city?name=one&state=two
    
    http://0.0.0.0:5090/add/city?name=Toronto&state=Ontario
'''
@api.route("/add/city" , methods =['POST'])
def add_city():

    name = request.values.get('name')
    state = request.values.get('state')
    country = request.values.get('country')
    
    city = City(name = name, state = state, country = country)

    db.session.add(city)
    db.session.commit()

    return "Successfully added"


'''
    http://0.0.0.0:5090/cities
'''
@api.route("/cities")
def get_cities():

    cities = City.query.all()

    result = {
        'cities' : serialize_db_objects(cities)
    }

    return jsonify(result)