from aiogram.types import Message
from data.loader import bot, dp, db
from aiogram.dispatcher import FSMContext
from states.states import NumberState
import re
from keyboards.reply import generate_main_menu, generate_delivery_types, generate_filials_buttons


async def start_register(message: Message, state=None):
    await NumberState.phone.set()
    await message.answer('Введите номер телефона в формате: +998 ** *** ** **')


@dp.message_handler(state=NumberState.phone)
async def get_phone(message: Message, state: FSMContext):
    phone = message.text
    result1 = re.search(r'\+998 \d\d \d\d\d \d\d \d\d', phone)
    result2 = re.search(r'\+998\d{9}', phone)
    if result1 or result2:
        await state.finish()
        chat_id = message.chat.id
        full_name = message.from_user.full_name
        db.insert_user(chat_id, full_name, phone)
        '''Показать главное меню'''
        await show_main_menu(message)
    else:
        await state.finish()
        await again_ask_phone(message)

async def again_ask_phone(message: Message, state=None):
    await NumberState.phone.set()
    await message.answer('''Не верный формат телефона.
Введите номер телефона в формате: +998 ** *** ** **''')


@dp.message_handler(regexp='🏠 Главное меню')
async def show_main_menu(message: Message):
    await message.answer('Главное меню', reply_markup=generate_main_menu())


@dp.message_handler(regexp='🛍 Заказать')
async def show_delivery_types(message: Message):
    await message.answer('Выберите тип доставки', reply_markup=generate_delivery_types())


@dp.message_handler(regexp='🏃‍♀️Самовывоз')
async def show_filials(message: Message):
    await message.answer('Выберите фалиал', reply_markup=generate_filials_buttons())


filials = [i[0] for i in db.get_filials_names()]


@dp.message_handler(lambda message: message.text in filials)
async def show_menu(message: Message):
    await message.answer('Выберите категорию')
