def func_outrer():
    x = 2
    print('x равно', x )

    def func_inner():
        nonlocal x 
        x = 5 

    func_inner()
    print('Локальный х сменилось на', x )

func_outrer()        

'''когда мы находимся внутри func_inner, переменная x, определённая в первой строке func_outer находится ни в локальной области видимости (определение переменной не входит в блок func_inner), ни в глобальной области видимости (она также и не в основном блоке программы). Мы объявляем, что хотим использовать именно эту переменную x, следующим образом: nonlocal
x.
Попробуйте заменить «nonlocal x» на «global x», а затем удалить это зарезервированное слово, и пронаблюдайте за разницей между этими двумя
случаями'''