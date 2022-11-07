def export_func1(last_name):
    with open('database.txt', 'r', encoding='utf-8') as f:
        info_list = f.read().splitlines()
        for person in info_list:
            if last_name in person:
                with open('info1.txt', 'a', encoding='utf-8') as d:
                    d.write(person + '\n')


def export_func2(last_name):
    with open('database.txt', 'r', encoding='utf-8') as f:
        info_list = f.read().splitlines()
        for person in info_list:
            if last_name in person:
                person_list = person.split(" ")
                with open('info2.txt', 'a', encoding='utf-8') as d:
                    for i in person_list:
                        d.write(i + '\n')
                    d.write('\n')






