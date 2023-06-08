from database import db


class Games(db.Model):
    __tablename__ = 'games'

    id = db.Column(db.Integer, primary_key=True)
    session_id = db.Column(db.Integer, db.ForeignKey('sessions.id'), nullable=False)
    start_time = db.Column(db.DateTime)
    end_time = db.Column(db.DateTime)
    result = db.Column(db.String(255))

    session = db.relationship('Session', backref='games')

    def __repr__(self):
        return f"<Game {self.id}>"
