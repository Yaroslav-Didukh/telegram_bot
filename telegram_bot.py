import telebot

#змінні
bot = telebot.TeleBot('798951881:AAG2sRR_q2r2-p16_4k7Upvz378olbnmnWc')
keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row('Привіт', 'До наступного разу', 'Перейти на сайт')

#старт бота і прийом повідомлень
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Бот включено', reply_markup = keyboard1)

@bot.message_handler(content_types=['sticker'])
def message(message):
    bot.send_sticker(message.chat.id, 'CAADAgADAQADwDZPExguczCrPy1RFgQ')

#код прийому повідомлень
@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привіт':
        bot.send_message(message.chat.id, 'Вітаю Вас!')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'До наступного разу!')
    elif message.text.lower() != 'привіт' or 'пока':
        bot.send_message(message.chat.id, 'З чого розпочнемо роботу?')

bot.polling()
