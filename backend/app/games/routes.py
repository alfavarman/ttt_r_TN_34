from flask import Blueprint, jsonify, request

from app.models import User, Sessions, Games, Statistics
from database import db

games_bp = Blueprint('games', __name__, url_prefix='/game')


@games_bp.route('/select', methods=['GET'])
def select_game_mode():
    # game mode: vs computer or multiplayer
    pass


@games_bp.route('/start', methods=['POST'])
def start_game():
    # start new session, users ids
    pass


@games_bp.route('/play', methods=['POST'])
def play_game():
    # make move (player id, move) update -> updated game
    pass


@games_bp.route('/stats', methods=['GET'])
def get_game_stats():
    # get day stats:
    pass
