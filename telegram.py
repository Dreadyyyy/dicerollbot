from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters.command import Command
from dotenv import dotenv_values as env

from utils import parse_dice

bot = Bot(token=env()["BOT_TOKEN"] or exit("No api key set!"))
dp = Dispatcher()


async def start_bot():
    await dp.start_polling(bot)


@dp.message(Command("start"))
async def start(message: Message) -> None:
    await message.answer(
        """
Commands:
    /roll {Amount of dice}d{Edges on a die} ...
    Example: /roll 2d6 3d8
        """
    )


@dp.message(Command("roll"))
async def roll(message: Message) -> None:
    if message.text is None:
        await message.reply("Wrong format!")
        return

    text = message.text.replace("/roll", "")
    text = text.strip(" ")
    await message.reply(parse_dice(text))
