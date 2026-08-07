class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #set 基本上就是「只有 key、沒有 value 的 dict」
        num_set = set(nums)
        longest = 0

        for n in num_set:
            if n-1 not in num_set:
                length = 1
                while n + length in num_set:
                    length += 1
                longest = max(longest,length)

        return longest