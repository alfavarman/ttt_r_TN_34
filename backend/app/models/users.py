from database import db
from werkzeug.security import check_password_hash


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    credits = db.Column(db.Integer, nullable=False, default=10)

    def __init__(self, username, password, credits):
        """init"""
        self.username = username
        self.password = password
        self.credits = credits

    def __repr__(self) -> str:
        """repr User username"""
        return f"<User {self.username}>"

    def create(self) -> str:
        db.session.add(self)
        db.session.commit()
        return "User created"

    def check_password(self, password: str) -> bool:
        """check password"""
        return check_password_hash(self.password, password)

    def add_credits(self) -> bool:
        """add credits"""
        if self.credits == 0:
            self.credits += 10
            db.session.commit()
            # TODO (EXTRA) logger
            return True
        else:
            return False
