class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            # 格式：長度 + # + 字串本身
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while(i < len(s)):
            j = i
            while s[j] != "#":
                j += 1
            
            length = int(s[i:j])
            end = j+length+1
            string = s[j+1:end]
            res.append(string)
            i = end
        return res



            
