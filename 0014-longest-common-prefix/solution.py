class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = os.path.commonprefix(strs)
        return result
