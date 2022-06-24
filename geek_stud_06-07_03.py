def int_func(word):
    return word[0].upper() + word[1:].lower()


q = input('Вводим слово строчной латиницей: ').split()
for i, word in enumerate(q):
    if not word.isascii() or not word.isalpha() or not word.islower():
        print('Ошибочный ввод!')
    else:
        q[i] = int_func(word)

print(' '.join(q))



