class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        
        prime = [0] * n  # Array to track prime numbers
        
        for i in range(2, int(n ** 0.5) + 1):  
            if prime[i] == 0:  # If i is prime
                for j in range(i * i, n, i):
                    prime[j] = 1  # Mark multiples of i as non-prime
        
        # Count numbers that are still marked as prime
        return sum(1 for i in range(2, n) if prime[i] == 0)
