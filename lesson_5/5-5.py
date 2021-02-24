f = open("nums.txt", "w+")

nums = input('Введите цифры через пробел = ')
f.writelines(nums)
f.close()
f = open("nums.txt", "r")
my_numb = f.read()
res = my_numb.split()

print(sum(map(int, res)))
f.close()
