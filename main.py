from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

TOKEN = "ТВОЙ_ТОКЕН"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message()
async def start(message: types.Message):
    await message.answer("Привет! Это VPN бот.")

if __name__ == '__main__':
    executor.run(dp, skip_updates=True)
