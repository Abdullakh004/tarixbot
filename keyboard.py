from telebot import types


def generate_main_menu():
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
            knopka1 = types.KeyboardButton('Tarixiy davlatlar')
            knopka2 = types.KeyboardButton('Tarixiy shaxslar')
            keyboard.row(knopka1, knopka2)
            return keyboard

def sulolalar():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True , one_time_keyboard=True)
    knopka1 = types.KeyboardButton('Usmoniylar')
    knopka2 = types.KeyboardButton('Safaviylar')
    knopka3 = types.KeyboardButton('Shayboniylar')
    knopka4 = types.KeyboardButton('Ashtarxoniylar')
    knopka5 = types.KeyboardButton('Ahamoniylar')
    knopka6 = types.KeyboardButton('Umaviylar')
    knopka7 = types.KeyboardButton('Abbosiylar')
    knopka8 = types.KeyboardButton('Chingiziylar')
    back = types.KeyboardButton('🔙Orqaga')
    keyboard.row(knopka1, knopka2)
    keyboard.row(knopka3, knopka4)
    keyboard.row(knopka5, knopka6)
    keyboard.row(knopka7, knopka8)
    keyboard.row(back)
    return keyboard

def tarixiy_shaxslar():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    knopka1 = types.KeyboardButton('Amir Temur')
    knopka2 = types.KeyboardButton('Ismoil Safaviy')
    knopka3 = types.KeyboardButton('Yovuz Sulton Salim')
    knopka4 = types.KeyboardButton('Mehmed Fotih')
    knopka5 = types.KeyboardButton('Salohiddin Ayyubiy')
    knopka6 = types.KeyboardButton('Temur Malik')
    knopka7 = types.KeyboardButton('Horun ar-Rashid')
    knopka8 = types.KeyboardButton('Abdulmalik ibn Marvon')
    knopka9 = types.KeyboardButton('Umar ibn Abdulaziz')
    knopka10 = types.KeyboardButton('Hunyadi Yanosh')
    back = types.KeyboardButton("🔙Orqaga")
    keyboard.row(knopka1, knopka2)
    keyboard.row(knopka3, knopka4)
    keyboard.row(knopka5, knopka6)
    keyboard.row(knopka7, knopka8)
    keyboard.row(knopka9, knopka10)
    keyboard.row(back)
    return keyboard

def davlat_xaritasi():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    knopka1 = types.KeyboardButton('Safaviylar xaritasi')
    keyboard.row(knopka1)
    return keyboard
def davlat_xaritasi1():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    knopka1 = types.KeyboardButton('Usmoniylar xaritasi')
    keyboard.row(knopka1)
    return keyboard
def davlat_xaritasi2():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    knopka1 = types.KeyboardButton('Shayboniylar xaritasi')
    keyboard.row(knopka1)
    return keyboard
def davlat_xaritasi3():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    knopka1 = types.KeyboardButton('Ashtarxoniylar xaritasi')
    keyboard.row(knopka1)
    return keyboard
def davlat_xaritasi4():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    knopka1 = types.KeyboardButton('Ahamoniylar xaritasi')
    keyboard.row(knopka1)
    return keyboard
def davlat_xaritasi5():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    knopka1 = types.KeyboardButton('Umaviylar xaritasi')
    keyboard.row(knopka1)
    return keyboard
def davlat_xaritasi6():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    knopka1 = types.KeyboardButton('Abbosiylar xaritasi')
    keyboard.row(knopka1)
    return keyboard
def davlat_xaritasi7():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    knopka1 = types.KeyboardButton('Chingiziylar xaritasi')
    keyboard.row(knopka1)
    return keyboard





