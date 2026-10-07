class Solution:
    def sortColors(self, nums: List[int]) -> None:
        for i in range(1, len(nums)):
            value_to_sort = nums[i]

            while nums[i - 1] > value_to_sort and i > 0:
                nums[i], nums[i - 1] = nums[i - 1], nums[i]
                i -= 1
            