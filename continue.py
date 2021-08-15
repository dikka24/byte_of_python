while True:
    s = input('Вводите что-нибудь: ')
    if s == 'выход':
        break
    if len(s) < 3:
        print('слишком мало')
        continue
    print('Введенная строка ддостаточной длины')

''' этой программе мы запрашиваем ввод со стороны пользователя, но обрабатываем введённую строку только если она имеет длину хотя бы в 3 символа.
Итак, мы используем встроенную функцию len для получения длины строки,
и если длина менее 3, мы пропускаем остальные действия в блоке при помощи оператора continue. В противном случае все остальные команды в цикле
выполняются, производя любые манипуляции, которые нам нужны.
Заметьте, что оператор continue также работает и с циклом for.'''