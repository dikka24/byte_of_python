shoplist = ['яблоко', 'манго', 'морковь', 'банан']

print('я должен сделать',len (shoplist), 'покупок')

print('Покупки: ', end = ' ')
for item in shoplist:
    print(item, end= ' ')

dika = ('риса')
print(f'\nТакже нужно купить {dika}.')
shoplist.append('рис')
print("Теперь мой список покупок таков: ", shoplist)


print('Отсортирую-ка я свой список')
shoplist.sort()
print('Отсортированный список покупок выглядит так: ', shoplist)

print(f'Первое что я должен купить это: {shoplist[0]}')
oldtime = shoplist[0]
del shoplist[0]
print(f'я купил {oldtime}')
print(f'Теперь мой список покупок:{shoplist}')