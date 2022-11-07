def add_func(lot, data_for_file):
    if lot == 1:
        with open("database.txt", "a", encoding='utf-8') as f:
            f.write(f'\n{data_for_file}')
    else:
        data = data_for_file.split(", ")
        with open("database.txt", "a", encoding='utf-8') as f:
            f.write(f'\n{data[0]}, ')
        with open("database.txt", "a", encoding='utf-8') as f:
            f.write(f'\n{data[1]}, ')
        with open("database.txt", "a", encoding='utf-8') as f:
            f.write(f'\n{data[2]}, ')
            f.write('\n')



