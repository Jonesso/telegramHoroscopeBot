import telebot

bot = telebot.TeleBot('1738329242:AAFu0PjReh7LgSa6FxWagA2yPok0FfX-PjM')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text.lower() == "привет":

        bot.send_message(message.from_user.id,
                         "Привет, сейчас я расскажу тебе гороскоп на сегодня.")

    elif message.text == "/help":

        bot.send_message(message.from_user.id, "Напиши 'привет'")

    else:

        bot.send_message(message.from_user.id,
                         "Я тебя не понимаю. Напиши /help.")

bot.polling(none_stop=True, interval=0)
