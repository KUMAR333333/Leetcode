class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        if n == 4:
            return False
        
        sum_of_squares = sum(int(digit) ** 2 for digit in str(n))
        return self.isHappy(sum_of_squares)

        
        
