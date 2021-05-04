class Solution:
    def countSubstrings(self, s: str) -> int:
        cnt = 0
        n = len(s)
        dp = [[0]*n for _ in range(n)]
        
        for i in range(n):
            dp[i][i] = 1
            cnt += 1
            
        for col in range(1, n):
            for row in range(col):
                if col - row == 1 and s[row] == s[col]:
                    dp[row][col] = 1
                    cnt += 1
                    
                elif dp[row+1][col-1] == 1 and s[row] == s[col]:
                    dp[row][col] = 1
                    cnt += 1    
                    
        return cnt
