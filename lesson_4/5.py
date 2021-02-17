
from functools import reduce

nums = range(100,1001)
new_nums = [el for el in nums if el %2 == 0]
print(f'Четные числа : {new_nums}')
result = reduce(lambda x,y: x*y, new_nums)
print(f'Произведение всех чисел из списка: {result}')
