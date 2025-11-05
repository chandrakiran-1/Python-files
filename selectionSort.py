nums = [5, 3, 8, 6, 7, 2]

for i in range(len(nums)):
    minpos = i           # assume current position is smallest
    for j in range(i+1, len(nums)):
        if nums[j] < nums[minpos]:
            minpos = j   # update smallest position
    nums[i], nums[minpos] = nums[minpos], nums[i]   # swap

print(nums)
