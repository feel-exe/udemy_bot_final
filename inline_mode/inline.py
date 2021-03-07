from loader import dp

from aiogram import  types

@dp.inline_handler(text="")
async def empty_query(query: types.InlineQuery):
    await query.answer(
        results=[
            types.InlineQueryResultArticle(
                id = "unknow",
                title = "введите какой - то запрос",
                input_message_content=types.InputTextMessageContent(
                    message_text="НЕ обязательно жат ьн акнопку"
                )
            )
        ]
    )