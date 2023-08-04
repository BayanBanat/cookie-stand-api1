

# Lab: Class 33
# # api-quick-start
**Author: Bayan**

**Setup**

Create a virtual environment and activate it:
```
python -m venv .venv
source .venv/bin/activate

```

Launch the necessary services using Docker Compose:
```
docker-compose up
```

Environment Variables

SECRET_KEY= ###

DEBUG=True

ALLOWED_HOSTS=localhost,127.0.0.1,0.0.0.0

ALLOW_ALL_ORIGINS=True

Database Configuration


DATABASE_ENGINE: Specify the database engine for Django.

DATABASE_ENGINE=django.db.backends.postgresql
DATABASE_NAME: Set the name of PostgreSQL database.

DATABASE_USER: Provide the username for connecting to the PostgreSQL database.


DATABASE_PASSWORD: Use this variable to set the password for the database user.

DATABASE_HOST: Specify the host address of PostgreSQL database.

DATABASE_PORT: Set the port number for the database connection.


**Testing with HTTP Clients**
manually test the API endpoints, ThunderClient

**List of Routes**

**Get Tokens**
HTTP Method: POST

**Refresh Tokens**
HTTP Method: POST


**CRUD routes for resource**

HTTP Method: GET, POST, PUT, DELETE
Token Required: Yes

**PORT** - 8001


**How to initialize/run your application**
gunicorn

Install gunicorn if you haven't already:

```
pip install gunicorn
```

**in docker-compose.yml**

```
gunicorn project.wsgi:application --bind 0.0.0.0:8001 --workers 4
```
