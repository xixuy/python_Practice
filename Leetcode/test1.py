"""
加一
不够完善
"""

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n=digits.pop()
        n+=1
        digits.append(n)
        print(digits)

a=Solution()
digits=[1,2,3]
a.plusOne(digits)