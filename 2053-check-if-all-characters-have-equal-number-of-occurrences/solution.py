class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        freq = dict()
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        # Check if all frequencies are the same
        return len(set(freq.values())) == 1
