from flask import Blueprint, request, jsonify
from app import db
from app.models import Contact

import numpy as np
import joblib
import os
import logging

# Configuration des logs
logging.basicConfig(level=logging.DEBUG)

# Déclaration du blueprint
contact_bp = Blueprint('contact', __name__, url_prefix='/contacts')

# === Chargement du modèle une seule fois ===
model_path = 'model_classification.joblib'

try:
    model = joblib.load(model_path)
    logging.info("✅ Modèle chargé avec succès.")
except Exception as e:
    model = None
    logging.error(f"❌ Erreur lors du chargement du modèle : {e}")

# === POST : Créer un contact avec prédiction ===
@contact_bp.route('', methods=['POST'])
def create_contact():
    try:
        if model is None:
            return jsonify({"error": "Le modèle n'est pas chargé"}), 500

        data = request.get_json()
        poids = data.get('poids')
        age = data.get('age')

        if poids is None or age is None:
            return jsonify({"error": "Poids et âge sont requis !"}), 400

        try:
            poids = float(poids)
            age = float(age)
        except ValueError:
            return jsonify({"error": "Poids et âge doivent être des nombres valides !"}), 400

        # Prédiction
        features = [[poids, age]]
        probabilities = model.predict_proba(features)[0]
        prediction_class = model.predict(features)[0]
        prediction_proba = probabilities[1]  # Classe 1 (maladie chronique)

        # Sauvegarde dans la base de données
        new_contact = Contact(poids=prediction_class, age=prediction_proba)
        db.session.add(new_contact)
        db.session.commit()

        return jsonify({
            "message": "Contact créé avec succès !",
            "prediction_classe": int(prediction_class),
            "probabilités": {
                "classe_0": round(probabilities[0], 3),
                "classe_1": round(probabilities[1], 3)
            }
        }), 201

    except Exception as e:
        logging.error(f"❌ Erreur : {str(e)}")
        return jsonify({"error": f"Erreur lors de la prédiction ou l'enregistrement : {str(e)}"}), 500

# === GET : Récupérer tous les contacts ===
@contact_bp.route('/obtenir', methods=['GET'])
def get_contacts():
    try:
        contacts = Contact.query.all()

        if not contacts:
            return jsonify({"message": "Aucun contact trouvé."}), 200

        contact_list = [{"poids": contact.poids, "age": contact.age} for contact in contacts]

        return jsonify({"contacts": contact_list}), 200

    except Exception as e:
        logging.error(f"❌ Erreur lors de la récupération des contacts : {str(e)}")
        return jsonify({"error": f"Erreur lors de la récupération des contacts : {str(e)}"}), 500
