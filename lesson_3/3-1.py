def numbers():
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))

    while b == 0:
        b = int(input("Ноль вводить нельзя, делить на ноль нельзя \nВведите второе число: "))


    result = a / b
    return result


print(numbers())
