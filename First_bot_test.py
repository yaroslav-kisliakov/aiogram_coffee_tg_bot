import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message
from bot_config_example import TOKEN
from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)

bot = Bot(token=TOKEN)
dp = Dispatcher()

menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🕒 Режим работы")],
        [KeyboardButton(text="📍 Адрес")],
        [KeyboardButton(text="📜 Наше меню")],
        [KeyboardButton(text="Сылки на наши соцсети и карты")],
    ],
    resize_keyboard=True,
)


society = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Наш Инстаграм", url="https://www.instagram.com/lecafegomel/"
            )
        ],
        [
            InlineKeyboardButton(
                text="Мы на картах",
                url="https://yandex.by/maps/org/le_cafe/32066750173/",
            )
        ],
    ]
)


@dp.message(CommandStart())
async def start_prog(message: Message):
    await message.answer(
        "Привет! Рады видеть тебя в Coffee break ☕️. Чем могу помочь?",
        reply_markup=menu,
    )


@dp.message(F.text == "Сылки на наши соцсети и карты")
async def start_but1(message: Message):
    await message.answer("Наш Инстаграмм и Мы На картах", reply_markup=society)


@dp.message(F.text == "🕒 Режим работы")
async def start_but2(message: Message):
    await message.answer(
        "Мы открыты каждый день с 8:00 до 22:00. Приходите за бодростью!"
    )


@dp.message(F.text == "📍 Адрес")
async def start_but3(message: Message):
    await message.answer(
        "Ждем вас по адресу: г. Гомель, ул. Советская, 15 (напротив главного парка)."
    )


@dp.message(F.text == "📜 Наше меню")
async def start_but4(message: Message):
    await message.answer(
        "Цены:\n\nЭспрессо — 3.50 BYN\n\nКапучино — 4.50 BYN\n\nЛатте — 5.00 BYN\n\nКруассан — 4.00 BYN"
    )


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
