from database import db
from sqlalchemy import Enum


class Statistics(db.Model):
    __tablename__ = "statistics"

    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, db.ForeignKey("games.id"), nullable=False)
    player_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    session_id = db.Column(db.Integer, db.ForeignKey("sessions.id"), nullable=False)
    duration = db.Column(db.Integer)
    result = db.Column(db.ForeignKey("games.result"))

    game = db.relationship("Games", backref="statistics")
    player = db.relationship("User", backref="statistics")

    def __repr__(self):
        return f"<Statistics {self.id}>"
