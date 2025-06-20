class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
    # initialize two pointers to start of list, i at k + 1
        k = 0
        i = 0
    # iterate one pointer over entire list
        while i < len(nums):
    # replace k with list at i
            nums[k] = nums[i]
    # if k is not equal to val
            if k != val:
                k = k + 1
        # advance k
    # advance i
        return k