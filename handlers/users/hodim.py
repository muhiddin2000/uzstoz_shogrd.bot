from keyboards.inline.StartInline import confirmation_keyboard, post_callback
from states.PersonalData import Hodim
from loader import dp, bot
from aiogram import types
from aiogram.dispatcher import FSMContext
from data.config import ADMINS, CHANNELS
from aiogram.types import Message, CallbackQuery
from utils.util import *


@dp.message_handler(text='Hodim kerak', state=None)
async def send_link(message: Message):
    await message.answer("Hodim topish uchun ariza berish.\n\n" + suz, )
    await message.answer("Idora nomi ?")
    await Hodim.idora.set()

    @dp.message_handler(state=Hodim.idora, )
    async def answer_fullname(message: types.Message, state: FSMContext):
        idora = message.text

        await state.update_data(
            {"idora": idora}
        )

        await message.answer(yoshlar)
        await Hodim.next()

    @dp.message_handler(state=Hodim.texnologiya)
    async def answer_texnologiya(message: types.Message, state: FSMContext):
        texnologiya = message.text

        await state.update_data(
            {"texnologiya": texnologiya}
        )

        await message.answer(aloqalar)
        await Hodim.next()

    @dp.message_handler(state=Hodim.aloqa)
    async def answer_aloqa(message: types.Message, state: FSMContext):
        aloqa = message.text

        await state.update_data(
            {"aloqa": aloqa}
        )

        await message.answer(hududlar)
        await Hodim.next()

    @dp.message_handler(state=Hodim.hudud)
    async def answer_hudud(message: types.Message, state: FSMContext):
        hudud = message.text

        await state.update_data(
            {"hudud": hudud}
        )

        await message.answer(narxlar)
        await Hodim.next()

    @dp.message_handler(state=Hodim.masul)
    async def answer_aloqa(message: types.Message, state: FSMContext):
        masul = message.text

        await state.update_data(
            {"masul": masul}
        )

        await message.answer(masullar)
        await Hodim.next()

    @dp.message_handler(state=Hodim.murojat_vaqti)
    async def answer_murojat(message: types.Message, state: FSMContext):
        murojat_vaqti = message.text

        await state.update_data(
            {"murojat_vaqti": murojat_vaqti}
        )

        await message.answer(maqsadlar)
        await Hodim.next()

    @dp.message_handler(state=Hodim.ish_vaqti)
    async def answer_murojat(message: types.Message, state: FSMContext):
        ish_vaqti = message.text

        await state.update_data(
            {"ish_vaqti": ish_vaqti}
        )

        await message.answer(ishvaqti)
        await Hodim.next()

    @dp.message_handler(state=Hodim.narx)
    async def answer_narx(message: types.Message, state: FSMContext):
        narx = message.text

        await state.update_data(
            {"narx": narx}
        )

        await message.answer(narxlar)
        await Hodim.next()

    @dp.message_handler(state=Hodim.qushimcha_malumot)
    async def answer_maqsad(message: types.Message, state: FSMContext):
        qushimcha_malumot = message.text

        await state.update_data(
            {"qushimcha_malumot": qushimcha_malumot}
        )
        await message.answer("‼ Qo`shimcha ma'lumotlar ?")
        await Hodim.next()

        data = await state.get_data()
        texts = "Xodim kerak:\n\n"
        texts += f"🏢 Idora : {data.get('idora')}\n"
        texts += f"📚Texnologiya: {data.get('texnologiya')}\n"
        texts += f"🇺🇿Teligram: @{message.from_user.username}\n"
        texts += f"📞Aloqa: {data.get('aloqa')}\n"
        texts += f"🌐Hudud: {data.get('hudud')}\n"
        texts += f"✍Mas'ul: {data.get('masul')}\n"
        texts += f"🕰 Murojaat vaqti: {data.get('murojat_vaqti')}\n"
        texts += f"🕰 Ish vaqti: {data.get('ish_vaqti')}\n"
        texts += f"‼Qo`shimcha:  {data.get('qushimcha_malumot')}\n"
        await message.answer(texts)
        await message.answer(f"Barcha malumotlaringiz Tugrimi?",
                             reply_markup=confirmation_keyboard)



    @dp.callback_query_handler(post_callback.filter(action="post"), state=Hodim.Confirm, )
    async def confirm_post(call: CallbackQuery, state: FSMContext):
        data = await state.get_data()
        texts = "Xodim kerak:\n\n"
        texts += f"🏢 Idora : {data.get('idora')}\n"
        texts += f"📚Texnologiya: {data.get('texnologiya')}\n"
        texts += f"🇺🇿Teligram: @{message.from_user.username}\n"
        texts += f"📞Aloqa: {data.get('aloqa')}\n"
        texts += f"🌐Hudud: {data.get('hudud')}\n"
        texts += f"✍Mas'ul: {data.get('masul')}\n"
        texts += f"🕰 Murojaat vaqti: {data.get('murojat_vaqti')}\n"
        texts += f"🕰 Ish vaqti: {data.get('ish_vaqti')}\n"
        texts += f"‼Qo`shimcha:  {data.get('qushimcha_malumot')}\n"
        await state.finish()
        await call.message.edit_reply_markup()
        await call.message.answer("Post Adminga yuborildi")
        await bot.send_message(ADMINS[0], f"Foydalanuvchi {call.from_user.full_name} quyidagi postni chop etmoqchi:")
        await bot.send_message(ADMINS[0], texts, parse_mode="HTML", reply_markup=confirmation_keyboard)

    @dp.callback_query_handler(post_callback.filter(action="cancel"), state=Hodim.Confirm)
    async def cancel_post(call: CallbackQuery, state: FSMContext):
        await state.finish()
        await call.message.edit_reply_markup()
        await call.message.answer("Post rad etildi.")

    @dp.message_handler(state=Hodim.Confirm)
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
