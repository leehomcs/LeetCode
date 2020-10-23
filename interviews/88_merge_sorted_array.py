class Solution:
  def merge(self, nums1, m, nums2, n):
    """
    Do not return anything, modify nums1 in-place instead.
    """
    idx_1 = idx_2 = 0
    ans = []
    if m == 0:
      return nums2
    if n == 0:
      return nums1
    if m == 0 and n == 0:
      return []
    del nums1[m:]
    while idx_1 < m and idx_2 < n:
      if nums1[idx_1] <= nums2[idx_2]:
        ans.append(nums1[idx_1])
        idx_1 += 1
      else:
        ans.append(nums2[idx_2])
        idx_2 += 1
    if idx_1 < m:
      ans.extend(nums1[idx_1:])
    if idx_2 < n:
      ans.extend(nums2[idx_2:])
    return ans


if __name__ == '__main__':
  nums1=[1, 2, 3, 0, 0, 0]
  m=3
  nums2=[2, 5, 6]
  n=3
  call = Solution()
  print(call.merge(nums1,m,nums2,n))