def add_func(lot, data_for_file):
    if lot == 1:
        with open("database.txt", "a", encoding='utf-8') as f:
            f.write(f'\n{data_for_file}')
    else:
        data1 = data_for_file.split("\n")
        data2 = ' '.join(str(i) for i in data1)
        with open("database.txt", "a", encoding='utf-8') as f:
            f.write(f'{data2}')
            f.write('\n')
        # with open("database.txt", "a", encoding='utf-8') as f:
        #     f.write(f'\n{data[1]}, ')
        # with open("database.txt", "a", encoding='utf-8') as f:
        #     f.write(f'\n{data[2]} ')
        #     f.write('\n')



