from database import db
from flask import Blueprint, jsonify, request

multiplayer_bp = Blueprint("multiplayer", __name__, url_prefix="/game/multiplayer")


@multiplayer_bp.route("/waiting", methods=["POST"])
def wait_for_opponent():
    # wait for new player
    # start new session in new player or after x time return message with option try again / play vs computer
    pass


@multiplayer_bp.route("/join", methods=["POST"])
def join_multiplayer_game():
    # find active session and join player or return unavailable offer game against computer
    pass


@multiplayer_bp.route("/play", methods=["POST"])
def play_multiplayer_game():
    # make a move in multiplayer mode
    pass
