class Solution(object):
    def decodingString(self, s):
        """
        :param s: str
        :return: str
        """
        stack_nums, stack_words, result, num = [],[],'',''
        for ch in s:
            if ch.isdigit():
                num += ch
            elif ch == '[':
                stack_nums.append(int(num))
                stack_words.append(result)
                result, num = '',''
            elif ch == ']':
                result = stack_words.pop() + stack_nums.pop()*result
            else:
                result += ch
        return result

if __name__ == '__main__':
    solution = Solution()
    print(solution.decodingString("2[abc]3[cd]ef"))