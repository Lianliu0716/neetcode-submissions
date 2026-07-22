class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        temp = {}

        for s in strs:
            sorted_text = "".join(sorted(s))
            if sorted_text not in temp:
                temp[sorted_text] = []
            temp[sorted_text].append(s)

        return list(temp.values())