from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

def main():
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton(text='❓ Пройти опрос', callback_data='quiz'))
    kb.add(InlineKeyboardButton(text='⌚ Напоминания', callback_data='notifications'))
    kb.add(InlineKeyboardButton(text='🎮 Мини-игра(в разработке)', callback_data='game'))
    kb.add(InlineKeyboardButton(text='⭐ Отзывы', callback_data='reviews'))
    return kb

def reviews_menu(tg_id):
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton(text='✍️ Оставить отзыв', callback_data='add_review'))
    kb.add(InlineKeyboardButton(text='📃 Посмотреть отзывы', callback_data='all_reviews'))
    kb.add(InlineKeyboardButton(text='🔮 Мои отзывы', callback_data=f'reviews_{tg_id}'))
    kb.add(InlineKeyboardButton(text='🔙 Назад', callback_data='main_menu'))
    return kb

def all_reviews(db):
    kb = InlineKeyboardMarkup()
    reviews = db.get_reviews()
    for review in reviews:
        kb.add(InlineKeyboardButton(text=review[2], callback_data=f'review_{review[0]}'))
    kb.add(InlineKeyboardButton(text='🔙 Назад', callback_data='reviews_menu'))
    return kb

def notifications_menu(tg_id):
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton(text='Создать напоминание', callback_data='create_notification'))
    kb.add(InlineKeyboardButton(text='Мои напоминания', callback_data='my_notifications'))
    kb.add(InlineKeyboardButton(text='🔙 Назад', callback_data='main_menu'))
    return kb

def user_notifications(db, tg_id):
    kb = InlineKeyboardMarkup()
    notifications = db.user_reminders(tg_id)
    if not notifications:
        kb.add(InlineKeyboardButton(text='Нет напоминаний', callback_data='no_notifications'))
    else:
        for notification in notifications:
            kb.add(InlineKeyboardButton(text=notification[2], callback_data=f'notification_{notification[0]}'))
    kb.add(InlineKeyboardButton(text='🔙 Назад', callback_data='main_menu'))
    return kb