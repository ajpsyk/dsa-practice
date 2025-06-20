class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # store the length
        length = len(nums)
        i = 0
        # iterate over nums
        while i < length:
            # push current number to end of nums
            nums.append(nums[i])
            i = i + 1
        # stop at length
        return nums
