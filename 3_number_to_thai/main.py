"""
เขียบนโปรแกรมแปลงตัวเลยเป็นคำอ่านภาษาไทย

[Input]
number: positive number rang from 0 to 10_000_000

[Output]
num_text: string of thai number call

[Example 1]
input = 101
output = หนึ่งร้อยเอ็ด

[Example 2]
input = -1
output = number can not less than 0
"""


class Solution:
    thai_digits = ["", "หนึ่ง", "สอง", "สาม", "สี่", "ห้า", "หก", "เจ็ด", "แปด", "เก้า"]
    thai_units = ["", "สิบ", "ร้อย", "พัน", "หมื่น", "แสน", "ล้าน"]

    def number_to_thai(self, number: int) -> str:
        if number < 0:
            return "number can not less than 0"
        if number == 0:
            return "ศูนย์"
        
        return self.convert_number(number)
    
    def convert_number(self, number: int) -> str:
        parts = []
        million_unit = 1000000
        
        if number >= million_unit:
            millions = number // million_unit
            parts.append(self.convert_number(millions) + "ล้าน")
            number = number % million_unit
        
        parts.append(self.convert_small_number(number))
        return "".join(parts)
    
    def convert_small_number(self, number: int) -> str:
        if number == 0:
            return ""
        
        result = []
        unit_position = 0
        
        while number > 0:
            digit = number % 10
            if digit != 0:
                if unit_position == 0:
                    if digit == 1 and number > 10:
                        result.append("เอ็ด")
                    else:
                        result.append(self.thai_digits[digit])
                elif unit_position == 1:
                    if digit == 1:
                        result.append("สิบ")
                    elif digit == 2:
                        result.append("ยี่สิบ")
                    else:
                        result.append(self.thai_digits[digit] + "สิบ")
                else:
                    result.append(self.thai_digits[digit] + self.thai_units[unit_position])
            number //= 10
            unit_position += 1
        
        return "".join(reversed(result))


if __name__ == "__main__":
    solution = Solution()

    print(solution.number_to_thai(101))
    print(solution.number_to_thai(-1))   
    print(solution.number_to_thai(10020000))
    print(solution.number_to_thai(21))   
