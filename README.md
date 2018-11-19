# DiscoBot
Here is Disco2018 registration bot for Telegram. We'll use this for signing up new guest on our event, that created
by Gravity Production.
The usage is pretty simple:
    User type "/start" and bot send a individual token to user. My script add this token to event database. When user
    payed for ticket, bot change user status in BD to "Payed" or to "1". On the event day operators check user token in
    event database and if user status is "Payed", person is allowed to go to the event.