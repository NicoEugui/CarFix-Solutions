from flask import Flask
from src.routes import IndexRoutes
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from src.models.models import *
from config import config

app = Flask(__name__)

# Configuración de la aplicación
app.config.from_object(config['development'])

# Initialize SQLAlchemy
db.init_app(app)

# Initialize Migrate
MIGRATE = Migrate(app, db, compare_type=True)

# Blueprints
app.register_blueprint(IndexRoutes.main, url_prefix='/')

if __name__ == '__main__':
    app.run()