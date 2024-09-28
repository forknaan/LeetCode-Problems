# Furqan Saeed
# fsaeed@andrew.cmu.edu

#Two Sum
#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.
#You can return the answer in any order.

def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    num1index = 0
    num1index = 0
    for i in range(len(nums)):
        for j in range(len(nums)):
            if j != i:
                if nums[i] + nums[j] == target :
                    num1index = i
                    num2index = j
                    break
    final = [num1index, num2index]
    return final