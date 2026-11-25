class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        var = {}

        for x in range(len(nums)):
            y = target - nums[x]

            if y in var:
                return [var[y],x]
            var[nums[x]] = x
            
