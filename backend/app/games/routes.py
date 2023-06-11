from datetime import date, datetime

from flask import Blueprint, jsonify, request, url_for
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.models import User, Sessions, Games, Statistics
from app.ttt.ttt import TicTacToe
from database import db

games_bp = Blueprint("games", __name__, url_prefix="/game")


from flask import request, redirect

@games_bp.route("/select", methods=["GET", "POST"])
def select_game_mode():
    """ endpoint to select the game mode (player vs. computer or player vs. player)"""
    if request.method == "POST":
        mode = request.form.get("mode")
        if mode == "player_vs_computer":
            return redirect("/game/start/computer")
        elif mode == "player_vs_player":
            return redirect("/game/multiplayer/waiting")
        else:
            return jsonify({"error": "Invalid game mode"}), 400

    # get to select the mode
    game_modes = ["player_vs_computer", "player_vs_player"]
    # or redirect to endpoints depend on FE idea
    return jsonify({"game_modes": game_modes}), 200

game_session = TicTacToe()
@games_bp.route("/start", methods=["POST"])
@jwt_required
def start_game():
    # Retrieve the necessary data from the request, such as the selected game mode
    game_mode = request.json.get("game_mode")

    # get user credits
    user_id = get_jwt_identity()
    user = User.query.get(user_id)

    # handle user not enought credit
    if user.credits < 3:
        if user.credits == 0:
            # "user can add credit when has 0""
            return redirect(url_for("users.add_user_credits"))
        else:
            # "end game session when user cant add credit"
            return redirect(url_for("session.end_game_session"))


    # create new session and game
    session = Sessions(user_id=user_id, status="active")
    game = Games(session_id=session.id, start_time=datetime.now())

    user.credits -= 3
    db.session.add(session)
    db.session.add(game)
    db.session.commit()

    # return game created details
    return jsonify({
        "session_id": session.id,
        "game_id": game.id,
        "game_mode": game_mode,
        "user_credits": user.credits,
        "board": game.board
    }), 201



@games_bp.route("/play", methods=["POST"])
def play_game():
    """ endpoint to play a game"""

    # get data from request
    data = request.get_json()
    game_id = data.get("game_id")
    # get board from request
    board = data.get("board")
    # get move from request
    move = data.get("move")
    # get user_id from request
    user_id = data.get("user_id")
    # get session_id from request
    session_id = data.get("session_id")
    if move:
        move = int(move)

    # assign board to game object passed in requests
    game_session.board = board
    # make move
    game_session.make_move(move)
    # check for winner
    winner = game_session.check_winner()
    draw = (winner == 'tie')

    # if winner is None computer to make move
    if not winner:
        game_session.computer_make_move()
        winner = game_session.check_winner()
        if winner in ["X", "O"]:
            winner = "AI"

    if winner:
        user = User.query.get(user_id=user_id)
        game = Games.query.get(id=game_id)
        if not game:
            return jsonify({"error": "Game not found"}), 404
        game.result = winner
        game.end_time = datetime.now()
        game.duration = game.end_time - game.start_time

        # "4 credits if win"
        if winner in ["X", "O"]:
            user.credits += 4
        db.session.add(game)
        db.session.add(user)
        db.session.commit()
        return jsonify({
            "message": "Game finished",
            "session_id": session_id,
            "game_id": game_id,
            "user_credits": user.credits,
            "board": game.board,
            "winner": winner
        }), 201

    return jsonify({
        "message": "Move played successfully",
        "board": game_session.board,
        "session_id": session_id,
        "game_id": game_id,
    }), 200



@games_bp.route("/stats", methods=["GET"])
def get_game_stats():
    """endpoint to return stats for current day"""
    # get stats from today:
    today = date.today()
    statistics = Statistics.query.filter(db.func.date(Statistics.created_at) == today).all()

    # convert stats to dictionary
    game_stats = {}

    for stat in statistics:
        game_stats[stat.game_id] = {"duration": stat.duration, "results": [stat.result]}

    return jsonify(game_stats), 200