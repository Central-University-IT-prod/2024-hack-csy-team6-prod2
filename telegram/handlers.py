import json

from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram import Router, Bot
from jsonf import write_inf

TOKEN = '{{sensitive data}}'
bot = Bot(TOKEN)
router = Router()


@router.message(CommandStart())
async def start(message: Message):
    user_id = str(message.from_user.id)
    data = {user_id: {}}
    for i in range(13):
        data[user_id][i] = "0"
    write_inf(data, "db_users.json")
    await message.reply('Привет! Я Аска, учусь В ЕГЭлионе, как и ты. Я буду следить за тобой и напоминать тебе тренироваться!')

# рассылка ачивок
# @router.message()
# async def text(message: Message):
#     user_id = message.from_user.id
#     if user_id == {{sensitive data}}:
#         await bot.send_sticker({{sensitive data}}, sticker="CAACAgIAAxkBAAEJIflnCp3HIXITOHCCvu_9WTkte7qlxwACil4AAnF0UEj4ba56-wlu-DYE")
#         await bot.send_sticker({{sensitive data}}, sticker="CAACAgIAAxkBAAEJIftnCp3KbGN61kxoJCbWhLPpjQ6x7wACc10AAnUbUEiisgABlE1abxY2BA")
#         await bot.send_sticker({{sensitive data}}, sticker="CAACAgIAAxkBAAEJIf9nCp3Ol36wSfcbjFAH4EMkNd8JTAACul4AAmitWUhJxAuAZ0486DYE")