import telebot
from settings import BOT_TOKEN

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'hello'])
def send_message(message):
    bot.reply_to(message, "Hello Eugene Popov (lox)!")

@bot.message_handler(commands=['watch1', 'watch2'])
def send_watch(message):
    if message[0] == 'watch1':
        bot.send_photo('img/cat.jpg')
    elif message[0] == 'watch2':
        bot.send_photo('img/dog.jpg')
    
    

@bot.message_handler(commands=['read'])
def send_text(message):
    pass

@bot.message_handler(commands=['voice'])
def send_text(message):
    pass

bot.infinity_polling()