class Solution:
    def lenLongestFibSubseq(self, arr):
        s = set(arr)
        max_len, n = 0, len(arr)

        for i in range(n - 1):
            for j in range(i + 1, n):
                a, b, length = arr[i], arr[j], 2

                while a + b in s:
                    a, b = b, a + b
                    length += 1

                max_len = max(max_len, length)

        return max_len if max_len > 2 else 0
