# flask-sqlalchemy-hello-world
Hello World REST API deployed with Python Flask and SQLAlchemy as ORM over SQLite database

## Dependencies
* Python 3.5+
* [Flask](https://flask.palletsprojects.com/)
* [SQLAlchemy](https://www.sqlalchemy.org/)
* [Gunicorn](https://gunicorn.org/)

## Installation
### Local installation

Create virtual env:

```
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
```

Install `fshw`:

```
pip install .
```

## Run it!

```
run_fshw
```

This will create a local server listening on default port (8000). Test it with:

```
curl -i http://localhost:8000/hello
```