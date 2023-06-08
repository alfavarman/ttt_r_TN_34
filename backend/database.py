from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from sqlalchemy_utils import database_exists, create_database
from config import Config


# Create a new SQLAlchemy database instance
db = SQLAlchemy()

# Test the database connection
def test_db_connection():
    if not database_exists(Config.SQLALCHEMY_DATABASE_URI):
        create_database(Config.SQLALCHEMY_DATABASE_URI)
        print("Database created!")
    try:
        db.session.execute(text("SELECT 1"))
        print("Database connection successful!")
    except Exception as e:
        print("Database connection failed:", str(e))
