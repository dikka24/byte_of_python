number = 23 
running = True

while running:
    guess = int(input('Введите целое число: '))

    if guess == number:
        print('Поздравляю, вы угадали.')
        running = False 
    elif guess < number:
        print('Нет, загаданное число немного больше этого') 
    elif guess > number:
        print("Нет, загаданное число немного меньше этого.")
    else: 
        print("надо ввести число")    
else:
    print("Цикл закончен")        

print("Завершение.")  

    