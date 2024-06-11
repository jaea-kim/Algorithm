class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for index, n in enumerate(nums):
            a = target - n
            if a in dic:
                return [index, dic[a]]
            dic[n] = index
        