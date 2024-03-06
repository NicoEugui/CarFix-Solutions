from flask import Flask
from src.routes import IndexRoutes, UserRoutes
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from src.admin import setup_admin
from src.models.models import *
from config import config

app = Flask(__name__)

# Configuración de la aplicación
app.config.from_object(config['development'])

# Initialize SQLAlchemy
db.init_app(app)

setup_admin(app)

# Initialize Migrate
MIGRATE = Migrate(app, db, compare_type=True)

# Blueprints
app.register_blueprint(IndexRoutes.api, url_prefix='/')
app.register_blueprint(UserRoutes.api, url_prefix='/users')

if __name__ == '__main__':
    app.run()