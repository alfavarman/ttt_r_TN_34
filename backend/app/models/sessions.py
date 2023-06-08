from database import db


class Sessions(db.Model):
    __tablename__ = 'sessions'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    start_time = db.Column(db.DateTime)
    end_time = db.Column(db.DateTime)
    status = db.Column(db.String(255))

    user = db.relationship('User', backref='sessions')

    def __repr__(self):
        return f"<Session {self.id}>"
