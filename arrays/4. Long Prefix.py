from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if len(strs) == 1 or not strs[0]:
            return strs[0]

        lprefix = ''
        i = chi = 0
        char = strs[i][chi]

        while True:
            if not strs[i] or chi >= len(strs[i]) or strs[i][chi] != char:
                break

            if i == len(strs) - 1:
                lprefix += strs[i][chi]
                i, chi = 0, chi + 1
                if chi >= len(strs[i]):
                    break
                char = strs[i][chi]
                continue
            i += 1

        return lprefix


sol = Solution()
print(sol.longestCommonPrefix(["flower", "floght", "f"]))
print(sol.longestCommonPrefix(["fl", "fls"]))
