from collections import Counter


class Solution:
  def frequencySort(self, s):
    # most_common = Counter(s).most_common()
    # res = ''
    # for idx in range(len(most_common)):
    #     res += most_common[idx][0] * most_common[idx][1]
    # return res

    if not s: return s

    # Determine the frequency of each character.
    counts = Counter(s)
    max_freq = max(counts.values())

    # Bucket sort the characters by frequency.
    buckets = [[] for _ in range(max_freq + 1)]
    for c, i in counts.items():
      buckets[i].append(c)

    # Build up the string.
    string_builder = []
    for i in range(len(buckets) - 1, 0, -1):
      for c in buckets[i]:
        string_builder.append(c * i)

    return "".join(string_builder)


if __name__ == '__main__':
  so = Solution()
  print(so.frequencySort('tree'))