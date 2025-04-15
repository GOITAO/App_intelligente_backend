# app/routes.py
from flask import Blueprint  # type: ignore

# Définir le blueprint principal
main = Blueprint('main', __name__)

# Fonction pour enregistrer les routes
def register_routes(app):
    from app.api.user import user_bp  # Déplacer l'importation à l'intérieur de la fonction
    app.register_blueprint(user_bp)  # Enregistrer le blueprint utilisateur

    # Exemple d'ajout d'un autre blueprint, par exemple pour un blueprint 'admin'
    from app.api.contact import contact_bp  # Importation du blueprint admin
    app.register_blueprint(contact_bp)  # Enregistrer le blueprint admin
