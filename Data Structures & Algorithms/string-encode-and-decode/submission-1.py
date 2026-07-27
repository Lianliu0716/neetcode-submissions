class Solution:

    def encode(self, strs: List[str]) -> str:
        out = []
        for string in strs:
            for ch in string:
                out.append(str(ord(ch)))
                out.append("/")
            out.append("_")          # 不管空不空都要補
        return "".join(out)
        
    def decode(self, s: str) -> List[str]:
        ans = []
        for one_str in s.split("_")[:-1]:        # 丟掉尾巴空元素
            chars = one_str.split("/")[:-1]      # 同理
            ans.append("".join(chr(int(n)) for n in chars))
        return ans
