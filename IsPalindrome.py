Given a string s, return true if it is a palindrome, otherwise return false.

A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(filter(str.isalnum, s)).lower()
        print(s)

        i, j = 0, len(s) - 1 

        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True       
