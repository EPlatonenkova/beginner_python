def my_func():
    sum = 0
    char = ' '
    while char != '/':
        numbers = input("Введите числа через пробел ")
        print(numbers)
        text = numbers.split()  # [1,2,3,4,5]
        for i in text:
            if i == '/':
                return
            else:
                sum += int(i)
        print(sum)


my_func()




