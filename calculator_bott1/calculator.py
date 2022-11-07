from fractions import Fraction


def calc1(text):
    lst = text.split()
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
        return 'Некорректный запрос!'


def calc2(text):
    lst = text.split()
    a = lst[0]
    left_value = Fraction(int(a[0: a.index('/')]), int(a[a.index('/') + 1:len(a)]))
    g = lst[2]
    right_value = Fraction(int(g[0: g.index('/')]), int(g[g.index('/') + 1:len(g)]))
    if lst[1] == '+':
        return left_value + right_value
    if lst[1] == '-':
        return left_value - right_value
    if lst[1] == '*':
        return left_value * right_value
    if lst[1] == '/':
        return left_value / right_value
    else:
        return 'Некорректный запрос!'






