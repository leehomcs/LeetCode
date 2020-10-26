class Solution:
  def maximalSquare(self, matrix):
    if not matrix:
      return 0
    res = 0
    dp = [[0] * len(matrix[0]) for _ in range(len(matrix))]
    for i in range(len(matrix)):
      for j in range(len(matrix[0])):
        if matrix[i][j] == '1':
          dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
          res = max(res, dp[i][j])
    return res ** 2


if __name__ == '__main__':
  so = Solution()
  mat = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
  print(so.maximalSquare(mat))