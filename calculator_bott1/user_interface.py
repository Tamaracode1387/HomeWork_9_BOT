import telebot.types
from telebot import TeleBot
from calculator import calc1
from calculator import calc2
from logger import result_logger as write_log


bot = TeleBot('5650037558:AAGQXLntdvR05uAD4KZF1PKdckVAAH1SpwI')


@bot.message_handler(commands=['log'])
def hello(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id,
                     text='Лог программы\nкалькулятор')
    bot.send_document(chat_id=msg.from_user.id, document=open('log.csv', 'rb'))


@bot.message_handler(commands=['start'])
def first_command(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text="С какими числами будем работать? Введите 1 для работы с "
                                                    "комплексными числами, 2 - для работы с рациональными числами")
    bot.register_next_step_handler(callback=second_command, message=msg)


def second_command(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text=f"Вы ввели: {msg.text}")
    if msg.text == "1":
        bot.send_message(chat_id=msg.from_user.id,
                         text="Введите выражение из двух комплексных чисел через пробел, значение которого "
                              "необходимо найти, используйте формат: 3+2j + 3+2j")
        bot.register_next_step_handler(callback=result1, message=msg)
    elif msg.text == "2":
        bot.send_message(chat_id=msg.from_user.id,
                         text="Введите выражение из двух рациональных чисел через пробел, значение которого"
                              "необходимо найти, используйте формат: 5/11 * 5/11")
        bot.register_next_step_handler(callback=result2, message=msg)
    else:
        bot.send_message(chat_id=msg.from_user.id, text="Некорректный выбор, введите команду /start")
        bot.register_next_step_handler(callback=first_command, message=msg)


def result1(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text=calc1(msg.text))
    bot.register_next_step_handler(callback=write_log(msg.text), message=msg)


def result2(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text=calc2(msg.text))
    bot.register_next_step_handler(callback=write_log(msg.text), message=msg)


@bot.message_handler()
def echo(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text="Введите команду /start, чтобы начать новый расчет")


bot.polling()


