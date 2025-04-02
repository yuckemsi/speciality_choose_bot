from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

def main(tg_id=None):
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton(text='Пройти опрос', callback_data='asd'))
    return kb