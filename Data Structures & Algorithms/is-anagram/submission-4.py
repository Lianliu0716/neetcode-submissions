class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = {}
        for ch in s:
            count[ch] = count.get(ch, 0) + 1

        for ch in t:
            if count.get(ch, 0) == 0:   # ch 不存在,或已經扣光 → t 多了這個字元
                return False
            count[ch] -= 1

        return True   # 能走到這,長度又相等,必定全部歸零