nums = [1, 2, 2, 2, 3, 9, 10, 5, 5, 1]
new_nums = [el for el in nums if nums.count(el) ==1]

print(new_nums)


