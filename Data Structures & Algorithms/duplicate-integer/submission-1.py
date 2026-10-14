class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums)-1):
            next_num = nums[i+1]
            if(next_num == nums[i]):
                return True
        return False