class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash = {}
        for ch in s:
            hash[ch] = hash.get(ch,0) + 1
        
        for ch in t:
            if ch not in hash:
                return False 
            hash[ch] -= 1
            if hash[ch] == 0:
                del hash[ch]

        if len(hash) == 0:
            return True
        else:
            return False

