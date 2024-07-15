class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x = str(x)
        rev_str_x = str_x[::-1]
        if str_x == rev_str_x:
            return True
        return False


sol = Solution()

print(sol.isPalindrome(1512))
