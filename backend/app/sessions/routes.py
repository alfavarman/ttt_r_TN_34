from datetime import datetime

from flask import Blueprint, jsonify, request

from app.models import Sessions
from database import db

session_bp = Blueprint("session", __name__, url_prefix="/session")


@session_bp.route("/status", methods=["GET"])
def get_session_status():
    # get id from request
    session_id = request.args.get("session_id")

    # get session from db
    session = Sessions.query.get(session_id)

    # return session status or noexist
    if session:
        return jsonify({"status": session.status}), 200
    else:
        return jsonify({"error": "Session not exist"}), 404

@session_bp.route("/end", methods=["POST"])
def end_session():
    # Logic to end a session
    # Retrieve the session ID from the request
    session_id = request.json.get("session_id")

    # Query the database to get the session details
    session = Sessions.query.get(session_id)

    # Check if session exists
    if session is None:
        return jsonify({"error": "Session not found"}), 404

    # Update the session status and end time in the database
    session.status = "closed"
    session.end_time = datetime.utcnow()
    db.session.commit()

    return jsonify({"message": "Session ended successfully"}), 200