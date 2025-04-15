from app import db

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password_hash = db.Column(db.String(128), nullable=False)

    # Relation avec les contacts

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    poids = db.Column(db.Float, nullable=False)
    age = db.Column(db.Float, nullable=False)

    # Clé étrangère vers l'utilisateur
