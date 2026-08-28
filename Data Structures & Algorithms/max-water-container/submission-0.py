class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        best = 0

        while left < right: 
            width = right-left
            height = min(heights[left],heights[right])
            area = width*height
            best = max(best,area)

            # need to move smaller one as per hint
            if height == heights[left]:
                left+=1
            elif height == heights[right]:
                right-=1
        
        return best
