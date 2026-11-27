class Solution:
    def hash1(self,arr):
        var = {}
        for x in arr:
            if x not in var:
                var[x] = 1
            else:
                var[x]+=1
        return var
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ls = [[] for _ in range (len(nums)+1)]
        var = self.hash1((nums))
        t = []
        for x,y in var.items():
            ls[y].append(x)
        for z in range(len(ls)-1,0,-1):
            if ls[z] is not None:
                
                for q in ls[z]:
                    t.append(q)
                    k = k-1
                if k == 0:
                    return t



        