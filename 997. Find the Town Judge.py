class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        Trusted = (n+1) * [0]

        for (a, b) in trust:
            Trusted[a] -= 1
            Trusted[b] += 1
                
        for i in range(1, len(Trusted)):
            if Trusted[i] == n-1:
                return i
            
        return -1

        
