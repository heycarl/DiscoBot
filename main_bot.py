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

@bot.message_handler(commands=['signin'])

def answer(message):
    bot.send_message(message.chat.id, "Введите код администратора: ")
    configuration.status = 1

@bot.message_handler(content_types=['text'])
def answer(message):
    if configuration.status == 1:
        code = message.text
        if db_functions.check_admin_code(int(code)) == 1:
            bot.send_message(message.chat.id, "Вы успешно вошли в систему")
            print("Auth OK")
            configuration.status = 2
        else:
            bot.send_message(message.chat.id, "Неверный код, повоторите попытку")
            print("Auth Failed")



bot.polling(none_stop=True)
