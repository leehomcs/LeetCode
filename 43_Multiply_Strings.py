class Solution:
  def multiply(self, num1, num2):
    # return str(int(num1)*int(num2))
    i, j = len(num1) - 1, len(num2) - 1
    reminder = 0
    res = ''
    while i >= 0 or j >= 0 or reminder:
      sum_nums = int(num1[i]) * int(num2[j]) + reminder
      divd, reminder = sum_nums / 10, sum_nums % 10
      res = str(divd) + res
      i -= 1
      j -= 1
    return res

if __name__ == '__main__':
  so = Solution()
  num1, num2 = '2', '3'
  print(so.multiply(num1, num2))