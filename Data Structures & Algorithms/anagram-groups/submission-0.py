class Solution:
    def anagram(self, strs):
        var = {}

        for x in strs:
            if x in var:
                var[x] += 1
            else:
                var[x] = 1

        return frozenset(var.items())

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for word in strs:
            key = self.anagram(word)

            if key in groups:
                groups[key].append(word)
            else:
                groups[key] = [word]

        return list(groups.values())