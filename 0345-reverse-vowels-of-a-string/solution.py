class Solution:
    def reverseVowels(self, s: str) -> str:
        S = list(s)
        l, r = 0, len(S) - 1
        vowels = set('aeiouAEIOU')

        while l < r:
            while l < r and S[l] not in vowels:
                l += 1
            while l < r and S[r] not in vowels:
                r -= 1
            
            # Swap vowels
            S[l], S[r] = S[r], S[l]
            l += 1
            r -= 1

        return "".join(S)


