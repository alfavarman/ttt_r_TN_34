from flask import Flask
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate

from config import Config
from database import db, test_db_connection


# app instance to test configuration setup and db connection
def create_app():
    # create app instance
    app = Flask(__name__)

    # Load app configuration
    app.config.from_object(Config)

    # JWT
    jwt = JWTManager(app)

    # Initialize the database - for db connection test
    db.init_app(app)
    migrate = Migrate(app=app, db=db, directory=Config.MIGRATION_DIR)
    from app.models import (User, Statistics, Games, Sessions)

    # Test the database connection
    with app.app_context():
        test_db_connection()

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)


############
# TODO Extra (out of task scope) Logger