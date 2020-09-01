
import os

POSTGRES_USER = 'postgres'
POSTGRES_PASSWORD = 'root'
POSTGRES_HOST = '0.0.0.0'
POSTGRES_DB_NAME = 'credentials'


DB_URL = 'postgresql+psycopg2://{user}:{password}@{host}/{db}'.format(
    user=os.environ.get('POSTGRES_USER', POSTGRES_USER),
    password=os.environ.get('POSTGRES_PASSWORD', POSTGRES_PASSWORD),
    host=os.environ.get('POSTGRES_HOST', POSTGRES_HOST),
    db=os.environ.get('POSTGRES_DB_NAME', POSTGRES_DB_NAME),
    )
'''
# app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
import os
# POSTGRES_USER     = 'postgres'
# POSTGRES_PASSWORD = 'pgtaleSDRD4Df!)&'
# POSTGRES_HOST     = 'postclick-postgres-dev.cgwfcwpnk7dd.us-east-1.rds.amazonaws.com'
# POSTGRES_DB_NAME  = 'postclickdev'
POSTGRES_USER     = 'postgres'
POSTGRES_PASSWORD = 'postgres'
POSTGRES_HOST     = '127.0.0.1'
POSTGRES_PORT     = '5000'
POSTGRES_DB_NAME  = 'kapi'
DB_URL = 'postgresql+psycopg2://{user}:{password}@{host}:{port}/{db}'.format(
    user     = os.environ.get('POSTGRES_USER', POSTGRES_USER),
    password = os.environ.get('POSTGRES_PASSWORD', POSTGRES_PASSWORD),
    host     = os.environ.get('POSTGRES_HOST', POSTGRES_HOST),
    port     = os.environ.get('POSTGRES_PORT', POSTGRES_PORT),
    db       = os.environ.get('POSTGRES_DB_NAME', POSTGRES_DB_NAME),
    
)
'''