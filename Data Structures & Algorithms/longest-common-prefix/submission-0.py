class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = []

        for l in zip(*strs):
            if len(set(l)) == 1:
                result.append(l[0])
            else:
                break
        
        return "".join(result)