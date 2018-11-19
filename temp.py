user_code = other_functions.generate_code()
    bot.send_message(message.chat.id, user_code)
    log_functions.log("Code generated", message.chat.id, user_code)