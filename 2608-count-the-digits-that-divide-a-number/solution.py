class Solution:
    def countDigits(self, num: int) -> int:
        count = 0
        for d in str(num):  # iterate over each digit as a string
            if num % int(d) == 0:  # check if digit divides num
                count += 1
        return count
