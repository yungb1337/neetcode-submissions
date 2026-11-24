class Solution:
    def solve(self,st: str) -> dict:
        var = dict()
        for x in st:
            if x in var:
                var[x] += 1
            else:
                var[x] = 1
        return var


    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        
        if self.solve(s) == self.solve(t):
            return True
        else:
            return False