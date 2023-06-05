# Tic-Tac-Toe REST API Application

This is a backend application for playing the game "Tic-Tac-Toe" using a REST API. It allows players to initiate game sessions, play rounds, and track statistics. The application follows RESTful principles and is containerized using Docker.

## General Description

The Tic-Tac-Toe REST API application provides a platform for users to play the classic game of Tic-Tac-Toe. Users can start new game sessions, make moves, and view statistics of their gameplay. The application utilizes Flask, SQLAlchemy, and Flask-SocketIO for real-time interactions (optional). It is designed with a modular and scalable architecture following the MVC pattern.

## Architecture Overview

The application follows a modified Model-View-Controller (MVC) architecture pattern. The key components of the architecture are:

- `backend/app/`: Contains the API-related code and routes (View).
- `backend/app/models/`: Contains the database models defined using SQLAlchemy (Model).
- `backend/app/games/`: Implements the Tic-Tac-Toe game logic (Controller).
- `backend/app/statistics/`: Handles the collection and aggregation of game statistics (Controller).
- `backend/app/database.py`: Manages the database connection and initialization.
- `backend/app/config.py`: Stores application configuration variables.
- `backend/tests/`: Contains unit tests for different components.
- `backend/migrations/`: Stores database migration scripts.
- `backend/scripts/`: Holds utility scripts or helper functions.

## Directory Structure

The project follows the following directory structure:

project-root/
├── backend/
│ ├── app/
│ ├── tests/
│ ├── migrations/
│ ├── scripts/
├── Dockerfile
├── docker-compose.yaml
├── requirements.txt
├── .flake8
├── .gitignore
├── lefthook.yml
├── pyproject.toml
└── README.md


## API Design

The API endpoints available in the application include:

- `/game/start`: Starts a new game session.
- `/game/play`: Allows players to make moves and play rounds.
- `/game/stats`: Retrieves aggregated statistics for a given day.

Detailed documentation for each API endpoint, including their input/output formats and usage, will be provided in the following sections.

## Installation

To run the Tic-Tac-Toe REST API application locally, follow these steps:

1. Clone the repository.
2. Set up a virtual environment and activate it.
3. Install the required dependencies using `pip install -r requirements.txt`.
4. Update the necessary configurations in `backend/app/config.py`.
5. Run the application using `python backend/app/main.py`.

## Testing

Unit tests are available to ensure the correctness of the application. To run the tests, follow these steps:

1. Set up a virtual environment and activate it.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Run the tests using `pytest backend/tests`.

## License

This project is licensed under the [Creative Commons Attribution-NonCommercial License 4.0](LICENSE). This license limits the usage of the project for non-commercial purposes only.


