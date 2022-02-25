def intToRoman(self, num: int) -> str:
    int_to_roman = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
    roman_num = ""
    while num > 0:
        if num in int_to_roman:
            roman_num += int_to_roman[num]
            break
        for int_num in int_to_roman:
            if int(num / int_num) > 0:
                roman_num += int_to_roman[int_num]
                num = num - int_num
                break
                
    return roman_num
