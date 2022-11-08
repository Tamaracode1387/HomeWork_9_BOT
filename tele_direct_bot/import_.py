def import_data(file):
    with open(file, "r", encoding="utf-8") as f:
        data = f.read()
        data1 = data.split("\n")
        data2 = ' '.join(str(i) for i in data1)
        with open("database.txt", "a", encoding='utf-8') as f:
            f.write(f'{data2}')
            f.write('\n')





