from fshw.model.models import Shop
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema


class ShopSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Shop
        include_fk = True
        load_instance = True
