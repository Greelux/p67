import asyncio
import logging
import random
random_num = random.randint(1, 100)
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command, CommandObject

logging.basicConfig(level=logging.INFO)
bot = Bot(token="7171952283:AAFZ0ibmPPXhvUPFhcJM-1qvbqscUwoGpaU")
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello!")

@dp.message(Command("help"))
async def cmd_help(message: types.Message):
    await message.answer("/help - отримати довідку за командами")
    await message.answer("/roll - Рандомне число від 1 до 100!")

@dp.message(Command("roll"))
async def cmd_roll(message: types.Message, command: CommandObject):
    if command.args is not None:
        args = command.args.split()
        if len(args) == 1:
            await message.answer(f"Рандомне число від 1 до {args[0]} Це:  {random.randint(1, int(args[0]))}")
        elif len(args) == 2:
            await message.answer(f"")  #Нужно сделать так чтобы когда пишут два числа, оно делало диапазон между ними
        else:
            pass
    else:
        await message.answer(f"Рандомне число від 1 до 100 Це:  {random_num}")

@dp.message()
async def cmd_all_messages(message: types.Message):
    print(f'{message.from_user.full_name}(id:{message.from_user.id}) {message.text}')

async def main():
    await bot.send_message(chat_id=915485959, text= "Бот Запущен!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())