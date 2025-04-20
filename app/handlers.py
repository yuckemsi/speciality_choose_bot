from telebot import TeleBot

from dotenv import load_dotenv
import os

from app.notifications.logic import schedule_notification

from app.database.db import Database

import app.keyboards.kb as kb

from app.logic import start_quiz, User

load_dotenv()
bot = TeleBot(os.getenv('bot_token'))

db = Database()

@bot.message_handler(commands=['start'])
def send_welcome(msg):
    global user

    user = User(msg.from_user)
    db.add_user(msg.chat.id, msg.from_user.username, msg.from_user.first_name)
    bot.send_message(msg.chat.id, 'Привет, я бот-помощник по выбору профессии для тебя, если ты устал от своей нынешней или хочешь попробовать себя в новом направлении! Для тебя доступно множество функций, которые помогут тебе выбрать свое предназначение')
    bot.send_message(msg.chat.id, 'Основное меню', reply_markup=kb.main())

@bot.message_handler(commands=['help'])
def send_help():
    pass

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    bot.answer_callback_query(call.id)
    bot.delete_message(call.message.chat.id, call.message.message_id)
    if call.data == 'quiz':
        start_quiz(user, bot=bot, message=call.message)
    elif call.data.startswith('answer_'):
        answer = call.data.split('_')[1]
        if user.count == 2:
            db.set_study_field(call.message.chat.id, answer)
        user.answers[user.count] = answer
        user.count += 1
        start_quiz(user, bot, call.message)
    elif call.data.startswith('reviews'):
        bot.send_message(call.message.chat.id, 'Здесь будут отзывы пользователей о профессиях', reply_markup=kb.reviews_menu(call.message.chat.id))
    elif call.data == 'all_reviews':
        if not db.get_reviews():
            bot.send_message(call.message.chat.id, 'Отзывов пока нет')
        else:
            bot.send_message(call.message.chat.id, 'ОТЗЫВЫ', reply_markup=kb.all_reviews(db))
    elif call.data == 'add_review':
        bot.send_message(call.message.chat.id, 'Напишите свой отзыв')

        bot.register_next_step_handler(call.message, add_review)
    elif call.data == 'main_menu':
        bot.send_message(call.message.chat.id, 'Основное меню', reply_markup=kb.main())
    elif call.data == 'notifications':
        bot.send_message(call.message.chat.id, 'НАПОМИНАНИЯ', reply_markup=kb.notifications_menu(call.message.chat.id))
    elif call.data == 'create_notification':
        bot.send_message(call.message.chat.id, 'Напиши текст напоминания')
        bot.register_next_step_handler(call.message, text_notification)
    elif call.data == 'game':
        bot.send_message(call.message.chat.id, 'Мини-игра в разработке', reply_markup=kb.main())
    elif call.data.startswith('review_'):
        review_id = call.data.split('_')[1]
        review = db.review_by_id(review_id)
        if review:
            bot.send_message(call.message.chat.id, f'Отзыв: \n\n{review[2]}\n\nАвтор: {review[1]}', reply_markup=kb.reviews_menu(call.message.chat.id))
        else:
            bot.send_message(call.message.chat.id, 'Отзыв не найден', reply_markup=kb.reviews_menu(call.message.chat.id))
    elif call.data == 'my_notifications':
        reminds = db.user_reminders(call.message.chat.id)
        if not reminds:
            bot.send_message(call.message.chat.id, 'У вас нет напоминаний', reply_markup=kb.notifications_menu(call.message.chat.id))
        else:
            bot.send_message(call.message.chat.id, 'Ваши напоминания', reply_markup=kb.user_notifications(db, call.message.chat.id))
    elif call.data.startswith('notification_'):
        notification_id = call.data.split('_')[1]
        notification = db.get_reminder_by_id(notification_id)
        if notification:
            bot.send_message(call.message.chat.id, f'Напоминание: \n{notification[2]}\nВремя: \n{notification[3]}', reply_markup=kb.user_notifications(db, call.message.chat.id))
            db.delete_reminder(call.message.chat.id, notification[2])
        else:
            bot.send_message(call.message.chat.id, 'Напоминание не найдено', reply_markup=kb.user_notifications(db, call.message.chat.id))

def text_notification(msg):
    text = msg.text
    bot.send_message(msg.chat.id, 'Отправь время напоминания в минутах')

    bot.register_next_step_handler(msg, time_notification, text)

def time_notification(msg, text):
    time = msg.text
    if not time.isdigit():
        bot.send_message(msg.chat.id, 'Введите число')
        bot.register_next_step_handler(msg, time_notification, text)
    else:
        time = int(time)*60
        schedule_notification(bot, msg, time, text, db)
        db.add_reminder(msg.chat.id, text, time)
        bot.send_message(msg.chat.id, 'Напоминание добавлено!', reply_markup=kb.notifications_menu(msg.chat.id))

def add_review(msg):
    db.add_review(msg.chat.id, msg.text)
    bot.send_message(msg.chat.id, 'Ваш отзыв добавлен')
    bot.send_message(msg.chat.id, 'Основное меню', reply_markup=kb.main())