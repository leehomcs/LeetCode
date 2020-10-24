class Solution:
  def numDistinctIslands2(self, grid):

    def canonical(shape):

      def encode(shape):
        x, y = shape[0]
        # string = "".join(str(i - x) + ':' + str(j - y) for i, j in shape)
        udpated_list = [(i-x, j-y) for i, j in shape]
        return str(udpated_list)

      shapes = [[(a * i, b * j) for i, j in shape] for a, b in ((1, 1), (1, -1), (-1, 1), (-1, -1))]
      shapes += [[(j, i) for i, j in shape] for shape in shapes]
      res = [encode(sorted(shape)) for shape in shapes]
      return min(res)

    def dfs(grid, i, j, shape):
      if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or grid[i][j] != 1:
        return
      grid[i][j] = 0
      shape.append((i, j))
      dfs(grid, i+1, j, shape)
      dfs(grid, i-1, j, shape)
      dfs(grid, i, j-1, shape)
      dfs(grid, i, j+1, shape)

    islands = set()
    for row in range(len(grid)):
      for col in range(len(grid[0])):
        if grid[row][col] == 1:
          shape = []
          dfs(grid, row, col, shape)
          islands.add(canonical(shape))
    return len(islands)

if __name__ == '__main__':
    solution = Solution()
    grid = [[1,1,0,0,0],[1,0,0,0,0],[0,0,0,0,1],[0,0,0,1,1]]
    print(solution.numDistinctIslands2(grid))