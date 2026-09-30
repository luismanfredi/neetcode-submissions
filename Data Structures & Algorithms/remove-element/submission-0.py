class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        counter = 0
        l = []

        for i in range(len(nums)):
            if nums[i] != val:
                counter += 1
                l.append(nums[i])

        for i in range(counter):
            nums[i] = l[i]

        return counter