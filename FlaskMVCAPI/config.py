import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    # General settings
    DEBUG = True
    SECRET_KEY = os.environ.get('SECRET_KEY', 'your-default-secret-key')

    # Database settings
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL',
        f'sqlite:///{os.path.join(basedir, "app.db")}'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Optional: CORS, JWT, etc.
    # CORS_HEADERS = 'Content-Type'
    # JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY', 'your-jwt-secret')