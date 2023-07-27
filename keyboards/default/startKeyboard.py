from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.callback_data import CallbackData

menukeyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Sherik kerak"),
            KeyboardButton(text="Ish joyi kerak"),

        ],
        [
            KeyboardButton(text="Hodim kerak"),
            KeyboardButton(text="Ustoz kerak"),
        ],
        [
            KeyboardButton(text="Shogird kerak"),

        ],
    ],
    resize_keyboard=True
)
# post_callback = CallbackData("create_post", "action")
#
# confirmation_keyboard = ReplyKeyboardMarkup(
#     keyboard=[[
#         KeyboardButton(text="🆗 Chop etish", callback_data=post_callback.new(action="post")),
#         KeyboardButton(text="❌ Rad etish", callback_data=post_callback.new(action="cancel")),
#     ]],
#     resize_keyboard=True
# )
