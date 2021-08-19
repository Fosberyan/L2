while True:
    umonth = input('От 1 до 12: ')
    if umonth.isdigit() and 0 <= int(umonth) <= 12:
        season_1 = ['Зима', 'Весна', 'Лето', 'Осень']
        season_2 = {0: 'Зима', 1: 'Весна', 2: 'Лето', 3: 'Осень'}
        print(f'Это - {season_1[int(umonth) // 3]}')
        break
    else:
        print('Ошибка')




