import asyncio
import logging
import sys
import os
import uuid
import json

from random import choice, randint
from decouple import config

from aiogram import Bot, Dispatcher, Router, types, F

from aiogram.filters import Command

bot = Bot(token="6977539871:AAHzRM2c3_td94pVwLfY0ZIVpC1XfcsW17Q")
dp = Dispatcher()


math_problems = [
    {"problem": "4 + 7 * 12", "answer": 88},
    {"problem": "9 * 5", "answer": 45},
    {"problem": "10 - 1 * 7", "answer": 3},
    {"problem": "135 / 6", "answer": 22.5}
]


@dp.message(Command("start"))
async def on_start(message: types.Message):
    for problem in math_problems:
        button = types.KeyboardButton(text=(problem))
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[button])

    await message.answer("Виберіть математичний приклад для розв'язання:", reply_markup=markup)

@dp.message(lambda message: message.text in [problem["problem"] for problem in math_problems])
async def on_math_problem_selected(message: types.Message):
    problem_text = message.text
    for problem in math_problems:
        if problem["problem"] == problem_text:
            await message.answer(f"Ви обрали приклад: {problem['problem']}. Тепер введіть вашу відповідь.")

@dp.message(lambda message: message.text.isdigit())
async def on_answer(message: types.Message):
    user_answer = float(message.text)
    for problem in math_problems:
        if user_answer == problem["answer"]:
            await message.answer("Ваша відповідь вірна! 👍")
            return
    await message.answer("Ваша відповідь невірна. 😔")


async def main():
    print("Starting bot...")
    print("Bot username: @{}".format((await bot.me())))
    await dp.start_polling(bot)

asyncio.run(main())
