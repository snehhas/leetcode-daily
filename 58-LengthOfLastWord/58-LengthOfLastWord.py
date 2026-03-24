# Last updated: 24/03/2026, 22:39:30
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        a=s.split()
        return len(a[-1])
        