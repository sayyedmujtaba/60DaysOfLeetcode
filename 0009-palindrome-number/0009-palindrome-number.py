class Solution:
    def isPalindrome(self, x: int) -> bool:
        s=str(x)
        palindrome=s[::-1]
        if palindrome == s:
            return True
        else:
            return False
        