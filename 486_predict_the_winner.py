class Solution:

  def predict_winner(self, array):
    # dynamic programming: O(n^2), O(n^2)
    #dp[i][j] represents the maximum points we can get from array[i:j]
    # a = array[i] + min(dp[i+2][j], dp[i+1][j-1])
    # b = array[j] + min(dp[i+1][j-1], dp[i][j-2])
    # dp[i][j] = max(a, b)
    def calculate_points(array):
      length = len(array)
      dp = [[0] * length for _ in range(length)]
      for gap in range(length):
        for j in range(gap, length):
          i = j-gap
          x = 0
          if (i+2) <= j:
            x = dp[i+2][j]
          y = 0
          if (i+1) <= (j-1):
            y = dp[i+1][j-1]
          z = 0
          if i <= j-2:
            z = dp[i][j-2]
          dp[i][j] = max(array[i]+ min(x,y), array[j]+min(y,z))
      return dp[0][length-1]
    return calculate_points(array)


  def predict_winner_recursion(self, array):

    def calculate_points(arr, start, end, sum):
      if start + 1== end:
        return max(arr[start], arr[end])
      a = sum - calculate_points(arr, start+1, end, sum-arr[start])
      b = sum - calculate_points(arr, start, end-1, sum-arr[end])
      return max(a,b)
    return calculate_points(array, 0 , len(array)-1, sum(array))

if __name__ == '__main__':
  so = Solution()
  array = [20, 30, 2, 2, 2, 10]
  print(so.predict_winner_recursion(array))