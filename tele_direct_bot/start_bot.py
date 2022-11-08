import telebot.types
from telebot import TeleBot
import import_
import read_
import add_


bot = TeleBot('5777629455:AAExmiMiL8udeDKB7tOqKhV1BTd244DCM6g')


@bot.message_handler(commands=['start'])
def first_message(message):
    bot.send_message(message.chat.id,
                     text=(f'ПУНКТЫ МЕНЮ: \n' '\n' '/read - просмотр записей\n' '/add - добавление записи\n'
                           '/export - экспорт\n' '/import - импорт\n' '/exit - выход из программы\n'                           
                           '\n'
                           'Введите пункт меню.'))


@bot.message_handler(commands=['read'])
def read_bot(message):
    bot.send_message(message.chat.id,
                     text=read_.read_func())


@bot.message_handler(commands=['add'])
def add_bot(message):
    bot.send_message(message.chat.id,
                     text='Выберете формат записи и соответствующую команду: \n /1 - ФИО номер комментарий в одну '
                          'строку, \n /2 - ФИО номер комментарий в три строки.\n')


@bot.message_handler(commands=['1'])
def one(message: telebot.types.Message):
    next_message = bot.send_message(chat_id=message.from_user.id, text='Укажите через пробел: ФИО номер комментарий:' )
    bot.register_next_step_handler(callback=new_one, message=next_message)


def new_one(message):
    add_.add_func(1, message.text)
    bot.send_message(chat_id=message.from_user.id, text='Готово')


@bot.message_handler(commands=['2'])
def two(message):
    next_message = bot.send_message(chat_id=message.from_user.id, text='Укажите с новой строки:\n ФИО\n номер\n комментарий\n' )
    bot.register_next_step_handler(callback=new_two, message=next_message)


def new_two(message):
    add_.add_func(0, message.text)
    bot.send_message(chat_id=message.from_user.id, text='Готово')


@bot.message_handler(commands=['export'])
def export_bot(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id,
                     text='Справочник можете скачать ниже')
    bot.send_document(chat_id=msg.from_user.id, document=open('database.txt', 'rb'))


# @bot.message_handler(commands=['export'])
# def export_bot(message):
#     bot.send_message(message.chat.id,
#                      text='Выберете формат записи и соответствующую команду: \n /one - ФИО номер комментарий в одну '
#                           'строку, \n /two - ФИО номер комментарий в три строки.\n')
#
#
# @bot.message_handler(commands=['one'])
# def one_export(message: telebot.types.Message):
#     next_message = bot.send_message(chat_id=message.from_user.id, text='Введите фамилию человека' )
#     bot.register_next_step_handler(callback=new_one_export, message=next_message)
#
#
# def new_one_export(message):
#     export_.export_func1(message.text)
#     bot.send_message(chat_id=message.from_user.id,
#                      text='Файл можете скачать тут')
#     bot.send_document(chat_id=message.from_user.id, document=open('info1.txt', 'rb'))
#
#
# @bot.message_handler(commands=['two'])
# def one_export(message: telebot.types.Message):
#     next_message = bot.send_message(chat_id=message.from_user.id, text='Введите фамилию человека')
#     bot.register_next_step_handler(callback=new_two_export, message=next_message)
#
#
# def new_two_export(message):
#     export_.export_func2(message.text)
#     bot.send_message(chat_id=message.from_user.id,
#                      text='Файл можете скачать тут')
#     bot.send_document(chat_id=message.from_user.id, document=open('info2.txt', 'rb'))


@bot.message_handler(commands=['import'])
def imp_bot(message):
    bot.send_message(message.chat.id,
                     text='Вы можете отправить боту текстовый файл с данными, которые необходимо внести в базу. '
                          'Тект должен быть в одном из двух форматов: \n 1. - В одну строку через пробел, например: '
                          'Зайцева Любовь 89230002234 Бухгалтер, \n 2. - В несколько строк, например:\nЗайцева Любовь\n'
                          '89230002234\nБухгалтер\n')


@bot.message_handler(content_types=['document'])
def import_bot(msg: telebot.types.Message):
    file = bot.get_file(msg.document.file_id)
    downloaded_file = bot.download_file(file.file_path)
    with open(msg.document.file_name, "wb") as f_out:
        f_out.write(downloaded_file)
    import_.import_data(msg.document.file_name)
    bot.send_message(chat_id=msg.from_user.id, text='Готово')



# @bot.message_handler(commands=['import'])
# def import_bot(message):
#     bot.send_message(message.chat.id,
#                      text='Выберете формат записи и соответствующую команду: \n /one_imp - ФИО, номер, комментарий в одну '
#                           'строку, \n /two_imp - ФИО, номер, комментарий в три строки.\n')
#
#
# @bot.message_handler(commands=['one_imp'])
# def one_import(message: telebot.types.Message):
#     next_message = bot.send_message(chat_id=message.from_user.id, text='Введите имя файла, из которого нужно сделать импорт' )
#     bot.register_next_step_handler(callback=new_one_import, message=next_message)
#
#
# def new_one_import(message):
#     import_.import_func1(message.text)
#     bot.send_message(chat_id=message.from_user.id, text='Готово')
#
#
# @bot.message_handler(commands=['two_imp'])
# def one_import(message: telebot.types.Message):
#     next_message = bot.send_message(chat_id=message.from_user.id,
#                                     text='Введите имя файла, из которого нужно сделать импорт')
#     bot.register_next_step_handler(callback=new_two_import, message=next_message)
#
#
# def new_two_import(message):
#     import_.import_func2(message.text)
#     bot.send_message(chat_id=message.from_user.id, text='Готово')


@bot.message_handler(commands=['exit'])
def exit_bot(message):
    bot.send_message(message.chat.id,
                     text="Goodbye!")


bot.polling()
