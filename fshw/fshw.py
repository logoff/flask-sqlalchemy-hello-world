import sys
from typing import List

from flask import Flask, abort, jsonify, request
from fshw.db.database import db_session, init_db
from fshw.model.models import Shop
from fshw.model.schemas import ShopSchema
from sqlalchemy import create_engine

init_db()

app = Flask(__name__)


@app.route("/")
@app.route("/hello")
def hello():
    return f"Hello!\nPython {sys.version}\n"


@app.route("/shops", methods=["GET"])
def get_all_shops():
    # get al, Shop instances of database
    shops = Shop.query.all()

    # serialize Shop list to dict
    shop_schema = ShopSchema()
    dict_shops = shop_schema.dump(shops, many=True)

    # serialize to JSON and return
    return jsonify(dict_shops)


@app.route("/shops", methods=["POST"])
def add_shop():
    # return 400 if not JSON in request body
    if not request.is_json:
        abort(400)

    # deserialize JSON to Shop object
    shop_schema = ShopSchema()
    name = request.get_json()["name"]
    shop = shop_schema.load(request.get_json(), session=db_session)

    # return 200 OK (with no body)
    return "", 200


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()
