from aiogram import Dispatcher

from loader import dp
from .throttling import ThrottlingMiddleware
from .database import GetDBUser


def setup(dp: Dispatcher):
    dp.middleware.setup(ThrottlingMiddleware())
    dp.middleware.setup(GetDBUser())

# if __name__ == "middlewares":
#     dp.middleware.setup(ThrottlingMiddleware())