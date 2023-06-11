from datetime import datetime
from sqlalchemy import Enum

from database import db


class Sessions(db.Model):
    __tablename__ = "sessions"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    start_time = db.Column(db.DateTime, default=datetime.now(), nullable=False)
    end_time = db.Column(db.DateTime)
    status = db.Column(Enum("active", "closed", name="session_status"), default="active")

    user = db.relationship("User", backref="sessions")

    def __init__(self, user_id, start_time=datetime.now(), end_time=None, status="active"):
        self.user_id = user_id
        self.start_time = start_time
        self.end_time = end_time
        self.status = status

    def __repr__(self):
        return f"<Session {self.id}>"
