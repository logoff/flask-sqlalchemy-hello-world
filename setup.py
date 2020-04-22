#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name="fshw",
    version="0.0.1",
    packages=find_packages(),
    scripts=["run_fshw"],

    # dependencies
    install_requires=[
        "Flask==1.1.2",
        "SQLAlchemy==1.3.16",
        "gunicorn==20.0.4"
    ],

    # metadata to display on PyPI
    author="logoff",
    description="Hello World REST API deployed with Python Flask and SQLAlchemy as ORM over SQLite database",
    keywords="flask sqlalchemy sqlite",
    url="https://github.com/logoff/flask-sqlalchemy-hello-world",
    project_urls={
        "Source Code": "https://github.com/logoff/flask-sqlalchemy-hello-world",
    },
    classifiers=[
        "License :: OSI Approved :: MIT License"
    ]
)
