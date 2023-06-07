# backend/app/database.py
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

# Create a new SQLAlchemy database instance
db = SQLAlchemy()

# Test the database connection
def test_db_connection():
    try:
        db.session.execute(text("SELECT 1"))
        print("Database connection successful!")
    except Exception as e:
        print("Database connection failed:", str(e))
