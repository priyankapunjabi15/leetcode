class Solution:
    def isValid(self, s: str) -> bool:
        para = {")":"(", "]":"[", "}":"{"}
        #para = [('(',')'), ('{','}'), ('[',']')]        
        stack = []

        for char in s:
            if char in para:          # it's a closing bracket
                if not stack or stack[-1] != para[char]:
                    return False
                stack.pop()
            else:                      # it's an opening bracket
                stack.append(char)
        return not stack