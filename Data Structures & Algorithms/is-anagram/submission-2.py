class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        stemp = list(s)
        ttemp = list(t)

        if len(stemp) != len(ttemp):
            return False

        for i in stemp:
            if i in ttemp:
                ttemp.pop(ttemp.index(i))
        
        if len(ttemp) == 0:
            return True
        else:
            return False
        