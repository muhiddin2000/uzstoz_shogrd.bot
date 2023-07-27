from keyboards.inline.StartInline import confirmation_keyboard, post_callback
from states.PersonalData import Ish_Joy
from loader import dp, bot
from aiogram import types
from aiogram.dispatcher import FSMContext
from data.config import ADMINS, CHANNELS
from aiogram.types import Message, CallbackQuery
from utils.util import *


@dp.message_handler(text='Ish joyi kerak', state=None)
async def send_link(message: Message):
    await message.answer("Ish joyi  topish uchun ariza berish.\n\n" + suz,)
    await message.answer("Ism ,familyangizni kiriting ?")
    await Ish_Joy.fullname.set()
    @dp.message_handler(state=Ish_Joy.fullname, )
    async def answer_fullname(message: types.Message, state: FSMContext):
        fullname = message.text

        await state.update_data(
            {"fullname": fullname}
        )

        await message.answer(yoshlar)
        await Ish_Joy.next()

    @dp.message_handler(state=Ish_Joy.yoshi)
    async def answer_age(message: types.Message, state: FSMContext):
        yoshi = message.text

        await state.update_data(
            {"yoshi": yoshi}
        )

        await message.answer(texnologiyalar)
        await Ish_Joy.next()

    @dp.message_handler(state=Ish_Joy.texnologiya)
    async def answer_texnologiya(message: types.Message, state: FSMContext):
        texnologiya = message.text

        await state.update_data(
            {"texnologiya": texnologiya}
        )

        await message.answer(aloqalar)
        await Ish_Joy.next()

    @dp.message_handler(state=Ish_Joy.aloqa)
    async def answer_aloqa(message: types.Message, state: FSMContext):
        aloqa = message.text

        await state.update_data(
            {"aloqa": aloqa}
        )

        await message.answer(hududlar)
        await Ish_Joy.next()

    @dp.message_handler(state=Ish_Joy.hudud)
    async def answer_hudud(message: types.Message, state: FSMContext):
        hudud = message.text

        await state.update_data(
            {"hudud": hudud}
        )

        await message.answer(narxlar)
        await Ish_Joy.next()

    @dp.message_handler(state=Ish_Joy.narx)
    async def answer_narx(message: types.Message, state: FSMContext):
        narx = message.text

        await state.update_data(
            {"narx": narx}
        )

        await message.answer(kasblar)
        await Ish_Joy.next()

    @dp.message_handler(state=Ish_Joy.kasbi)
    async def answer_kasbi(message: types.Message, state: FSMContext):
        kasbi = message.text

        await state.update_data(
            {"kasbi": kasbi}
        )

        await message.answer(murojat_qilish_vaqti)
        await Ish_Joy.next()

    @dp.message_handler(state=Ish_Joy.murojat_vaqti)
    async def answer_murojat(message: types.Message, state: FSMContext):
        murojat_vaqti = message.text

        await state.update_data(
            {"murojat_vaqti": murojat_vaqti}
        )

        await message.answer(maqsadlar)
        await Ish_Joy.next()

    @dp.message_handler(state=Ish_Joy.maqsad)
    async def answer_maqsad(message: types.Message, state: FSMContext):
        maqsad = message.text

        await state.update_data(
            {"maqsad": maqsad}
        )
        await Ish_Joy.next()

        data = await state.get_data()
        texts = "Ish joyi kerak:\n\n"
        texts += f"🏅Sherik : {data.get('fullname')}\n"
        texts += f"🕑 Yosh : {data.get('yoshi')}\n"
        texts += f"📚Texnologiya: {data.get('texnologiya')}\n"
        texts += f"🇺🇿Teligram: @{message.from_user.username}\n"
        texts += f"📞Aloqa: {data.get('aloqa')}\n"
        texts += f"🌐Hudud: {data.get('hudud')}\n"
        texts += f"💰Narxi: {data.get('narxi')}\n"
        texts += f"👨🏻‍💻Kasbi: {data.get('kasbi')}\n"
        texts += f"🕰Murojat qilish vaqti : {data.get('murojat_vaqti')}\n"
        texts += f"🔎Maqsad:  {data.get('maqsad')}\n"
        await message.answer(texts)
        await message.answer(f"Barcha malumotlaringiz Tugrimi?",
                             reply_markup=confirmation_keyboard)

    # @dp.message_handler(state=PersonalData.NewMessage)
    # async def enter_message(message: Message, state: FSMContext):
    #     await message.answer(f"Barcha malumotlaringiz Tugrimi?",
    #                          reply_markup=confirmation_keyboard)
    #     await PersonalData.next()

    @dp.callback_query_handler(post_callback.filter(action="post"), state=Ish_Joy.Confirm, )
    async def confirm_post(call: CallbackQuery, state: FSMContext):
        data = await state.get_data()
        texts = "Ish joyi kerak :\n\n"
        texts += f"🏅Sherik : {data.get('fullname')}\n"
        texts += f"🕑 Yosh : {data.get('yoshi')}\n"
        texts += f"📚Texnologiya: {data.get('texnologiya')}\n"
        texts += f"🇺🇿Teligram: @{call.from_user.username}\n"
        texts += f"📞Aloqa: {data.get('aloqa')}\n"
        texts += f"🌐Hudud: {data.get('hudud')}\n"
        texts += f"💰Narxi: {data.get('narxi')}\n"
        texts += f"👨🏻‍💻Kasbi: {data.get('kasbi')}\n"
        texts += f"🕰Murojat qilish vaqti : {data.get('murojat_vaqti')}\n"
        texts += f"🔎Maqsad:  {data.get('maqsad')}\n"
        await state.finish()
        await call.message.edit_reply_markup()
        await call.message.answer("Post Adminga yuborildi")
        await bot.send_message(ADMINS[0], f"Foydalanuvchi {call.from_user.full_name} quyidagi postni chop etmoqchi:")
        await bot.send_message(ADMINS[0], texts, parse_mode="HTML", reply_markup=confirmation_keyboard)

    @dp.callback_query_handler(post_callback.filter(action="cancel"), state=Ish_Joy.Confirm)
    async def cancel_post(call: CallbackQuery, state: FSMContext):
        await state.finish()
        await call.message.edit_reply_markup()
        await call.message.answer("Post rad etildi.")

    @dp.message_handler(state=Ish_Joy.Confirm)
    async def post_unknown(message: Message):
        await message.answer("Chop etish yoki rad etishni tanlang")

    @dp.callback_query_handler(post_callback.filter(action="post"), user_id=ADMINS)
    async def approve_post(call: CallbackQuery):
        await call.answer("Chop etishga ruhsat berdingiz.", show_alert=True)
        target_channel = CHANNELS[0]
        message = await call.message.edit_reply_markup()
        await message.send_copy(chat_id=target_channel)

    @dp.callback_query_handler(post_callback.filter(action="cancel"), user_id=ADMINS)
    async def decline_post(call: CallbackQuery):
        await call.answer("Post rad etildi.", show_alert=True)
        await call.message.edit_reply_markup()
