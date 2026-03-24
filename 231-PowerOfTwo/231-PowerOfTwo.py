# Last updated: 24/03/2026, 22:38:35
class Solution:
    val=1
    def isPowerOfTwo(self, n):
        while True:
            if n==1:
                return True
            if n<1:
                return False
            n=n/2
