class Solution:
  def removeSubfolders(self, folder):
    # brute force
    ans = []
    for i in range(len(folder)):
      if not folder[i]:
        continue
      path_i = folder[i].split('/')
      path_i_str = ''.join(path_i[1:])
      for j in range(i, len(folder)):
        path_j = folder[j].split('/')
        path_j_str = ''.join(path_j[1:])
        if path_i_str in path_j_str:
          folder[j] = ""
    for i in range(len(folder)):
      if folder[i] != "":
        ans.append(folder[i])
    return ans


if __name__ == '__main__':
  s = Solution()
  folders = ["/a","/a/b","/c/d","/c/d/e","/c/f"]
  print(s.removeSubfolders(folders))