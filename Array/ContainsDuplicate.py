class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        a = set(nums)
        if len(nums)==len(a):
            return False
        else:
            return True
        