import os

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class Config:
    """Set Flask config variables."""

    # General Config
    ENVIRONMENT = os.getenv("ENVIRONMENT")
    FLASK_APP = os.getenv("FLASK_APP")
    FLASK_DEBUG = os.getenv("FLASK_DEBUG")
    SECRET_KEY = os.getenv("SECRET_KEY")
    # STATIC_FOLDER = "static"
    # TEMPLATES_FOLDER = "templates"

    # Database
    # SQLAlchemy database URI
    SQLALCHEMY_DATABASE_URI = f"postgresql://{os.getenv('DB_USERNAME')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
    # SQLAlchemy track modifications
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SQLAlchemy logs for debugging
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_MIGRATE_REPO = "backend/app/"
    MIGRATION_DIR = "backend/app/migrations"

    # Flask-Session
    SESSION_COOKIE_NAME = "tic-tac-toe"
    SESSION_TYPE = "sqlalchemy"
    SESSION_PERMANENT = False
    SESSION_SQLALCHEMY = SQLALCHEMY_DATABASE_URI
    SESSION_USE_SIGNER = True

    # JWT
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
    # blacklist enable
    JWT_BLACKLIST_ENABLED = True
    JWT_BLACKLIST_TOKEN_CHECKS = ["access"]
