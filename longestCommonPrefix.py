class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_str = min(strs)
        max_str = max(strs)
        res = ""

        for i in range(len(min_str)):
            if min_str[i] == max_str[i]:
                res += min_str[i]
            else :
                return res
        return res

or

class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        prefix = strs[0]
        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix
