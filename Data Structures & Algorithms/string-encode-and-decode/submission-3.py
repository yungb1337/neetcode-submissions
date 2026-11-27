class Solution:

    def encode(self, strs: List[str]) -> str:
        y = ""
        for x in strs:
            l = len(x)
            y = y+str(l)+"#"+str(x)
        return y

    def decode(self, s: str) -> List[str]:
        arr = []
        i = 0
        ns = ""
        while(i<len(s)):
            ns = ""
            while s[i]!="#":
                ns = str(ns) + str(s[i])
                i+=1
            ns = int(ns)
            if ns == 0:
                arr.append("")
                i=i+1
                continue
            slice = s[i+1 : i+1+ns]
            arr.append(slice)
            i = i+1+ns
        return arr

            





#    --->0#0#0#
# [hello, world]
# ---> Hello#

#use slicing