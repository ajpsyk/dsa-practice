class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # nums = [0,0,1,1,1,2,2,3,3,4]
        # solution where we can iterate once?
        # first pointer and "counter" pointer on the index 0 number
        # second "counter" pointer on the index 1 number
        # if different, advance counter, make counter value = interator value
        # advance iterator
        k = 0
        i = 0
        while i < len(nums):
            if nums[k] != nums[i]:
                k = k + 1
                nums[k] = nums[i]
            i = i + 1
        return k + 1