class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:   
        indexing_lenght = range(1, len(nums))

        for i in indexing_lenght:
            value_to_sort = nums[i]

            while nums[i - 1] > value_to_sort and i > 0:
                nums[i], nums[i - 1] = nums[i - 1], nums[i]
                i -= 1

        return nums