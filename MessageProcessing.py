import AnswersList
import random
import config
import time


def processing(message):

    resultList = []

    if message == '/help':
        resultList.insert(len(resultList), config.README)

    elif ('дурак' in message) or ('дибил' in message) or ('сука' in message) or (
            'ойвсе' in message) or ('обид' in message):
        resultList.insert(len(resultList), 'Ну не ругайся...')

    elif ('доброеутро' in message) or ('привет' in message) or ('добройночи' in message) or (
            'добрыйвечер' in message):
        resultList.insert(len(resultList), AnswersList.hello())

    elif ('какдела' in message) or ('кактвоидела' in message) or ('какнастроение' in message) or (
            'какнастрой' in message):
        resultList.insert(len(resultList), AnswersList.mood())

    elif ('чтоделаешь' in message) or ('чеделаешь' in message) or ('чемзанимаешься' in message) or (
            'чеммаешься' in message):
        resultList.insert(len(resultList), AnswersList.doing())

    elif ('хочуктебе' in message) or ('люблютебя' in message) or ('тебялюблю' in message) or (
            'скажичтолюбишь' in message) or (
            'скажилюблю' in message) or ('нелюбишь' in message) or ('напиши' in message):
        resultList.insert(len(resultList), AnswersList.compliment())
        time.sleep(2)

    elif ('комплимент' in message) or ('приятное' in message) or ('люблю' in message) or (
            'скажи' in message):
        resultList.insert(len(resultList), AnswersList.compliment())

    elif ('скучаю' in message) or ('соскуч' in message) or ('скучаешь' in message) or (
            'обним' in message) or ('скучаешь' in message):
        resultList.insert(len(resultList), AnswersList.miss() + ' ' + AnswersList.compliment())

    elif ('обижают' in message) or ('плохо' in message) or ('пожалей' in message) or ('дибилы' in message) or (
            'хочудомой' in message):
        resultList.insert(len(resultList), AnswersList.support())

    elif ('секс' in message) or ('пошалим' in message) or ('сделаемэто' in message) or (
            'трах' in message) or ('хочешьменя' in message) or ('хочутебя' in message):
        resultList.insert(len(resultList), AnswersList.sex())

    elif message == 'нет':
        resultList.insert(len(resultList), 'Ну на нет и суда нет')

    elif message == 'да':
        resultList.insert(len(resultList), 'Это хорошо...')

    else:
        resultList.insert(len(resultList), AnswersList.not_understand())
        if (random.randint(0, 3) == 2):
            resultList.insert(len(resultList), AnswersList.compliment())

    return resultList


"""
Добавить:

Покушал?
Кино
Шавуха
Чай
Реакция на хорошо
Работаешь
Доработать "Что делашь"
Целую
Спасибо
Смайлики
Соешко, Гоша
Зайка, котик и т.п

"""