class Solution:
    def isPalindrome(self, s: str) -> bool:
        string_len = len(s)
        i = 0
        c = string_len - 1

        while i < c and c > 0 and i < string_len:
            if not s[i].isalnum():
                i += 1
                continue
            elif not s[c].isalnum():
                c -= 1
                continue
            elif s[i].lower() != s[c].lower():
                return False
            i += 1
            c -= 1
        return True