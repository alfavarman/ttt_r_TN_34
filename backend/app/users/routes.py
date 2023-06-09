from flask import Blueprint, jsonify, request

from app.models import User, Sessions, Games, Statistics
from database import db

users_bp = Blueprint('users', __name__, url_prefix='/user')


@users_bp.route('/create', methods=['POST'])
def create_user():
    # create new user
    pass


@users_bp.route('/login', methods=['POST'])
def login():
    # login, authentication ->
    pass


@users_bp.route('/credits', methods=['GET'])
def get_user_credits():
    # user_id -> get use credits
    pass


@users_bp.route('/credits', methods=['POST'])
def add_user_credits():
    # user_id add credits
    pass


@users_bp.route('/stats', methods=['GET'])
def get_user_stats():
    # user_id -> get user stats
    pass
