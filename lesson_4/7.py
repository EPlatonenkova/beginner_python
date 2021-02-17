def func(el):
    a = 1
    for i in range(1, el + 1):
        a *= i
        yield a


num = int(input("Введите число: "))
for x in func(num):
    print(x)
