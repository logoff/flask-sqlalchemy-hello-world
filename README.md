# flask-sqlalchemy-hello-world
Hello World REST API deployed with Python Flask and SQLAlchemy as ORM over
SQLite database.

## Dependencies
* Python 3.8.x
* [Flask](https://flask.palletsprojects.com/) web/REST framework
* [marshmallow-sqlalchemy](https://marshmallow-sqlalchemy.readthedocs.io/),
an integration of [marshmallow](https://marshmallow.readthedocs.io/)
serialization library and [SQLAlchemy](https://www.sqlalchemy.org/) ORM with
* [Psycopg](https://www.psycopg.org/) as driver for
  [PostgreSQL](https://www.postgresql.org/) database
* [Gunicorn](https://gunicorn.org/) WSGI HTTP Server

## Installation
### Local installation

#### Run an instance of PostgreSQL

Use your PostgreSQL instance or simply use Docker locally
(specific internal network for the database instance):
```
docker network create db_net;
docker container run --name pg \
-e POSTGRES_PASSWORD=pass \
-d -p 5432:5432 \
--network db_net \
-v ${PWD}/data:/var/lib/postgresql/data \
postgres:12.2
```

Create app database using Docker `psql`, connecting to PostgreSQL previous
instance:
```
docker container run \
--network db_net \
-it postgres:12.2 \
psql -h pg -U postgres -d postgres -c 'CREATE DATABASE fshw;'
```

#### Create virtual environment and install the app

Create virtual env:

```
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip wheel setuptools
```

Install `fshw`:

```
deactivate; source .venv/bin/activate
pip install .
```

## Run it!

1. With premade script:

```
deactivate; source .venv/bin/activate
DATABASE_URL='postgresql+psycopg2://postgres:pass@localhost/fshw' run_fshw
```

2. With gunicorn binary:

```
deactivate; source .venv/bin/activate
DATABASE_URL='postgresql+psycopg2://postgres:pass@localhost/fshw' \
gunicorn fshw.fshw:app
```

3. With flask binary:

```
deactivate; source .venv/bin/activate
DATABASE_URL='postgresql+psycopg2://postgres:pass@localhost/fshw' \ 
FLASK_APP=fshw.fshw \
flask run
```

4. With flask module:

```
deactivate; source .venv/bin/activate
DATABASE_URL='postgresql+psycopg2://postgres:pass@localhost/fshw' \ 
FLASK_APP=fshw.fshw \
python -m flask run
```


This will create a local server listening on default port
(8000 for gunicorn, 5000 for Flask). Test it with:

1. For gunicorn (previous options 1 and 2)
```
curl -i -X GET http://localhost:8000/hello
```

2. For Flask (previous options 3 and 4)
```
curl -i -X GET http://localhost:5000/hello
```
