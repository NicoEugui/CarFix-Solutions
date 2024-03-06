import os

class Config():
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEBUG = os.getenv('DEBUG')
    
    db_url = os.getenv("DATABASE_URL")
    
    if db_url is not None:
        SQLALCHEMY_DATABASE_URI = db_url.replace(
            "postgres://", "postgresql://")
    else:
        print("Database URL is not defined in .env")

config = {
    'development': DevelopmentConfig
}