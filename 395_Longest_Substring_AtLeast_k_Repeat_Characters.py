import collections
class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        lookup = collections.Counter(s)
        for c in lookup:
            if lookup[c] < k:
                return max(self.longestSubstring(t, k) for t in s.split(c))
        return len(s)

if __name__ == '__main__':
    s = "abacbbbc"
    S = Solution()
    print(S.longestSubstring(s,3))