import telebot
import log_functions
import db_functions
import other_functions
import configuration

bot = telebot.TeleBot(configuration.token)

@bot.message_handler(commands=['start'])
def answer(message):
    bot.send_message(message.chat.id, "Привет! Ниже прикреплен твой личный код, его нужно будет показать при сдаче 7-ми рублей на организацию и при входе на вечеринку")
    user_code = other_functions.generate_code()
    bot.send_message(message.chat.id, user_code)
    log_functions.log("Code generated", message.chat.id, user_code)

@bot.message_handler(commands=['auth'])
def answer(message):
    bot.send_message(message.chat.id, "Введите код администратора: ")
    configuration.status = 1

@bot.message_handler(commands=['newadmin'])
def answer(message):
    print("1231231")
    if message.from_user.id != 321965003:
        bot.send_message(message.chat.id, "Я хз откуда ты узнал об этой команде, но тут все равно контроль по id :)")
    else:
        admin_code = other_functions.generate_admin_code()
        bot.send_message(message.chat.id, admin_code)
        log_functions.log("Admin code generated", 321965003, admin_code)

@bot.message_handler(commands=['info'])
def answer(message):
    bot.send_message(message.chat.id, configuration.info_str)

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
