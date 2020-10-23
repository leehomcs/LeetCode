class Solution(object):
  '''算法思路：
  也是先排序，然后两边加逼。
  '''

  def threeSumSmaller(self, nums, target):
    nums, n, r = sorted(nums), len(nums), 0
    for i, num in enumerate(nums):
      j, k, t = i + 1, n - 1, target - num
      while j < k:
        sum = nums[j] + nums[k]
        if sum < t:
          r += k-j
          j += 1
        else:
          k -= 1
    return r

if __name__ == '__main__':
  s = Solution()
  print(s.threeSumSmaller([-2, 0, 1, 3], 2))