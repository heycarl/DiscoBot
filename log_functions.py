import datetime
import configuration
import telebot

bot = telebot.TeleBot(configuration.token)
now = datetime.datetime.now()

def log(text, user_id, disco_id):
    print("------------------------------")
    ndt = now.strftime("%d-%m-%Y %H:%M")
    main_string = ndt + "\n" + 'result: ' + text + "\n"
    second_string = f"telegram id: {user_id}, disco id: {disco_id}"
    ready_string = main_string + second_string
    print(ready_string)
    print("------------------------------")
    bot.send_message(321965003, ready_string)

# log("123", "@keguser0", "321965003", "1645")