class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        # Approach 2: two passes
        up, down = [0] * len(arr), [0] * len(arr)
        for i in range(1, len(arr)):
            if arr[i] > arr[i - 1]: 
                up[i] = up[i - 1] + 1

        for i in range(len(arr) - 2, -1, -1):
            if arr[i] > arr[i + 1]: 
                down[i] = down[i + 1] + 1

        #print([u + d + 1 for u, d in zip(up, down) if u and d])
        return max([u + d + 1 for u, d in zip(up, down) if u and d] or [0])        
        
        
        # Approach 1: one pass
#         n = len(arr)
#         res = 0
#         start = 0
        
#         while start < n:
#             end = start
#             if end + 1 < n and arr[end] < arr[end + 1]:
#                 while end + 1 < n and arr[end] < arr[end + 1]:
#                     end += 1   # set end as the peak 
                    
#                 if end + 1 < n and arr[end] > arr[end + 1]:
#                     while end + 1 < n and arr[end] > arr[end + 1]:
#                         end += 1
#                     res = max(res, end - start + 1)
                    
#             start = max(end, start + 1)
            
#         return res
