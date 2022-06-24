
def my_func(x, y):
    try:
        x = float(x)
        y = int(y)
    except ValueError:
        print('Ошибка принимаются действительное число x и целое  число y')
        return
    if x <= 0 or y >= 0:
        print('принимаются положительное число x и отрицательное число y')
        return
    return x ** y


x = float(input("действительное положительное число x="))
y = int(input('целое отрицательное число y='))

print(round(my_func(x, y), 10))
