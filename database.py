
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine

import os

from creds import *

# from sqlalchemy.ext.declarative import declarative_base

DB_URL = 'postgresql+psycopg2://{user}:{password}@{host}/{db}'.format(
    user=os.environ.get('POSTGRES_USER', POSTGRES_USER),
    password=os.environ.get('POSTGRES_PASSWORD', POSTGRES_PASSWORD),
    host=os.environ.get('POSTGRES_HOST', POSTGRES_HOST),
    db=os.environ.get('POSTGRES_DB_NAME', POSTGRES_DB_NAME),
    )

engine = create_engine(DB_URL)

db = SQLAlchemy()

def init_app(app):
    
    global db
    db = SQLAlchemy(app)