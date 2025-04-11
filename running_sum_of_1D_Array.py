'''
Running Sum of 1D Array

'''
# LeetCode 1480
def running_sum(nums):
    result = []
    sum = 0
    for num in nums:
        sum += num
        result.append(sum)
    return result



# example usage
nums = [1,3,5,6,9,10]
print(running_sum(nums))