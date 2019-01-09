print('Камень, ножницы, бумага')
import random
import string

while True:
    c = input('Хотите играть? Д/Н\n')
    if c in ('д','Д'):
        b = random.choice('кнб')
        a = str(input('Что выберешь:\nкамень (к), ножницы (н) или бумагу (б)?\n'))
        if a not in ('к','н','б'):
            print('Повторите ввод.')
        else:
            if a == b:
                print('Ничья.')
            else:
                if a == ('б') and b == ('н'):
                    print('Я выбрал ножницы.')
                    print('Ножницы режут бумагу.')
                    print('Я победил.')
                else:
                    if a == ('к') and b == ('н'):
                        print('Я выбрал ножницы.')
                        print('Камень ломает ножницы.')
                        print('Ты победил.')
                    else:
                        if a == ('к') and b == ('б'):
                            print('Я выбрал бумагу.')
                            print('Бумага накрыла камень.')
                            print('Я победил.')
                        else:
                            if a == ('н') and b == ('б'):
                                print('Я выбрал бумагу.')
                                print('Ножницы режут бумагу.')
                                print('Ты победил.')
                            else:
                                if a == ('н') and b == ('к'):
                                    print('Я выбрал камень.')
                                    print('Камень ломает ножницы.')
                                    print('Я победил.')
                                else:
                                    if a == ('б') and b == ('к'):
                                        print('Я выбрал камень.')
                                        print('Бумага накрыла камень.')
                                        print('Ты победил.')

    elif c in ('н','Н'):
        print('До свидания!')
        break

    else:
        print('Повторите ввод.')
