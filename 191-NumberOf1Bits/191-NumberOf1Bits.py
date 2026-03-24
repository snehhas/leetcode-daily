# Last updated: 24/03/2026, 22:38:48
class Solution(object):
    def hammingWeight(self, n):
        set_bit_count = 0
        while n != 0:
            n &= (n - 1)
            set_bit_count += 1
        return set_bit_count
        