from sqlalchemy import Integer, Column, BigInteger, String, sql

from utils.db_api.db_gino import TimedBaseModel


class Product(TimedBaseModel):
    __tablename__ = 'products'
    id_product = Column(BigInteger, primary_key=True)
    title = Column(String(100))
    price = Column(String(100))
    points = Column(Integer)
    photo = Column(String(100))

    query: sql.Select