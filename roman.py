'''
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
'''

def romanToInt(s: str) -> int:
    m = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    specials = {'I':['V','X'],
                'X':['L','C'],
                'C':['D','M']}

    counter = 0
    next_char = None
    for i in range(len(s)):
        char = s[i]
        next_char = s[i+1] if i+1 < len(s) else None

        if char in specials:
            if next_char in specials[char]:
                counter += -m[char]
            else:
                counter += m[char]
        else:
            counter += m[char]
    return counter

def main():
    # Test cases
    test_cases = {
        "III": 3,
        "LVIII": 58, 
        "MCMXCIV": 1994,
        "XIV": 14,
        "IX": 9,
        "IV": 4,
        "XXV": 25,
        "MMMCMXCIX": 3999,
    }
    
    for roman,expected in test_cases.items():
        result = romanToInt(roman)
        print(f"Roman numeral: {roman} expected: {expected} = actual: {result}")

if __name__ == "__main__":
    main()





