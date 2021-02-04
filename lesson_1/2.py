a = None
while a != 0:
    a = int(input('Введите время в секундах: '))

    h = a // (60 * 60)

    ost = a - h * 60 * 60

    m = ost // 60

    s = ost - m * 60

    print(f'{str(h).zfill(2)}:{str(m).zfill(2)}:{str(s).zfill(2)}')
