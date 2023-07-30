class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }

        number = 0
        prev = 0
        for i in reversed(s):
            current = roman[i]
            if current >= prev:
                number += current
            else:
                number -= current
            prev = current
        return number
        
# Example usage:
roman_numeral = "XIV"
solution = Solution()
result = solution.romanToInt(roman_numeral)
print(result)  # Output: 14
