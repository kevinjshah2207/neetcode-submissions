class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        a = [0] * 26
        b = [0] * 26
        for i in range(len(s)):
            val_s = ord(s[i]) - ord('a')
            val_t = ord(t[i]) - ord('a')
            print(val_s, val_t)
            a[val_s] += 1
            b[val_t] += 1
        print(a)
        print(b)
        return a == b