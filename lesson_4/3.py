
nums = list(range(20, 240))
new_nums = [el for el in nums if el % 20 == 0 or el % 21 == 0]
print(new_nums)