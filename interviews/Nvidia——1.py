# You are provided with a list of tasks. For each task, there can be zero/one/more dependencies. Before processing a task, all the
# pre-req tasks should be processed. Implement a program that can takes the task dependencies as input and returns an executable order
# of tasks. :
# T1 : T2, T3, T4
# T2: T3
# T3: <>
# T4: T3
# sample output: T3, T4, T2, T1

mat = [
  [0, 1, 1, 1],
  [0, 0, 1, 0],
  [0, 0, 0, 0],
  [0, 0, 0, 1]
]

neigh = [
  [0, 0, 0, 0],
  [1, 0, 0, 0],
  [0, 1, 1, 1],
  [1, 0, 0, 0]
]

from collections import deque

def is_valid(task, visited, mat):
  flag = 1
  for i in range(mat[0]):
    if mat[task-1][i] == 1 and i not in visited:
      flag = 0
  return flag

def bfs(s, mat, visited, res):

  queue = deque([s])
  while queue:
    task = queue.popleft()
    if task not in visited:
      visited.add(task)
      res.append(task)
      for col in range(len(neigh[0])):
        if neigh[task-1][col] == 1 and is_valid(task, visited, mat):
          queue.append(col-1)




def print_tasks(mat):
  candid_start = []
  rows = len(mat)
  cols = len(mat[0])
  for i in range(rows):
    flag = 0
    for j in range(cols):
      if mat[i][j] == 1:
        flag = 1
    if not flag:
      candid_start.append(i+1)

  visited = set()
  s = candid_start.pop()
  res = []
  bfs(s, mat, visited, res)