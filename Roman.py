def romanToInt(self, s: str) -> int:
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
