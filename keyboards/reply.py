from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from data.loader import db

def generate_main_menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    order = KeyboardButton(text='🛍 Заказать')
    review = KeyboardButton(text='✍ Оставить отзыв')
    feedback = KeyboardButton(text='☎ Связаться с нами')
    info = KeyboardButton(text='ℹ Информация')
    settings = KeyboardButton(text='⚙ Настройки')
    markup.row(order)
    markup.row(review, feedback)
    markup.row(info, settings)
    return markup


def generate_delivery_types():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    delivery = KeyboardButton(text='🚗 Доставка')
    self_delivery = KeyboardButton(text='🏃‍♀️Самовывоз')
    back_btn = KeyboardButton(text='🏠 Главное меню')
    markup.row(delivery, self_delivery)
    markup.row(back_btn)
    return markup


def generate_filials_buttons():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    back_btn = KeyboardButton(text='🚗 назад к доставке')
    filials = db.get_filials_names()  # [(максимка), (чорсу)]
    buttons = []
    for filial in filials:
        btn = KeyboardButton(text=filial[0]) # (максимка) -> максимка
        buttons.append(btn)
    markup.add(back_btn)
    markup.add(*buttons)
    return markup


