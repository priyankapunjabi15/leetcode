class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        self.nums = nums
        self.target = target
        out = {}
        for i, num in enumerate(nums):
            n = target - num
            if n not in out:
                out[num] = i
            else:
                return [out[n], i]


