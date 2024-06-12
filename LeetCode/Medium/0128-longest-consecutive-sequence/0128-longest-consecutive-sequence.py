class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dic = {}
        INF = float("inf")

        for num in set(nums):
            dic[num] = INF
            if num - 1 in dic:
                dic[num - 1] = num
            if num + 1 in dic:
                dic[num] = num + 1

        answer = 0
        
        for n in dic.keys():
            if not n - 1 in dic:
                count = 1
                while True:
                    nextN = dic[n]
                    if not nextN == INF:
                        count+=1
                        n = nextN
                    else:
                        answer = max(answer, count)
                        break;


        return answer    
            
