class Solution:
  def lengthLongestPath(self, input: str) -> int:
    ans = 0
    prefix = {-1: 0}
    for subd in input.split("\n"):  # sub-directory
      depth = subd.count("\t")
      prefix[depth] = prefix[depth - 1] + len(subd) - depth  # not including delimiter
      if "." in subd: ans = max(ans, prefix[depth] + depth)  # including delimiter
    return ans

if __name__ == '__main__':
  s = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
  so = Solution()
  print(so.lengthLongestPath(s))