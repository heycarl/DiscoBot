import telebot
import log_functions
import db_functions
import other_functions
import configuration

bot = telebot.TeleBot(configuration.token)

@bot.message_handler(commands=['start'])
def answer(message):
    bot.send_message(message.chat.id, "Следующим сообщением тебе придет личный код, который нужно будет говорить при сдаче денег и входе на дискотеку")
    user_code = other_functions.generate_code()
    bot.send_message(message.chat.id, user_code)
    log_functions.log("Code generated", message.chat.id, user_code)


bot.polling(none_stop=True)
