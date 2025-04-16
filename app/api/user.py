from flask import Blueprint, request, jsonify  # type: ignore
from werkzeug.security import generate_password_hash, check_password_hash  # type: ignore
from app import db
from app.models import User

user_bp = Blueprint('user', __name__, url_prefix='/users')

# CREATE (Créer un utilisateur)
@user_bp.route('', methods=['POST'])
def create_user():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if not username or not email or not password:
        return jsonify({"error": "Username, email, and password are required!"}), 400

    if User.query.filter_by(username=username).first():
        return jsonify({"error": "Username already exists!"}), 400

    if User.query.filter_by(email=email).first():
        return jsonify({"error": "Email already exists!"}), 400

    password_hash = generate_password_hash(password)

    new_user = User(username=username, email=email, password_hash=password_hash)

    db.session.add(new_user)
    try:
        db.session.commit()
        return jsonify({"message": "User created successfully!"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": f"Database error: {str(e)}"}), 500

# LOGIN (Connexion de l'utilisateur)
@user_bp.route('/login', methods=['POST'])
def login_user():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({"error": "Email "}), 400

    user = User.query.filter_by(email=email).first()

    if not user:
        return jsonify({"error": "Invalid email or password!"}), 401

    if not check_password_hash(user.password_hash, password):
        return jsonify({"password!"}), 401

    return jsonify({
        "user": {
            "username": user.username,
            "email": user.email
        }
    }), 200
