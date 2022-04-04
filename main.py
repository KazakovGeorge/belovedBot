import telebot
import datetime
import time
import random
import AnswersList
import config
import MessageProcessing
import logging

logging.basicConfig(filename='logs\log_' + str(datetime.datetime.now().strftime('%Y%m%d_%H%M%S')) + '.log', level=logging.INFO)


NAME = config.NAME
LINK = config.LINK
TOKEN = config.TOKEN
README = config.README


def filter_message(text: str):
    logging.info('RECEIVED: ' + text)
    print('RECEIVED: ', text)

    text = text.replace(" ", "")
    text = text.replace(".", "")
    text = text.replace("!", "")
    text = text.replace("?", "")
    text = text.replace(",", "")
    text = text.lower()

    return text


while 1:

    bot = telebot.TeleBot(TOKEN)
    answer = []

    try:

        # ===============================

        @bot.message_handler(commands=['start'])
        def start(message):
            logging.info(str(datetime.datetime.now()) + str(message))
            print(datetime.datetime.now(), message)

            bot.send_message(message.from_user.id, config.README)

        @bot.message_handler(content_types=['text', 'document', 'audio'])
        def get_text_messages(message):

            logging.info('___________________________\n' + str(datetime.datetime.now()) + '\nUSER ID: ' + str(message.from_user.id) + '\nUSER NAME: ' + str(message.from_user.username) + '\nCHAT ID: ' + str(message.chat.id))
            print('___________________________\n' + str(datetime.datetime.now()), '\nUSER ID: ', message.from_user.id, '\nUSER NAME: ', message.from_user.username, '\nCHAT ID: ', str(message.chat.id))

            message.text = filter_message(message.text)

            answer = MessageProcessing.processing(message.text)

            for msg in answer:
                #bot.send_message(message.from_user.id, msg)
                bot.send_message(message.chat.id, msg)

                logging.info('SENT: ' + msg)
                print('SENT: ', msg)

                time.sleep(1)


        bot.send_message(chat_id=264743594, text='Бот отключен')
        bot.polling(non_stop=False, interval=0)

        logging.info('restart bot ' + str(datetime.datetime.now()))
        print('restart bot ', datetime.datetime.now())

    except BaseException:
        print('+++++++++++++\n' + str(datetime.datetime.now()) + '\nБот отключен с ошибкой\n+++++++++++++\n')