class Solution:
  def countAndSay(self, n: int) -> str:
    #         import re

    #         currSeq = '1'
    #         pattern = r'((.)\2*)'

    #         for i in range(n-1):
    #             nextSeq = []
    #             for g1, g2 in re.findall(pattern, currSeq):
    #                 # append the pair of <count, digit>
    #                 nextSeq.append(str(len(g1)))
    #                 nextSeq.append(g2)
    #             # prepare for the next iteration
    #             currSeq = ''.join(nextSeq)

    #         return currSeq

    # Briefly, as explained in the description, reading the previous numbers one by one
    # and then make the next numbers. "left" has an index of repeated number(so "num[left]"
    # has the repeated number), and "right" has the first index that is different from repeated
    # number. "str(right - left)" means the number of repeated number.

    num = '1'
    for _ in range(n - 1):
      new_num = ''
      left, right = 0, 0
      while right < len(num):
        if num[right] != num[left]:
          new_num += str(right - left) + num[left]
          left = right
        right += 1
      new_num += str(right - left) + num[left]
      num = new_num
    return num

if __name__ == '__main__':
  so = Solution()
  for i in range(1,10):
    print(so.countAndSay(i))