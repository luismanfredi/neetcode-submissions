class Solution:
    def isPalindrome(self, s: str) -> bool:
        ns = s.lower()
        i, j = 0, len(s) - 1
        ans = True

        while i <= j:
            if ns[i].isalnum() is False:
                i += 1
                continue
            elif ns[j].isalnum() is False:
                j -= 1
                continue

            if ns[i] != ns[j]:
                ans = False
                break
            i += 1
            j -= 1

        return ans

        