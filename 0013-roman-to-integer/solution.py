class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        output = []
        
        for i in range(len(s)):
            if i < len(s) - 1 and roman[s[i]] < roman[s[i+1]]:
                out = -roman[s[i]]
                output.append(out)
                i += 2
            else: 
                out = roman[s[i]]
                output.append(out)
                i += 1
        return sum(output)

