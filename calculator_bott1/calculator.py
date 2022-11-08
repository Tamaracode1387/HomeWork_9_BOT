from fractions import Fraction


def calc1(text):
    lst = text.split()
    if len(lst) == 3:
        lst1 = [char for char in lst[0]]
        lst2 = [char for char in lst[2]]
        if lst1[0].isdigit() and lst1[2].isdigit() and lst2[0].isdigit() and lst2[2].isdigit() and lst1[3].isalpha() \
                and lst2[3].isalpha() and lst1[1] in ['+', '-', '/', '+'] and lst2[1] in ['+', '-', '/', '+'] and \
                lst2[0].isdigit() and lst2[2].isdigit() and lst[1] in ['+', '-', '/', '+']:
            a = lst[0]
            left_value = complex(a)
            g = lst[2]
            right_value = complex(g)
            if lst[1] == '+':
                return left_value + right_value
            if lst[1] == '-':
                return left_value - right_value
            if lst[1] == '*':
                return left_value * right_value
            if lst[1] == '/':
                return left_value / right_value
        else:
            return 'Неверный формат! начните заново!'
    else:
        return 'Неверный формат! начните заново!'


    # lst = text.split()
    # a = lst[0]
    # left_value = complex(a)
    # g = lst[2]
    # right_value = complex(g)
    # if lst[1] == '+':
    #     return left_value + right_value
    # if lst[1] == '-':
    #     return left_value - right_value
    # if lst[1] == '*':
    #     return left_value * right_value
    # if lst[1] == '/':
    #     return left_value / right_value
    # else:
    #     return 'Некорректный запрос!'


def calc2(text):
    lst = text.split()
    if len(lst) == 3:
        a = lst[0]
        a1 = a[0: a.index('/')]
        a2 = a[a.index('/') + 1:len(a)]
        g = lst[2]
        g1 = g[0: g.index('/')]
        g2 = g[g.index('/') + 1:len(g)]
        if a1.isdigit() and a2.isdigit() and g1.isdigit() and g2.isdigit() and lst[1] in ['+', '-', '/', '+']:
            left_value = Fraction(int(a1), int(a2))
            right_value = Fraction(int(g1), int(g2))
            if lst[1] == '+':
                return left_value + right_value
            if lst[1] == '-':
                return left_value - right_value
            if lst[1] == '*':
                return left_value * right_value
            if lst[1] == '/':
                return left_value / right_value
        else:
            return 'Неверный формат! начните заново!'
    else:
        return 'Неверный формат! начните заново!'








