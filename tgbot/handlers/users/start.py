from aiogram import Dispatcher
from aiogram.types import Message
from tgbot.keyboards.default.start_keyboard import menu



async def user_start(message: Message):
    # try:
    #     user = await db.add_user(
    #         telegram_id=message.from_user.id,
    #         full_name=message.from_user.full_name,
    #         username=message.from_user.username,
    #     )
    # except asyncpg.exceptions.UniqueViolationError:
    #     user = await db.select_user(telegram_id=message.from_user.id)

    await message.answer(
        "Добро пожаловать! Нажмите кнопку меню ниже, чтобы увидеть товары в нашем магазине",
        reply_markup=menu,
    )


def register_user(dp: Dispatcher):
    dp.register_message_handler(user_start, commands=["start"], state="*")

    # ADMINGA xabar beramiz
    # count = await db.count_users()
    # msg = f"{user[1]} bazaga qo'shildi.\nBazada {count} ta foydalanuvchi bor."
    # await bot.send_message(chat_id=ADMINS[0], text=msg)