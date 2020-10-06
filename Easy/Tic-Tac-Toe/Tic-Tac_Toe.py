def illustration():
    print(f'''---------
| {game[0][0]} {game[0][1]} {game[0][2]} |
| {game[1][0]} {game[1][1]} {game[1][2]} |
| {game[2][0]} {game[2][1]} {game[2][2]} |
---------''')


def check_coord():
    for _ in choice:
        if int(_) not in [1, 2, 3]:
            print('Coordinates should be from 1 to 3!')
            return True
    return False


game = [[' ' for i in range(3)] for j in range(3)]  # Создание представления поля для игры
illustration()
coord = {'11': [2, 0], '12': [1, 0], '13': [0, 0], '21': [2, 1], '22': [1, 1], '23': [0, 1], '31': [2, 2],
         '32': [1, 2], '33': [0, 2]}  # Словарь при помощи которого
count, c, Flag = 0, 1, True

while Flag:
    choice = input('Enter the coordinates:').replace(' ', '')
    try:
        if check_coord():  # Осуществляется проверка на входные данные. Если придут неверные числа,
            continue  # то функция вернет true и цикл начнется заново, если придут буквы,
    except ValueError:  # то сработает except и цикл начнется заново.
        print('You should enter numbers!')
        continue
    if game[coord[choice][0]][coord[choice][1]] == ' ':  # Проверка на пустую ячейку поля
        game[coord[choice][0]][coord[choice][1]] = 'X' if c % 2 != 0 else 'O'  # переменная c служит для понимания
        c += 1  # чей в данный момент ход. Так как X начинает первый, то для него соответствует нечетное c.
        illustration()
        variation_winning = [
            [game[0][0], game[0][1], game[0][2]],
            [game[1][0], game[1][1], game[1][2]],
            [game[2][0], game[2][1], game[2][2]],
            [game[0][0], game[1][0], game[2][0]],  # Массив данных при которых происходит выигрыш
            [game[0][1], game[1][1], game[2][1]],
            [game[0][2], game[1][2], game[2][2]],
            [game[0][0], game[1][1], game[2][2]],
            [game[0][2], game[1][1], game[2][0]]
        ]
    else:
        print('This cell is occupied! Choose another one!')
        continue
    for X_O in ['X', 'O']:  # Проверка того, что нет ли на поле выигрышной комбинации
        if any([variant.count(X_O) == 3 for variant in variation_winning]):
            print(X_O + ' wins')
            Flag = False
            break
        elif ' ' not in (game[0] + game[1] + game[2]):
            print('Draw')
            Flag = False
            break
