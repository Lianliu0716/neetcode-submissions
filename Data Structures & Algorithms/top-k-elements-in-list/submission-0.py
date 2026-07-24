class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = {}
        for i in nums:
            if i not in hash:
                hash[i] = 0
            hash[i] += 1

        hash = dict(sorted(hash.items(), key=lambda x:x[1], reverse=True))
        top_2_keys = list(hash.keys())[:k]
        return top_2_keys

