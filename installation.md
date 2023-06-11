# Project Name

A brief description of your project.

## Requirements

- Docker
- Docker Compose

## Setup

1. Clone the repository:
git clone <repository-url>
2. Set up environment variables:
- Create a `.env` file in the project root directory.
- Set the required environment variables in the `.env` file, including database credentials, API keys, etc.

3. Start the project:
docker-compose up -d

4. flask --app backend/app/app run
or python3 backend/app/app.py

This command will build and start the necessary containers for the project.

4. Access the application:
- Web: http://localhost:8000
- API: http://localhost:8000/api

5. Database & Migrations:
create migration repository - if you dont use migrations from repo:
>>>flask db init

generate initial migrations:
>>>flask db migrate -m "Initial migration"

to apply migrations to db:
>>>flask db upgrade

6. PyCharm Setup:
