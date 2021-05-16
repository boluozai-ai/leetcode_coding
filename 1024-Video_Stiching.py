class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        prev_end, right = -1, 0
        res = 0
        
        for s, e in sorted(clips):
            if s > right or right >= T:
                break
            if prev_end < s <= right:
                res += 1
                prev_end = right
            right = max(right, e)
            
        return res if right >= T else -1 
      
      
