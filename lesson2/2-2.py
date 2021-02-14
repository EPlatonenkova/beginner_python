my_list = list(input("Введите целые числа: "))
res = []
res = my_list
print(res)
n = 0
for i in range(int(len(res)/2)):

    res[n], res[n+1] = res[n+1], res[n]
    n += 2

print(res)



