from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS
from app.database import db
from app.api.user import user_bp  # Blueprint de l'utilisateur
from app.api.contact import contact_bp  # Blueprint du contact

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # Initialisation de la base de données et de Flask-Migrate
    db.init_app(app)
    migrate = Migrate(app, db)

    # Enregistrement des blueprints
    app.register_blueprint(user_bp)  # Enregistrement du blueprint utilisateur
    app.register_blueprint(contact_bp)  # Enregistrement du blueprint contact

    # Activer CORS
    CORS(app)

    return app
