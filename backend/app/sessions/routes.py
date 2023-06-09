from flask import Blueprint, jsonify, request

from app.models import Sessions
from database import db

session_bp = Blueprint('session', __name__, url_prefix='/session')


@session_bp.route('/status', methods=['GET'])
def get_session_status():
    # get return session status
    pass


@session_bp.route('/end', methods=['POST'])
def end_session():
    # end session
    pass
