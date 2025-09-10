
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False

        s = 1  # 1 is always a proper divisor
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                s += i
                if i != num // i:  # add the complementary divisor
                    s += num // i

        return s == num     
