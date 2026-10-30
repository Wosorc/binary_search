def input_num(name): # Защищённый ввод: повторяет запрос, пока не введено целое число.
    while True:
        try:
            return int(input(f"Введите {name}: "))
        except ValueError:
            print("Ошибка: необходимо ввести целое число!")


def binary_search(left, right, hidden): # Бинарный поиск hidden в [left; right]
    steps = 0

    while left <= right:
        steps += 1
        mid = (left + right) // 2 # середина текущего диапазона
        print(f"Шаг {steps}: left={left}, right={right}, mid={mid}", end=" -> ")

        if mid == hidden:
            print(f"{mid} = {hidden}, число найдено.")
            return steps
        elif mid < hidden:
            print(f"{mid} < {hidden}, ищем правее.")
            left = mid + 1 # отбрасываем левую половину вместе с mid
        else:
            print(f"{mid} > {hidden}, ищем левее.")
            right = mid - 1 # отбрасываем правую половину вместе с mid

    return -1 # диапазон исчерпан, числа нет


def start_program(): # Ввод и проверка данных, запуск поиска, вывод итога.
    while True:
        left = input_num("число начала сектора")
        right = input_num("число конца сектора")
        hidden = input_num("спрятанное число")

        if left > right:
            print("Неверно введённый сектор!")
        elif not (left <= hidden and hidden <= right):
            print("Спрятанное число вне диапазона!")
        else:
            break

    count = right - left + 1 # количество чисел в диапазоне
    max_steps = count.bit_length() # равно ceil(log2(count + 1))

    steps = binary_search(left, right, hidden)

    print(f"Число {hidden} найдено за {steps} шагов.")
    print(f"Теоретический максимум для диапазона из {count} чисел: {max_steps} шагов.")


if __name__ == "__main__":
    start_program()