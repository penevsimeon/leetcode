class Solution:
    def romanToInt(self, s: str) -> int:

        roman_dict = {"I": 1,
                      "V": 5,
                      "X": 10,
                      "L": 50,
                      "C": 100,
                      "D": 500,
                      "M": 1000}

        total = 0

        for i in range(len(s) - 1):
            if roman_dict[s[i]] < roman_dict[s[i + 1]]:
                total -= roman_dict[s[i]]
            else:
                total += roman_dict[s[i]]

        return total + roman_dict[s[-1]]

    # IX
    # XI

sol = Solution()
print(sol.romanToInt('IX'))
