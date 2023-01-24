class Solution:
    def fib(self, n: int) -> int:

        f0 = 0
        f1 = 1

        for i in range(n):
            f0, f1 = f1, f0 + f1
           
        return f0
