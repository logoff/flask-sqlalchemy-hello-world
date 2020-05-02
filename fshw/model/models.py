import sqlalchemy as sa
from fshw.db.database import Base


class Shop(Base):
    __tablename__ = "shops"
    id = sa.Column(sa.Integer, primary_key=True)
    name: str = sa.Column(sa.String(50), unique=True)
    address: str = sa.Column(sa.String(200), nullable=False)

    def __init__(self, name: str = None, address: str = None):
        self.name = name
        self.address = address
