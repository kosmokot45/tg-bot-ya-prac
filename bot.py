from telebot import TeleBot, types, logger
import os
from settings import BOT_TOKEN, REP_LINK, YA_IAM_TOKEN
from converter import Converter
# import logging

bot = TeleBot(BOT_TOKEN)
iam_key = YA_IAM_TOKEN

# logging.basicConfig(level=logging.INFO,
#                     format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
# logger = logging.getLogger()

def main_menu():
    main_keyboard = types.ReplyKeyboardMarkup()
    photo_btn = types.KeyboardButton('Фотографии')
    joy_btn = types.KeyboardButton('Увлечение')
    voice_btn = types.KeyboardButton('Войсы')
    main_keyboard.row(photo_btn, joy_btn)
    main_keyboard.row(voice_btn)
    return main_keyboard

def photo_menu():
    photo_keyboard = types.ReplyKeyboardMarkup()
    last_photo_btn = types.KeyboardButton('Последние селфи')        
    school_photo_btn = types.KeyboardButton('Старшая школа))')
    back_btn = types.KeyboardButton('Назад')
    photo_keyboard.row(last_photo_btn, school_photo_btn)
    photo_keyboard.row(back_btn)
    return photo_keyboard


@bot.message_handler(commands=['start', 'hello'])
def send_message(message):
    main_keyboard = main_menu()
    bot.send_message(message.chat.id, f"Привет {message.chat.first_name}!", reply_markup=main_keyboard)
    # bot.register_next_step_handler(message, on_click)

@bot.message_handler(content_types=['text'])
def text_commands(message):
    if message.text == 'Фотографии':
        photo_keyboard = photo_menu()
        bot.send_message(message.chat.id, 'Какие конкретно?', reply_markup=photo_keyboard)
    elif message.text == 'Увлечение':
        main_keyboard = main_menu()
        bot.send_message(message.chat.id, 'Люблю пирожки', reply_markup=main_keyboard)
    elif message.text == 'Войсы':
        main_keyboard = main_menu()
        bot.send_message(message.chat.id, 'Ща расскажу')
    elif message.text == 'Назад':
        main_keyboard = main_menu()
        bot.send_message(message.chat.id, 'Выберите кнопку или воспользуюйтесь меню', reply_markup=main_keyboard)
    else:
        bot.reply_to(message, 'Я еще не знаю такой команды :(')


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
    bot.send_message(message.chat.id, message_text, reply_to_message_id=message.message_id)


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

# @bot.message_handler()
# def send_unknow(message):
#     bot.reply_to(message, 'Я еще не знаю такой команды :(')


bot.infinity_polling()