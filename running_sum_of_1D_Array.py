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

# optimize the time and space complexity
def running_sum_1(nums):
    for i in range(1, len(nums)):
        nums[i] += nums[i - 1]
    return nums



# example usage
nums = [1,3,5,6,9,10]
print(running_sum(nums))

nums_1 = [1,3,5,6,9,10]
print(running_sum_1(nums_1))