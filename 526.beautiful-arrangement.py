class Solution:
    def countArrangement(self, n: int) -> int:
        # backtracking
        self.res = 0
        nums = [0 for i in range(n + 1)]
        self.dfs(nums, 1, n)
        return self.res
        
    def dfs(self, nums, val, n):
        if val > n:
            self.res += 1
            return 
        
        for i in range(1, n + 1):
            if nums[i] == 0 and (val % i == 0 or i % val == 0):
                nums[i] = val
                self.dfs(nums, val + 1, n)
                nums[i] = 0
