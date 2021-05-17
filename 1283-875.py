#1283 
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l, r = 1, max(nums)
        
        while l < r:
            mid = l + (r - l) // 2
            if sum(ceil(num/mid) for num in nums) > threshold:
                l = mid + 1
            else:
                r = mid
                
        return l
        
#875
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        
        while l < r:
            mid = l + (r - l) // 2
            if sum(ceil(pile/mid) for pile in piles) > h:
                l = mid + 1
            else:
                r = mid
                
        return l
            

