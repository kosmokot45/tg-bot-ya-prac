from telebot import TeleBot, types, logger
import os
from settings import BOT_TOKEN, REP_LINK
from converter import Converter
import logging
import utils
import keyboards as kb

bot = TeleBot(BOT_TOKEN)

logging.basicConfig(filename='filename.log', level=logging.INFO,
                    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger()


@bot.message_handler(commands=['start', 'hello'])
def send_message(message):
    main_keyboard = kb.main_menu()
    bot.send_message(message.chat.id, f"Привет, {message.chat.first_name}!\n" +
                     "Меня зовут Евгений Попов и это мой телеграм бот по тестовому заданию для наставников подростков Яндекс Практикума!\n"
                     "Для управления ботом используй кнопки или команды в меню.\n"
                     "Также присутствует управление голосовыми командами. Полный список команд представлен в /help", reply_markup=main_keyboard)

@bot.message_handler(content_types=['voice'])
def get_audio_messages(message: types.Message):
    file_id = message.voice.file_id
    file_info = bot.get_file(file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    file_name = str(message.message_id) + '.ogg'
    name = message.chat.first_name if message.chat.first_name else 'No_name'
    logger.info(f"Chat {name} (ID: {message.chat.id}) download file {file_name}")
    with open(file_name, 'wb') as new_file:
        new_file.write(downloaded_file)
    converter = Converter(file_name)
    os.remove(file_name)
    message_text = converter.audio_to_text()
    del converter
    print(message_text)
    text_commands(message, message_text)

@bot.message_handler(commands=['cat', 'dog'])
def send_watch(message):
    if message.text.lower() == '/cat':
        with open('img/cat.jpg', 'rb') as file:
            bot.send_photo(message.chat.id, file)
    elif message.text.lower() == '/dog':
        with open('img/dog.jpg', 'rb') as file:
            bot.send_photo(message.chat.id, file)
      
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
                 'Получение ссылки на репозиторий - /site \n'+
                 'Большинство комманд доступны через меню, текст и голосовое сообщение.\n'+
                 'Это относится к следующему функционалу:\n'+
                 'Фотографии, последние селфи, фото из старшей школы. Пост о главном увлечении. Войсы. Первая любовь 😻\n'
                 'Например можно отправить в чат сообщение "Фотографии" или отправить такое же голосовое сообщение.\n'
                 'Так же можно выбрать эту команду через меню. \n' +
                 'Некоторые команды доступны по синонимичным словам, например "фотографии" - "фотки"\n'+
                 'Так же есть фото котика - /cat\n'+
                 'И фото собачки - /dog'
                 , reply_markup=keyboard
                 )

@bot.message_handler(content_types=['text'])
def text_commands(message, text = ''):
    if text != '':
        command = text.lower()
    else:
        command = message.text.lower()

    if command in utils.commands_photo:
        photo_keyboard = kb.photo_menu()
        bot.send_message(message.chat.id, 'Какие конкретно?', reply_markup=photo_keyboard)

    elif command in utils.commands_hobby:
        main_keyboard = kb.main_menu()
        bot.send_message(message.chat.id, utils.hobby, reply_markup=main_keyboard)

    elif command in utils.commands_voice:
        voice_keyboard = kb.voice_menu()
        bot.send_message(message.chat.id, 'Что хочешь услышать?', reply_markup=voice_keyboard)

    elif command in utils.commands_back:
        main_keyboard = kb.main_menu()
        bot.send_message(message.chat.id, 'Выберите кнопку или воспользуйтесь меню', reply_markup=main_keyboard)

    elif command in utils.commands_selfie:
        with open('img/self_1.jpg', 'rb') as file_1, open('img/self_2.jpg', 'rb') as file_2:
            bot.send_photo(message.chat.id, file_1)
            bot.send_photo(message.chat.id, file_2)

    elif command in utils.commands_school:
        with open('img/school_1.jpg', 'rb') as file_1, open('img/school_2.jpg', 'rb') as file_2:
            bot.send_photo(message.chat.id, file_1)
            bot.send_photo(message.chat.id, file_2)

    elif command in utils.commands_gpt:
        with open('audio/gpt_true.ogg', 'rb') as file:
            bot.send_voice(message.chat.id, file)

    elif command in utils.commands_sql:
        with open('audio/sql_true.ogg', 'rb') as file:
            bot.send_voice(message.chat.id, file)

    elif command in utils.commands_love:
        with open('audio/love_true.ogg', 'rb') as file:
            bot.send_voice(message.chat.id, file)
    else:
        bot.reply_to(message, f'Я еще не знаю такой команды :( - {command}')


bot.infinity_polling()