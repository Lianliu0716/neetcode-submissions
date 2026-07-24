class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        freq = [[] for i in range(len(nums)+1)]

        for n in nums:
            counts[n] = counts.get(n,0) + 1
        for n, c in counts.items():
            freq[c].append(n)
        
        ans = []
        for f in range(len(freq)-1,0,-1):
            for item in freq[f]:
                ans.append(item)
                if len(ans) == k:
                    return ans
        
