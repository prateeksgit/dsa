def maxArea(height):
        left = 0
        right = len(height) - 1
        
        maxArea = 0
        while left < right:
            area = (right - left) * min(height[left], height[right])
            maxArea = max(area, maxArea)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return maxArea

if(__name__=="__main__"):
    nums=[1,8,6,2,5,4,8,3,7]
    print(maxArea(nums))
