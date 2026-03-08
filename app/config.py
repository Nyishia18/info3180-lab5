import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

class Config(object):
    """Base Config Object"""

    DEBUG = False

    SECRET_KEY = os.environ.get('SECRET_KEY')

    UPLOAD_FOLDER = os.environ.get('UPLOAD_FOLDER', './uploads')
    
    UPLOAD_FOLDER = "app/uploads"

    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL'
    ).replace('postgres://', 'postgresql://')

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    
    