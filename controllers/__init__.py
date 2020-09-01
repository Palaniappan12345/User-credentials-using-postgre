


from flask import Blueprint

api = Blueprint('local_api', __name__)

from .base_controller import *
from .city_controller import *
from .user_controller import *