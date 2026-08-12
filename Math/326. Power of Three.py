class Solution(object):
    def isPowerOfThree(self, n):
        return n in [3**x for x in range(21)]
        
        