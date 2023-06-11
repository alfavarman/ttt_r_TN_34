from datetime import datetime

from database import db
from sqlalchemy import Enum


class Games(db.Model):
    __tablename__ = "games"

    id = db.Column(db.Integer, primary_key=True)
    session_id = db.Column(db.Integer, db.ForeignKey("sessions.id"), nullable=False)
    start_time = db.Column(db.DateTime, default=datetime.now(), nullable=False)
    end_time = db.Column(db.DateTime)
    result = db.Column(Enum("X", "O", "tie", name="result"))

    session = db.relationship("Session", backref="games")

    def __repr__(self):
        return f"<Game {self.id}>"
