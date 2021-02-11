nums = [0, 1, 300, 7, 10, 2, 1, 30, 1, 500, 9]

new_nums = [el for i, el in enumerate(nums) if nums[i] > nums[i-1]]
print(new_nums)


