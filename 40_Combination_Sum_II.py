class Solution:
  def combinationSum2(self, candidates, target):
    candidates = sorted(candidates)
    self.output = []
    self.backtracking([], 0, candidates, target)
    return self.output

  def backtracking(self, subset, start, candidates, target):
    if target == 0:
      self.output.append(list(subset))
    for idx in range(start, len(candidates)):
      if candidates[idx] > target:
        break
      if idx != start and candidates[idx-1] == candidates[idx]:
        continue
      subset.append(candidates[idx])
      self.backtracking(subset, idx+1, candidates, target-candidates[idx])
      subset.pop()

if __name__ == '__main__':
  so = Solution()
  candid = [10,1,2,7,6,1,5]
  target = 8
  print(so.combinationSum2(candid, target))