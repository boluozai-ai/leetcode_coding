# 198. House Robber
class Solution:
    def rob(self, nums: List[int]) -> int:
        # DP 
#         if not nums:
#             return 0
#         # base case
#         num_house = len(nums)
#         dp = [0] * (num_house+1)
#         dp[num_house] = 0
#         dp[num_house-1] = nums[num_house - 1]
        
#         # transition
#         for i in range(num_house - 2, -1, -1):
#             dp[i] = max(dp[i+1], dp[i+2] + nums[i])
            
#         return dp[0]
    
        # Optimized DP
        num_house = len(nums)
        rob_next_next = 0
        rob_next = nums[num_house-1]
        
        for i in range(num_house - 2, -1, -1):
            curr = max(rob_next, rob_next_next + nums[i])
            
            rob_next_next = rob_next
            rob_next = curr
            
        return rob_next       
      
      
# 213. House Robber II
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        return max(self.rob_helper(nums[:-1]), self.rob_helper(nums[1:]))
        
    def rob_helper(self, nums):
        num_house = len(nums)
        rob_next_next = 0
        rob_next = nums[num_house-1]
        
        for i in range(num_house - 2, -1, -1):
            curr = max(rob_next, rob_next_next + nums[i])
            
            rob_next_next = rob_next
            rob_next = curr
            
        return rob_next       
      
      
      
# 337. House Robber III
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        
        def rob_helper(root):
            if not root:
                # (rob, not_rob)
                return (0, 0)
            
            left = rob_helper(root.left)
            right = rob_helper(root.right)
            
            rob = root.val + left[1] + right[1]
            not_rob = max(left) + max(right)
            
            return (rob, not_rob)
        
        return max(rob_helper(root))
            


