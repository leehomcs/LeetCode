import collections
class gameoflife:
  def gameOfLifeInfinite(self, live):
    ctr = collections.Counter((I, J)
                              for i, j in live
                              for I in range(i - 1, i + 2)
                              for J in range(j - 1, j + 2)
                              if I != i or J != j)
    return {ij for ij in ctr if ctr[ij] == 3 or ctr[ij] == 2 and ij in live}

  def gameOfLife(self, board):
    """
    Do not return anything, modify board in-place instead.
    """
    live = {(i, j) for i, row in enumerate(board) for j, live in enumerate(row) if live}
    live = self.gameOfLifeInfinite(live)
    for i, row in enumerate(board):
      for j in range(len(row)):
        row[j] = int((i, j) in live)


if __name__ == '__main__':
  live = [(1,0), (0,3), (100,4), (10,4), (7,400)]
  game = gameoflife()
  live_res = game.gameOfLifeInfinite(live)
  for i,j in live_res:
    print(str(i) + ' ' +str(j))