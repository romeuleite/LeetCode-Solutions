class Solution:
    def countOdds(self, low: int, high: int) -> int:

        cont = 0

        if (low % 2) != 0 or (high % 2) != 0:
            cont += 1

        cont += ((high - low) // 2)

        return cont
