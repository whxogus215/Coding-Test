class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i in range(len(nums)):
            hashMap[nums[i]] = i
        for i in range(len(nums)):
            complement = target-nums[i]
            if complement in hashMap and hashMap[complement] != i:
                return [i, hashMap[complement]]