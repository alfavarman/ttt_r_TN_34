from database import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    credits = db.Column(db.Integer, nullable=False)
    # TODO credits default 10, id autoincrement
    # TODO logger - not task requirements/ extra


    def __repr__(self):
        return f"<User {self.username}>"

