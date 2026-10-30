nums = [ 2,2,1,2,3,1,2,5,4,3]

frequency = {}
for num in nums:
 if num in frequency:
    frequency[num] +=1
else:
  frequency[num] =1

print (frequency)
