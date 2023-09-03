print("Цветочный магазин")
dict = {'Праздничный': ["Розы и тюльпаны", 50, 6], 'Романтический': ["Розы", 65, 7],
        'Похоронный': ["Хризантемы и гвоздики", 45, 4], }
while True:
    menu_point = int(input(
        "1 - Просмотр описания\n2 - Просмотр цены\n3 - Просмотр количества\n4 - Вся информация\n5 - Покупка\n6 - Выход\n"))
    if menu_point == 1:
        name = input("Введите название букета: ")
        try:
            print('Состав букета ', name, ':', dict[name][0])
        except KeyError:
            print("Не существует букета с таким названием")
    elif menu_point == 2:
        name = input("Введите название букета: ")
        try:
            print('Цена букета (в рублях) ', name, ':', dict[name][1])
        except KeyError:
            print("Не существует букета с таким названием")
    elif menu_point == 3:
        name = input("Введите название букета: ")
        try:
            print('Количество букетов ', name, ':', dict[name][2])
        except KeyError:
            print("Не существует букета с таким названием")
    elif menu_point == 4:
        for i in dict.items():
            print(i)
    elif menu_point == 5:
        name = input("Введите название букета: ")
        number = int(input("Введите количество букетов: "))
        try:
            if number > dict[name][2]:
                print("Недостаточно букетов в наличии")
            else:
                print('К оплате', number * dict[name][1], 'рублей. Для оплаты покупки нажмите 1: ')
                verif = int(input())
                if verif == 1:
                    dict[name][2] -= number
                    print("Спасибо за покупку")
                else:
                    print("Ладно")
        except KeyError:
            print("Не существует букета с таким названием")
    elif menu_point == 6:
        print("  До свидания")
        break
    else:
        print("Нет такого пункта меню")
