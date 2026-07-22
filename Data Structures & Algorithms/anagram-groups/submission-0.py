class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        temp = defaultdict(list)

        for s in strs:
            ch = [0] * 26
            for c in s:
                ch[ord(c)-ord("a")] += 1
            temp[tuple(ch)].append(s)

        return list(temp.values())
