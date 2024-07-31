class Solution:
    def check(self, nums: List[int]) -> bool:
        sortedNums = sorted(nums)
        for i in range(len(nums)):
            if(nums == sortedNums):
                return True
            tempNum = nums.pop(0)
            nums.append(tempNum)
        return False
    