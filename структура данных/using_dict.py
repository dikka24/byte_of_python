ab = {
    'swaroop'  : 'awarooop@gmail.com',
    'larry'    : 'larry@gmail.com',
    'Matsumto' : 'matzsumto@gmail.com'
}

print('adress of swaroop is: ', ab['swaroop'])

del ab['swaroop']

print ('В адресной книге {0}контактов'.format(len(ab)))

for name, adress in ab.items():
    print(f'контакт {name} c адресом {adress}')

ab['dalban'] = 'dalban@gamil.com'

if 'dalban' in ab:
    print("\nАдресс Dalban:", ab['dalban'])


'''Мы создаём словарьab2при помощи обозначений, описанных ранее. Затеммы обращаемся к парам ключ-значение, указывая ключ в операторе индек-сирования, которым мы пользовались для списков и кортежей. Как видите,синтаксис прост.Удалять пары ключ-значение можно при помощи нашего старого доброгооператораdel. Мы просто указываем имя словаря и оператор индексирова-ния для удаляемого ключа, после чего передаём это операторуdel. Для этойоперации нет необходимости знать, какое значение соответствует данномуключу.Далее мы обращаемся ко всем парам ключ-значение нашего словаря, исполь-зуя методitems, который возвращает список кортежей, каждый из которыхсодержит пару элементов: ключ и значение. Мы получаем эту пару и присваи-ваем её значение переменнымnameиaddressсоответственно в циклеfor..in,а затем выводим эти значения на экран в блоке for.Новые пары ключ-значение добавляются простым обращением к нужномуключу при помощи оператора индексирования и присваиванием ему неко-торого значения, как мы сделали для Guido в примере выше'''