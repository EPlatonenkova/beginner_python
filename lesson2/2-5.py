my_list = [8, 5, 4, 2]
num = int(input("Введите число: "))
counter = 0
for i in my_list:
    if num >= i:
        my_list.insert(counter, num)
    elif num < i and counter+1 < len(my_list):
        counter += 1
        continue
    else:
        my_list.insert(counter, num)
        break
    counter += 1
print(my_list)
