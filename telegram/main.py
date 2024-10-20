import asyncio
import json
from datetime import datetime
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from aiogram.types import FSInputFile
from aiogram import Bot, Dispatcher
from handlers import router

TOKEN = '{{sensitive data}}'
bot = Bot(TOKEN)

# отправка стикеров (ачивок)
async def sticker1(user_id, ind):
    if ind == 1:
        await bot.send_sticker({{sensitive data}}, sticker="CAACAgIAAxkBAAEJIflnCp3HIXITOHCCvu_9WTkte7qlxwACil4AAnF0UEj4ba56-wlu-DYE")
    elif ind == 2:
        await bot.send_sticker({{sensitive data}}, sticker="CAACAgIAAxkBAAEJIftnCp3KbGN61kxoJCbWhLPpjQ6x7wACc10AAnUbUEiisgABlE1abxY2BA")
    elif ind == 3:
        await bot.send_sticker({{sensitive data}}, sticker="CAACAgIAAxkBAAEJIf1nCp3LW1lNqZzqjc0FnhE-6sdaywACclIAAlsCUUgP78XRAAHWiAk2BA")
    else:
        await bot.send_sticker({{sensitive data}}, sticker="CAACAgIAAxkBAAEJIf9nCp3Ol36wSfcbjFAH4EMkNd8JTAACul4AAmitWUhJxAuAZ0486DYE")



async def main():
    dp = Dispatcher()
    dp.include_router(router)
    scheduler = AsyncIOScheduler()
    scheduler.add_job(remind, "interval", seconds=3600)
    scheduler.start()
    await dp.start_polling(bot)


# напоминание в x и y часов
async def remind():
    now = datetime.now()
    if now.hour == 10 or now.hour == 20:
        with open("db_users.json", 'r') as f:
            data = json.load(f)
            for i in data:
                await bot.send_message(i, "Напоминаю выполнить ежедневную тренировку!")


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот выключен')
