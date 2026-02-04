def moveZeroes(self, nums):
        j=-1
        i=0
        for num in nums:
            if nums[i]== 0:
                j = i # j must be at zero always.
                break
            elif nums[i]!= 0: # when the element is non zero , swap with zero.
                swap(nums[i],num[j])
                j++
        return movezeroes(nums)
