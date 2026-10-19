from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import (
    Message,
    CallbackQuery,
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

from handlers.balance_water import balance_water


router = Router()


def get_main_keyboard():
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Трек воды")]
        ],
        resize_keyboard=True
    )
    return keyboard

def get_inline_keyboard():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="+250", callback_data="+250"), InlineKeyboardButton(text="-250", callback_data="-250")],
            [InlineKeyboardButton(text="+500", callback_data="+500"), InlineKeyboardButton(text="-500", callback_data="-500")]
        ],
    )
    return keyboard

@router.message(Command("start"))
async def start(message: Message):
    await message.answer("Бот для трека воды в дальнейшем будут улучшения",
    reply_markup=get_main_keyboard())

@router.message(F.text == "Трек воды")
async def show_water_tracker(message: Message):
    await message.answer(
        "Сколько выпито?",
        reply_markup=get_inline_keyboard()
    )


@router.callback_query(F.data.in_({'+250', '-250', '+500', '-500'}))
async def water(callback: CallbackQuery):
    user_id = callback.from_user.id
    total, done = balance_water(user_id, callback.data)

    if done:
        await callback.message.answer(text="на сегодня вода выпита пацанчо")
    else:
        await callback.message.answer(text=f"воды выпито {total}/2000 вась")

    await callback.answer()