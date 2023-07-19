from telebot import TeleBot, types
import requests
import time
import json
from settings import BOT_TOKEN, REP_LINK, YA_IAM_TOKEN

bot = TeleBot(BOT_TOKEN)
iam_key = YA_IAM_TOKEN

@bot.message_handler(commands=['start', 'hello'])
def send_message(message):
    bot.reply_to(message, f"Привет {message.chat.first_name}!")

@bot.message_handler(content_types=["voice"])
def voice_rec(message):
    file_info = bot.get_file(message.voice.file_id)
    file = requests.get('https://api.telegram.org/file/bot{0}/{1}'.format(BOT_TOKEN, file_info.file_path))
    
    POST = "https://transcribe.api.cloud.yandex.net/speech/stt/v2/longRunningRecognize"
    body ={
        "config": {
            "specification": {
                "languageCode": "ru-RU"
            }
        },
        "audio": {
            "uri": file
        }
    }

    header = {'Authorization': 'Bearer {}'.format(iam_key)}
    
    req = requests.post(POST, headers=header, json=body)
    data = req.json()
    print(data)
    id = data['id']
    while True:

        time.sleep(1)

        GET = "https://operation.api.cloud.yandex.net/operations/{id}"
        req = requests.get(GET.format(id=id), headers=header)
        req = req.json()

        if req['done']: break
        print("Not ready")
    print("Text chunks:")
    for chunk in req['response']['chunks']:
        print(chunk['alternatives'][0]['text'])
    bot.reply_to(req['response']['chunks'])

@bot.message_handler(commands=['cat', 'dog'])
def send_watch(message):
    if message.text.lower() == '/cat':
        with open('img/cat.jpg', 'rb') as file:
            bot.send_photo(message.chat.id, file)
    elif message.text.lower() == '/dog':
        with open('img/dog.jpg', 'rb') as file:
            bot.send_photo(message.chat.id, file)
      
@bot.message_handler(commands=['read'])
def send_text(message):
    pass

@bot.message_handler(commands=['voice'])
def send_voice(message):
    pass

@bot.message_handler(commands=['site'])
def send_site(message):
    bot.reply_to(message, REP_LINK)

@bot.message_handler(commands=['help'])
def send_help(message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(
        types.InlineKeyboardButton(
            'Связаться с автором', url='telegram.me/pohuelofmind'
        )
    )
    bot.send_message(message.chat.id, 
                 'Для получения ссылки на репозиторий - /site \n'+
                 'Хотите котю? - /cat \n'+
                 'Хотите доги? - /dog', reply_markup=keyboard
                 )

@bot.message_handler()
def send_unknow(message):
    bot.reply_to(message, 'Я еще не знаю такой команды :(')

bot.infinity_polling()