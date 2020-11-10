from collections import deque, defaultdict
class Solution:
  def killProcess(self, pid, ppid, kill):
    lookup = defaultdict(list)
    for id, p in enumerate(ppid):
      lookup[p].append(pid[id])
    res = []
    queue = deque([kill])
    while queue:
      p_id = queue.popleft()
      res.append(p_id)
      queue.extend(lookup[p_id])
    return res

if __name__ == '__main__':
  so = Solution()
  pid = [1,2,3, 4, 5]
  ppid = [0,1,1,1,1]
  kill = 1
  print(so.killProcess(pid, ppid, kill))