class Solution:
    def isPalindrome(self, x: int) -> bool:
        xlist = list(str(x))
        xlist_rev = xlist[::-1]
        return xlist == xlist_rev
