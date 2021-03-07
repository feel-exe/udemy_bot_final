from asyncpg import UniqueViolationError

from utils.db_api.db_gino import db
from utils.db_api.schemas.product import Product


async def add_product(id: int, name: str, email: str = None):
    try:
        product = Product(id=id, name=name, email=email)
        await product.create()

    except UniqueViolationError:
        pass


async def select_all_product():
    product = await Product.query.gino.all()
    return product


async def select_product(id: int):
    product = await Product.query.where(Product.id == id).gino.first()
    return product


async def count_users():
    total = await db.func.count(Product.id).gino.scalar()
    return total


async def update_user_email(id, email):
    # строка ниже позволяет вытащить класс пользователя из БД и затем обращаться к нему через атрибуты и методы класса
    product = await Product.get(id)


    await product.update(email=email).apply()