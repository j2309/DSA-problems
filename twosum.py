class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)): # for first index number
            for j in range(i+1,len(nums)): # for second index number
                if nums[j] == target - nums[i]:
                    return [i,j]
        return []