class Solution(object):
  def findWords(self, board, words):
    """
    :type board: List[List[str]]
    :type words: List[str]
    :rtype: List[str]
    """
    trie, self.ans = {}, set()
    rows, columns = len(board), len(board[0])
    for word in words:
      node = trie
      for letter in word:
        node = node.setdefault(letter, {})
      node['#'] = None

    def dfs(trie, x, y, comb):
      node = board[x][y]
      if node in trie:
        adj = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
        nxt = trie[node]
        board[x][y] = '.'
        comb = comb + node
        if '#' in nxt:
          self.ans.add(comb)
        for i, j in adj:
          if 0 <= i < rows and 0 <= j < columns:
            dfs(nxt, i, j, comb)
        board[x][y] = node

    for row in range(rows):
      for column in range(columns):
        dfs(trie, row, column, '')
    return list(self.ans)


if __name__ == '__main__':
  board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
  words = ["oath","pea","eat","rain"]
  find_words = Solution()
  print(find_words.findWords(board, words))
