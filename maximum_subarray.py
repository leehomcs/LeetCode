def maxSubArray(nums):
  res = [0] * len(nums)
  res[0] = nums[0]
  for idx in range(1, len(nums)):
    res[idx] = max(nums[idx] + res[idx - 1], 0)
  # return max(res)

  j=k=0
  max_sum = res[0]
  for i in range(1,len(nums)):
    if res[i]>=max_sum:
      max_sum = res[i]
      k=i
    if res[i]==0 and i>=k:
      j=i+1
  return nums[j:k+1]

if __name__ == '__main__':
  # nums = [-2,1,-3,4,-1,2,1,-5,4]
  nums = [5,15,-30,10,-5,40,10]
  str = maxSubArray(nums)
  print(str)

