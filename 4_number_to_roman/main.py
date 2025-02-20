"""
เขียบนโปรแกรมแปลงตัวเลยเป็นตัวเลข roman

[Input]
number: list of numbers

[Output]
roman_text: roman number

[Example 1]
input = 101
output = CI

[Example 2]
input = -1
output = number can not less than 0
"""


class Solution:

    def number_to_roman(self, number: int) -> str:
        if number <= 0:
            return "number can not less than 0"
        
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
        ]
        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
        ]
        
        roman_text = ""
        i = 0
        while number > 0:
            for _ in range(number // val[i]):
                roman_text += syb[i]
                number -= val[i]
            i += 1
        return roman_text


if __name__ == "__main__":
    solution = Solution()

    print(solution.number_to_roman(101))  
    print(solution.number_to_roman(1364)) 
    print(solution.number_to_roman(-1))