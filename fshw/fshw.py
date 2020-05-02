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
    shops = Shop.query.all()

    shop_schema = ShopSchema()
    json_shops = shop_schema.dump(shops, many=True)

    return jsonify(json_shops)


@app.route("/shops", methods=["POST"])
def add_shop():
    if not request.is_json:
        abort(400)

    shop_schema = ShopSchema()
    shop = shop_schema.load(request.get_json(), session=db_session)

    db_session.add(shop)
    db_session.commit()

    return '',200


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()
