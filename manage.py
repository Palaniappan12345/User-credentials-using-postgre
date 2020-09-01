from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from base import app
from database import db, DB_URL


# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'



migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

# from models import MyUser
# from models import *

if __name__ == '__main__':
    manager.run()