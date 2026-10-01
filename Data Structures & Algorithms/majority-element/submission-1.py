class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        possible_num = None
        counter = 0

        for num in nums:
            if counter == 0:
                possible_num = num

            counter += (1 if num == possible_num else -1)

        
        return possible_num