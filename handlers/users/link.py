from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
# from filters import IsPrivate
from loader import dp
from loader import bot

print("link")


# from re import compile
# from aiogram.methods import ExportChatInviteLink
# from aiogram.api.methods import ExportChatInviteLink
# from aiogram.api.methods.export_chat_invite_link import ExportChatInviteLink

@dp.message_handler(text="link")
async def bot_create_link(message: types.Message):
    shat_id = message.chat.id
    print(shat_id)
    await bot.export_chat_invite_link(shat_id)
    await message.answer(message.chat.user())

