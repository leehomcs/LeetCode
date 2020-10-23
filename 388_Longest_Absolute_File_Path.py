class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        maxlen = 0
        levels = {-1: 0}
        elements = input.split("\n")

        for e in elements:
            level = e.count("\t")
            levels[level] = levels[level - 1] + len(e) - level

            if '.' in e:
                maxlen = max(maxlen, levels[level] + level)
        return maxlen


if __name__ == "__main__":
    input = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
    s = Solution()
    print(s.lengthLongestPath(input))