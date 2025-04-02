def recommend_professions(education_level, field_of_study, skills, tasks_preference):
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


def main():
    print("Привет! Я помогу тебе найти подходящую профессию или направление для развития.")
    print("Ответь на несколько вопросов, чтобы мы могли лучше понять твои интересы и навыки.\n")

    # Сбор ответов
    education_level = input(
        "1. Какой у тебя уровень образования? (Среднее/Высшее (бакалавр)/Высшее (магистр)/Другой): ")

    field_of_study = input(
        "2. В какой области ты сейчас работаешь или учишься? (Технологии/Наука/Искусство и дизайн/Бизнес и экономика/Социальные науки/Другой): ")

    skills = input(
        "3. Какие из следующих навыков у тебя развиты? (Коммуникация, Аналитическое мышление, Креативность, Лидерство, Технические навыки, Другие): ").split(
        ',')

    tasks_preference = input(
        "4. Какие из следующих задач тебе нравятся больше всего? (Работать с людьми, Решать проблемы, Создавать что-то новое, Анализировать данные, Работать с технологиями, Другие): ").split(
        ',')

    work_style = input(
        "5. Какой стиль работы тебе ближе? (Индивидуальная работа/Работа в команде/Гибкий график/Строгий график): ")

    work_factors = input(
        "6. Какие факторы для тебя важны в работе? (Высокая зарплата, Возможность карьерного роста, Удобное местоположение, Интересные задачи, Социальная значимость работы): ").split(
        ',')

    learning_attitude = input(
        "7. Как ты относишься к обучению новым навыкам? (Очень заинтересован(а) в обучении/Не против, если это необходимо/Предпочитаю использовать уже имеющиеся навыки): ")

    interested_professions = input("8. Какие профессии тебя интересуют? (Напиши несколько вариантов): ")

    print("\nСпасибо за ответы! Вот что я узнал о тебе:")
    print(f"Уровень образования: {education_level}")
    print(f"Область работы/учебы: {field_of_study}")
    print(f"Развитые навыки: {', '.join([skill.strip() for skill in skills])}")
    print(f"Предпочитаемые задачи: {', '.join([task.strip() for task in tasks_preference])}")
    print(f"Стиль работы: {work_style}")
    print(f"Важные факторы в работе: {', '.join([factor.strip() for factor in work_factors])}")
    print(f"Отношение к обучению: {learning_attitude}")
    print(f"Интересующие профессии: {interested_professions}")

    recommended_professions = recommend_professions(education_level, field_of_study, skills, tasks_preference)

    if recommended_professions:
        print("\nНа основе твоих ответов, вот несколько профессий, которые могут тебя заинтересовать:")
        for profession in recommended_professions:
            print(f"- {profession}")
    else:
        print("\nК сожалению, я не нашел подходящих профессий на основе твоих ответов.")


if __name__ == "__main__":
    main()
