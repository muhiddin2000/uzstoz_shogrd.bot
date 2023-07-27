from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
# async def bot_help(message: types.Message):
#     text = ("Buyruqlar: ",
#             "/start - Botni ishga tushirish",
#             "/help - Yordam")
#
#     await message.answer("\n".join(text))
@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Muhiddin tomonidan tuzilgan",
            "Ustoz Shogird kanali",
            "Bu yerda Dasturlash bo`yocha \n\n"
            
            
            "#Ustoz\n"
            "#Shogird",
            "#uquvkursi",
            "#Sherik",
            "#Xodim",
            "#IshJoyi",
            "topish mumkun\n",
            "Elon berish: @UstozzShogirD_bot\n\n",
            "Admin:@coder_200")

    await message.answer("\n".join(text))