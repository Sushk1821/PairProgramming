# Convert roman to integer
def romanToInt(self, s: str) -> int:
    """
    Map a roman_int list. 
    """
    roman_to_int = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    roman = ["I","V","X","L","C","D","M"]
    int_num = 0
    for i in range(len(s)):
        if i == len(s)-1:
            int_num += roman_to_int[s[i].upper()]
            break
        if roman.index(s[i]) < roman.index(s[i+1]):
            int_num -= roman_to_int[s[i].upper()]
        else:
            int_num += roman_to_int[s[i].upper()]
        print(int_num)
    return int_num

# Convert integer to roman
def intToRoman(self, num: int) -> str:
    """
    Map a int_roman list. 
    """
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

