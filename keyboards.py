from telebot import types

def main_menu():
    main_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    photo_btn = types.KeyboardButton('Фотографии')
    joy_btn = types.KeyboardButton('Увлечение')
    voice_btn = types.KeyboardButton('Войсы')
    main_keyboard.row(photo_btn, joy_btn)
    main_keyboard.row(voice_btn)
    return main_keyboard

def photo_menu():
    photo_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    last_photo_btn = types.KeyboardButton('Последние селфи')        
    school_photo_btn = types.KeyboardButton('Старшая школа')
    back_btn = types.KeyboardButton('Назад')
    photo_keyboard.row(last_photo_btn, school_photo_btn)
    photo_keyboard.row(back_btn)
    return photo_keyboard

def voice_menu():
    voice_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    gpt_voice_btn = types.KeyboardButton('Что такое GPT?')        
    sql_voice_btn = types.KeyboardButton('SQL и NoSQL')
    love_voice_btn = types.KeyboardButton('Первая любовь 😻')
    back_btn = types.KeyboardButton('Назад')
    voice_keyboard.row(gpt_voice_btn, sql_voice_btn)
    voice_keyboard.row(love_voice_btn, back_btn)
    return voice_keyboard