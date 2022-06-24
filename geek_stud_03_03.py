def my_fun(a, b, c):
    if a >= c and b >= c:
        return a + b
    elif a >= b and c >= b:
        return a + c
    else:
        return b + c


a = int(input('Вводим a'))
b = int(input('Вводим b'))
c = int(input('Вводим c'))
print(my_fun(a, b, c))
