from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

from telebot.types import User as TeleBotUser

kb1 = InlineKeyboardMarkup()
kb1.add(InlineKeyboardButton(text='Среднее', callback_data='answer_Среднее'))
kb1.add(InlineKeyboardButton(text='Высшее (бакалавр)', callback_data='answer_Высшее (бакалавр)'))
kb1.add(InlineKeyboardButton(text='Высшее (магистр)', callback_data='answer_Высшее (магистр)'))

kb2 = InlineKeyboardMarkup()
kb2.add(InlineKeyboardButton(text='Технологии', callback_data='answer_Технологии'))
kb2.add(InlineKeyboardButton(text='Наука', callback_data='answer_Наука'))
kb2.add(InlineKeyboardButton(text='Искусство и дизайн', callback_data='answer_Искусство и дизайн'))
kb2.add(InlineKeyboardButton(text='Бизнес и экономика', callback_data='answer_Бизнес и экономика'))
kb2.add(InlineKeyboardButton(text='Социальные науки', callback_data='answer_Социальные науки'))

kb3 = InlineKeyboardMarkup()
kb3.add(InlineKeyboardButton(text='Коммуникация', callback_data='answer_Коммуникация'))
kb3.add(InlineKeyboardButton(text='Аналитическое мышление', callback_data='answer_Аналитическое мышление'))
kb3.add(InlineKeyboardButton(text='Лидерство', callback_data='answer_Лидерство'))
kb3.add(InlineKeyboardButton(text='Технические навыки', callback_data='answer_Технические навыки'))

kb4 = InlineKeyboardMarkup()
kb4.add(InlineKeyboardButton(text='Индивидуальная работа', callback_data='answer_Индивидуальная работа'))
kb4.add(InlineKeyboardButton(text='Работа в команде', callback_data='answer_Работа в команде'))
kb4.add(InlineKeyboardButton(text='Гибкий график', callback_data='answer_Гибкий график'))
kb4.add(InlineKeyboardButton(text='Строгий график', callback_data='answer_Строгий график'))

kb5 = InlineKeyboardMarkup()
kb5.add(InlineKeyboardButton(text='Высокая зарплата', callback_data='answer_Высокая зарплата'))
kb5.add(InlineKeyboardButton(text='Возможность карьерного роста', callback_data='answer_Возможность карьерного роста'))
kb5.add(InlineKeyboardButton(text='Удобное местоположение', callback_data='answer_Удобное местоположение'))
kb5.add(InlineKeyboardButton(text='Интересные задачи', callback_data='answer_Интересные задачи'))
kb5.add(InlineKeyboardButton(text='Социальная значимость работы', callback_data='answer_Социальная значимость работы'))

kb6 = InlineKeyboardMarkup()
kb6.add(InlineKeyboardButton(text='Очень заинтересован(а)', callback_data='answer_Очень заинтересован(а)'))
kb6.add(InlineKeyboardButton(text='Не против', callback_data='answer_Не против'))
kb6.add(InlineKeyboardButton(text='Предпочитаю имеющиеся навыки', callback_data='answer_Предпочитаю имеющиеся навыки'))

questions = {
    1:kb1,
    2:kb2,
    3:kb3,
    4:kb4,
    5:kb5,
    6:kb6
}

class User:
    def __init__(self, user: TeleBotUser):
        self.first_name = user.first_name
        self.last_name = user.last_name
        self.username = user.username
        self.tg_id = user.id
        self.answers = {}
        self.count = 1


def start_quiz(user, bot, message):
    match user.count:
        case 1:
            bot.send_message(message.chat.id, "Привет! Я помогу тебе найти подходящую профессию или направление для развития.\n\n Ответь на несколько вопросов, чтобы мы могли лучше понять твои интересы и навыки")
            bot.send_message(message.chat.id, "Какой у тебя уровень образования?", reply_markup=questions[user.count])
        case 2:
            bot.send_message(message.chat.id, "В какой области ты сейчас работаешь или учишься?", reply_markup=questions[user.count])
        case 3:
            bot.send_message(message.chat.id, "Какие из следующих навыков у тебя развиты?", reply_markup=questions[user.count])
        case 4:
            bot.send_message(message.chat.id, "Какой стиль работы тебе ближе?", reply_markup=questions[user.count])
        case 5:
            bot.send_message(message.chat.id, "Какие факторы для тебя важны в работе?", reply_markup=questions[user.count])
        case 6:
            bot.send_message(message.chat.id, "Как ты относишься к обучению новым навыкам?", reply_markup=questions[user.count])
        case 7:
            recommended_professions = recommend_professions(user.answers[2], user.answers[3], user.answers[4])

            if recommended_professions:
               bot.send_message(message.chat.id, "На основе твоих ответов, вот несколько профессий, которые могут тебя заинтересовать:")
               for profession in recommended_professions:
                   bot.send_message(message.chat.id,f"- {profession}")

                
            else:
               bot.send_message(message.chat.id, 'К сожалению, я не нашел подходящих профессий на основе твоих ответов.')

def recommend_professions(field_of_study, skills, tasks_preference):
    recommendations = []

    if "Технологии" in field_of_study:
        if "Технические навыки" in skills:
            recommendations.extend(["Программист", "Системный администратор", "Data Scientist"])
        if "Аналитическое мышление" in skills:
            recommendations.extend(["Аналитик данных", "IT-менеджер"])
        if "Креативность" in skills:
            recommendations.append("UX/UI дизайнер")

    elif "Наука" in field_of_study:
        if "Аналитическое мышление" in skills:
            recommendations.extend(["Исследователь", "Биолог", "Физик"])
        if "Коммуникация" in skills:
            recommendations.append("Научный писатель")

    elif "Искусство и дизайн" in field_of_study:
        if "Креативность" in skills:
            recommendations.extend(["Графический дизайнер", "Художник", "Архитектор"])
        if "Коммуникация" in skills:
            recommendations.append("Маркетолог")

    elif "Бизнес и экономика" in field_of_study:
        if "Аналитическое мышление" in skills:
            recommendations.extend(["Экономист", "Финансовый аналитик"])
        if "Лидерство" in skills:
            recommendations.append("Менеджер проектов")

    elif "Социальные науки" in field_of_study:
        if "Коммуникация" in skills:
            recommendations.extend(["Социолог", "Психолог", "HR-менеджер"])

    if any(task in tasks_preference for task in ["Работать с людьми", "Создавать что-то новое"]):
        recommendations.append("Коуч/Наставник")

    if any(task in tasks_preference for task in ["Анализировать данные", "Решать проблемы"]):
        recommendations.append("Консультант")

    return list(set(recommendations))