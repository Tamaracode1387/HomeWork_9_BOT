from datetime import datetime as dt


def result_logger(text):
    lst = text.split()
    data_str = f'{str(lst[0])} {str(lst[1])} {str(lst[2])}'
    fixtime = dt.now().strftime('%H:%M')
    with open('log.csv', 'a', encoding='UTF-8') as file:
        file.write('{}; операция : {} \n'.format(
            fixtime, data_str))


# def result_logger(data, result):
#     left_value, oper, right_value = data
#     data_str = f'{str(left_value)} {oper} {str(right_value)}'
#     time = dt.now().strftime('%H:%M')
#     # print('{}; операция : {} результат : {}\n'.format(time, data_str, data))
#     with open('log.csv', 'a', encoding='UTF-8') as file:
#         file.write('{}; операция : {} результат :{}\n'.format(time, data_str, result))
