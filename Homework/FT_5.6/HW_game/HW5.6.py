# Создаем пустое поле 3x3
field = [[" " for _ in range(3)] for _ in range(3)]

# Функция для отображения поля
def display_field():
    for row in field:
        print("|".join(row))
        print("-" * 5)

# Функция для проверки выигрышных комбинаций
def check_win(player):
    for row in field:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(row[col] == player for row in field):
            return True
    if all(field[i][i] == player for i in range(3)) or all(field[i][2 - i] == player for i in range(3)):
        return True
    return False

# Основной цикл игры
current_player = "X"
while True:
    display_field()
    row = int(input(f"Игрок {current_player}, выберите строку (0, 1, 2): "))
    col = int(input(f"Игрок {current_player}, выберите столбец (0, 1, 2): "))

    # Проверка на корректность хода
    if field[row][col] != " ":
        print("Некорректный ход. Попробуйте еще раз.")
        continue

    # Устанавливаем символ игрока на поле
    field[row][col] = current_player

    # Проверяем, выиграл ли игрок
    if check_win(current_player):
        display_field()
        print(f"Игрок {current_player} победил!")
        break

    # Проверяем на ничью
    if all(cell != " " for row in field for cell in row):
        display_field()
        print("Ничья!")
        break

    # Смена игрока
    current_player = "O" if current_player == "X" else "X"
