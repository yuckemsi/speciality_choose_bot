import threading

def notification(bot, message, text):
    bot.send_message(message.chat.id, f'Напоминание:\n{text}')

def schedule_notification(bot, message, time, text):
    timer = threading.Timer(time, notification(bot, message, text))
    timer.start()