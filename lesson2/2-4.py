a = input("Введите несколько слов, разделенных пробелами: ")
my_list = a.split()
print(my_list)

n = 0

for i in my_list:
    n += 1
    if len(i) > 10:
        print(f'{n} {i[:10]}')
    else:
        print(f'{n} {i}')


