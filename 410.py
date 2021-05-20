class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
      #Binary search
        low, high = max(nums), sum(nums)

        def valid(m, mid):
            curr_sum = 0; cnt = 1
            for num in nums:
                curr_sum += num
                if curr_sum > mid:
                    cnt += 1
                    curr_sum = num
                    if cnt > m:
                        return False
            return True
           
        while low < high:
            mid = (low + high) // 2
            if valid(m, mid):
                #high = valid(m, mid)
                high = mid
            else:
                low = mid + 1
        return low
    
