# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect
from .config import Config  # relative import

db = SQLAlchemy()
migrate = Migrate()
csrf = CSRFProtect()

def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)  # only once

    db.init_app(app)
    migrate.init_app(app, db)
    csrf.init_app(app)

    from app.views import main
    app.register_blueprint(main)

    return app



