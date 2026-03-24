# Last updated: 24/03/2026, 22:38:55
class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.split()
        result=""
        for i in range(-1,-len(s)-1,-1):
            result+=s[i]
            result+=" "
        return result[:-1]
        