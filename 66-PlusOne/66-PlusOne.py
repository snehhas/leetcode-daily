# Last updated: 24/03/2026, 22:39:28
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Convert the list of digits to a string
        c = "".join(str(digit) for digit in digits)
        
        # Convert the string to an integer and add one
        c = int(c) + 1
        
        # Convert the result back to a list of integers
        return [int(i) for i in str(c)]
