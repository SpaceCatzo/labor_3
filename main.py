n = int(input("Введите количество дисков: "))


def hanoi_towers(n, start, finish, middle):
    if n == 1:
        print(f"Переместить диск {n} с {start} на {finish}")
        return

    hanoi_towers(n - 1, start, middle, finish)

    print(f"Переместить диск {n} с {start} на {finish}")

    hanoi_towers(n - 1, middle, finish, start)


hanoi_towers(n, 'Начальная палка', 'Конечная палка', 'Средняя палка')
