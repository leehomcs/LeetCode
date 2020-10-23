import collections
def findNumOfValidWords(words, puzzles):
  res = []
  cnt = collections.Counter(''.join(sorted(set(w))) for w in words)
  for p in puzzles:
    bfs = [p[0]]
    for c in p[1:]:
      bfs += [s + c for s in bfs]
    res.append(sum(cnt[''.join(sorted(s))] for s in bfs))
  return res


if __name__ == '__main__':
  words = ["aaaa", "asas", "able", "ability", "actt", "actor", "access"]
  puzzles = ["aboveyz", "abrodyz", "abslute", "absoryz", "actresz", "gaswxyz"]
  res = findNumOfValidWords(words, puzzles)
  print(res)