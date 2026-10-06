class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:   
        for i in range(1, len(nums)):
            while nums[i - 1] > nums[i] and i > 0:
                nums[i], nums[i - 1] = nums[i - 1], nums[i]
                i -= 1
            
        return nums