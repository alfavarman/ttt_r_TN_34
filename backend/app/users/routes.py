from flask import Blueprint, jsonify, request
from werkzeug.security import generate_password_hash
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required

from app.models import User, Sessions, Games, Statistics
from database import db


users_bp = Blueprint("users", __name__, url_prefix="/user")


@users_bp.route("/create", methods=["POST"])
def create_user():
    """ endpoint to create a new user username and password required"""
    # get data from request
    username = request.json.get("username")
    user = User.query.get(username=username)
    if user:
        return jsonify({"error": "User already exists"}), 400

    # TODO (EXTRA) password validator
    # hash password
    password = generate_password_hash(request.json.get("password"))

    # validate data
    if not username or not password:
        return jsonify({"error": "Missing username or password"}), 400

    # create user #TODO (EXTRA) def create user include hahsing
    user = User(username=username, password=password)
    db.session.add(user)
    db.session.commit()

    # TODO (EXTRA) logger
    return jsonify({"message": "User created"}), 201



@users_bp.route("/login", methods=["POST"])
def login():
    """ endpoint to handle user login"""
    # Get username from request or return missing username
    username = request.json.get("username")
    if not username:
        return jsonify({"error": "Missing username"}), 400

    # Get user from the database or return user does not exist
    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({"error": "User does not exist"}), 400

    # Get password from request or return missing password
    password = request.json.get("password")
    if not password:
        return jsonify({"error": "Missing password"}), 400

    # Check password
    if not user.check_password(password):
        return jsonify({"error": "Invalid credentials"}), 401

    # Generate access token
    access_token = create_access_token(identity=user.id)

    # TODO (EXTRA) logger
    return jsonify({"message": "User logged in", "access_token": access_token}), 200



@users_bp.route("/credits", methods=["GET"])
@jwt_required
def get_user_credits():
    """ endpoint to get user credits"""
    # return credits of auth user
    credits = User.query.get(id=get_jwt_identity()).credits
    return jsonify({"credits": credits}), 200


@users_bp.route("/credits", methods=["POST"])
@jwt_required
def add_user_credits():
    """ endpoint to add credits to user account user must be authenticated, balance must be 0"""
    user = User.query.get(id=get_jwt_identity())

    # TODO (EXTRA) payment
    added = user.add_credits()
    if added:
        return jsonify({"message": "Credits added"}), 200
    else:
        return jsonify({"error": "Credits can be added only when balance is 0"}), 400
    # TODO (EXTRA)logger



@users_bp.route("/stats", methods=["GET"])
@jwt_required
def get_user_stats():
    """ endpoint to get user statistics, user must be auth"""

    # get user stats:
    user_id = get_jwt_identity()
    data = Statistics.query.filter_by(user_id=user_id).all()
    if not data:
        return jsonify({"error": "User does not have statistics"}), 400

    stats = {}
    for stat in data:
        stats[stat.game_id] = {"duration": stat.duration, "result": stat.result}

    return jsonify(stats), 200
