import threading



def notification(bot, message, text, db):
	bot.send_message(message.chat.id, f'Напоминание:\n{text}')
	db.delete_reminder(message.chat.id, text)


def schedule_notification(bot, message, time, text, db):
    timer = threading.Timer(time, notification, args=(bot, message, text, db))
    timer.start()

