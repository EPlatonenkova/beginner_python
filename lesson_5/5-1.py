f = open('file_one.txt', 'w')
data = 1
while data != "":
    data = (input("Введите данные "))
    if data != "":
        f.write(f'{data}\n')
    else:
        print("Работа с фаулом закончена")


f.close()