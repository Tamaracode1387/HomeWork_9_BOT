def read_func():
    with open('database.txt', 'r', encoding='utf-8') as f:
        info_list = f.read()
        return info_list

