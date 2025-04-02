# app/__init__.py
from flask import Flask # type: ignore
from flask_migrate import Migrate # type: ignore
from flask_cors import CORS # type: ignore
from app.database import db
from app.api.user import user_bp  # Importation du blueprint utilisateur

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # Activer CORS
    CORS(app)

    # Initialisation de la base de données et de Flask-Migrate
    db.init_app(app)
    migrate = Migrate(app, db)

    # Enregistrement du blueprint utilisateur
    app.register_blueprint(user_bp)

    return app
