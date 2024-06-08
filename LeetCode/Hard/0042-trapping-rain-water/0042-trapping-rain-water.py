class Solution:
    def trap(self, height: List[int]) -> int:
        answer = 0
        for i in range(1, len(height) - 1):
            maxL = max(height[:i])
            maxR = max(height[i + 1:])
            minH = min(maxL, maxR)
            if height[i] < minH:
                answer += minH - height[i]
              
        return answer