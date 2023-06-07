from flask import Flask
from database import db, test_db_connection


# app instance to test configuration setup and db connection
def test_setup_app():
    # create app instance
    app = Flask(__name__)

    # Load app configuration
    app.config.from_object("config.Config")

    # Initialize the database - for db connection test
    db.init_app(app)

    # Test the database connection
    with app.app_context():
        test_db_connection()

    return app

if __name__ == '__main__':
    app = test_setup_app()
    app.run(debug=True)
