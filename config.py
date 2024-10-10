import os

SECRET_KEY = os.environ.get('SECRET_KEY') 
SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
SCHEDULER_API_ENABLED = os.environ.get('SCHEDULER_API_ENABLED')
RESEND_API_KEY = os.environ.get('RESEND_API_KEY')
SERVER_NAME = os.environ.get('SERVER_NAME')
APPLICATION_ROOT=os.environ.get('APPLICATION_ROOT')
PREFERRED_URL_SCHEME=os.environ.get('PREFERRED_URL_SCHEME')