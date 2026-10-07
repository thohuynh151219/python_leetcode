"""
You are given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity

"""
class TwoSum:
    def __init__(self, nums, target):
        self.nums = nums
        self.target = target

    def index_of_sum(self):
        for i in range(len(self.nums) -1):
            for j in range(i + 1, len(self.nums)):
                sum =self.nums[i] + self.nums[j]
                if sum == self.target:
                    return [i, j]
        return -1
    
    def index_of_sum_1(self):
        dict_nums = {}
        
        for i in range(len(self.nums)):
            num = self.target - self.nums[i]
            if num in dict_nums:
                return [dict_nums[num], i]
            else:
                dict_nums.update({self.nums[i]:i})
            
        return -1
        
    
                

obj = TwoSum([2,7,11,15], 9)
print(obj.index_of_sum())
obj = TwoSum([3,2,4], 6)
print(obj.index_of_sum())
obj = TwoSum([3,3], 6)
print(obj.index_of_sum())
obj = TwoSum([3,2,3], 6)
print(obj.index_of_sum())
######################################
obj = TwoSum([2,7,11,15], 9)
print(obj.index_of_sum_1())
obj = TwoSum([3,2,4], 6)
print(obj.index_of_sum_1())
obj = TwoSum([3,3], 6)
print(obj.index_of_sum_1())
obj = TwoSum([3,2,3], 6)
print(obj.index_of_sum_1())