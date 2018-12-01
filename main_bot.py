import telebot
import log_functions
import db_functions
import other_functions
import configuration

bot = telebot.TeleBot(configuration.token)

@bot.message_handler(commands=['start'])
def answer(message):
    bot.send_message(message.chat.id, configuration.start_text)
    configuration.status = 3

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

@bot.message_handler(commands=['checkpay'])
def answer(message):
    bot.send_message(message.chat.id, configuration.checkpay_text)
    configuration.status = 4

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
    elif configuration.status == 3:
        configuration.name = message.text
        user_code = other_functions.generate_code()
        bot.send_message(message.chat.id, f"Ты успешно зарегистрировался в системе, вот твой уникальный код: {user_code}")
        bot.send_message(message.chat.id, "Не забудь подойти к организаторам :)")
        log_functions.log("Code generated", message.chat.id, user_code)
        configuration.status = 0
    elif configuration.status == 4:
        code = message.text
        log_functions.log("Code checking started", message.chat.id, code)
        bot.send_message(message.chat.id, db_functions.check_user_pay(code))
        configuration.status = 0
    elif configuration.status == 2:
        code = message.text
        bot.send_message(message.chat.id, db_functions.update_user_pay(code))



bot.polling(none_stop=True)
