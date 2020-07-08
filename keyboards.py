from aiogram.types import ReplyKeyboardMarkup

def city():
    markup = ReplyKeyboardMarkup(True, True)
    markup.row('Бишкек', 'Ош')
    markup.row('Джалал Абад', 'Баткен')
    markup.row('Талас', 'Нарын')
    markup.row('Ысык-Кол')
    markup.row('Меню')

    return markup

def menu():
    markup = ReplyKeyboardMarkup(True, True)
    markup.row('Поиск универиситета', 'Поиск факультета')
    markup.row('Поиск специальности')
    markup.row('Контакты', 'Предметы для ОРТ')

    return markup