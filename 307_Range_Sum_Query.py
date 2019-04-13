class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: None
        """
        self.nums[i] = val

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return sum(self.nums[i:j+1])


# Your NumArray object will be instantiated and called as such:
if __name__ == "__main__":
    # ["NumArray", "sumRange", "update", "sumRange"]
    # [[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]
    nums = [1,3,5]
    i = 0
    val = 2
    obj = NumArray(nums)
    print(obj)
    # obj.update(i,val)
    # param_2 = obj.sumRange(i,j)