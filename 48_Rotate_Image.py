class Solution:
  def rotate(self, matrix):
    """
    Do not return anything, modify matrix in-place instead.
    """
    rows = len(matrix)
    cols = len(matrix[0])
    for i in range(rows // 2):
      for j in range(cols):
        matrix[i][j] = matrix[rows - i - 1][j]
    for i in range(rows):
      for j in range(i):
        if i == j:
          continue
        else:
          matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    return matrix

if __name__ == '__main__':
  so = Solution()
  mat = [[1,2,3],[4,5,6],[7,8,9]]
  print(so.rotate(mat))