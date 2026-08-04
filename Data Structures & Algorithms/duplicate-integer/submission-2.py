class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash = {}
        for n in nums:
            if n not in hash:
                hash[n] = 1
                continue
            return True
        return False