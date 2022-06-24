def my_func():
    x = 0
    my_list = input('Вводим числа через пробел или Q,для выхода: ').upper().split()
    for i in my_list:
        if i == 'Q':
            return x, True
        try:
            x += int(i)
        except ValueError:
            pass
        return x, False


result = 0
while True:
    a, b = my_func()
    result += a
    print(result)
    if b:
        break
