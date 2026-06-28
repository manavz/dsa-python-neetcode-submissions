class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        l = 0
        r = len(nums) - 1
        maxSum = 0

        while l < r:
            maxSum = nums[l] + nums[r]
            if maxSum == target:
                return [l, r]

            elif maxSum > target:
                r -= 1
            else:
                l += 1

        hash_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in hash_map:
                return [hash_map[complement], i]
            hash_map[num] = i