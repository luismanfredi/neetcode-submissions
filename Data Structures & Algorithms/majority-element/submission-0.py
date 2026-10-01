class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}

        for i in range(len(nums)):
            d[nums[i]] =  d.get(nums[i], 0) + 1

        major = max(d.values())

        return next((k for k, v in d.items() if v == major), None)