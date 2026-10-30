nums = [12,45,780,23,4]


maximum = nums[0]
minimum = nums[0]


for i in nums:
    if i > maximum:
        maximum = i
    elif i < minimum:
        minimum = i


print("Maximum number = ", maximum)
print("Minimum number = ", minimum)