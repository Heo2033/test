class Solution:
    def romanToInt(self, s: str) -> int:
        rim_number = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                      'C': 100, 'D': 500, 'M': 1000}

        norm_number: int = rim_number[s[len(s) - 1]]
        for i in range(len(s) - 1):
            if rim_number[s[i]] < rim_number[s[i + 1]]:
                norm_number -= rim_number[s[i]]
            else:
                norm_number += rim_number[s[i]]

        return norm_number


test = Solution()
print(test.romanToInt('III'))
print(test.romanToInt('IV'))
print(test.romanToInt('IX'))
print(test.romanToInt('LVIII'))
print(test.romanToInt('MCMXCIV'))
