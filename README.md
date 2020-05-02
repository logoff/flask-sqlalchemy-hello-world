# flask-sqlalchemy-hello-world
Hello World REST API deployed with Python Flask and SQLAlchemy as ORM over
SQLite database.

## Dependencies
* Python 3.8.2
* [Flask](https://flask.palletsprojects.com/)
* [SQLAlchemy](https://www.sqlalchemy.org/) with
  [Psycopg](https://www.psycopg.org/) as driver for
  [PostgreSQL](https://www.postgresql.org/) database
* [Gunicorn](https://gunicorn.org/)

## Installation
### Local installation

#### Run an instance of PostgreSQL

Use your PostgreSQL instance or simply use Docker (change credentials!):
```
docker run --name pg \
-e POSTGRES_PASSWORD=pass \
-d -p 5432:5432 \
-v ${PWD}/data:/var/lib/postgresql/data \
postgres:12.2
```

Create app database using Docker `psql` (use proper credentials):
```
docker container run -it postgres:12.2 \
psql -h 172.17.0.1 -U postgres -d postgres -c 'CREATE DATABASE fshw;'
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
pip install .
```

## Run it!

```
DATABASE_URL='postgresql+psycopg2://postgres:pass@172.17.0.1/fshw' \
.venv/bin/gunicorn fshw.fshw:app
```

This will create a local server listening on default port (8000). Test it with:

```
curl -i -X GET http://localhost:8000/hello
```
