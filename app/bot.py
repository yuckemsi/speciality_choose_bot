from telebot import TeleBot

from dotenv import load_dotenv
import os

from app.database.db import Database

import app.keyboards.kb as kb

load_dotenv()
bot = TeleBot(os.getenv('bot_token'))

db = Database()

@bot.message_handler(commands=['start'])
def send_welcome(msg):
    db.add_user(msg.chat.id, msg.from_user.username, msg.from_user.first_name)
    bot.send_message(msg.chat.id, 'Привет, я бот-помощник по выбору профессии для тебя, если ты устал от своей нынешней или хочешь попробовать себя в новом направлении! Для тебя доступно множество функций, которые помогут тебе выбрать свое предназначение')
    bot.send_message(msg.chat.id, 'Основное меню', reply_markup=kb.main())

@bot.message_handler(commands=['help'])
def send_help(msg):
    pass