roman = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}

def romanToInt(s):
    s = s.upper()
    value = 0
    for i in range(len(s)):
        if i > 0 and roman[s[i]] > roman[s[i-1]]:
            value += roman[s[i]] - 2 * roman[s[i-1]]
        else:
            value += roman[s[i]]
    return value

s = input("Enter a Roman numeral: ")
result = romanToInt(s)
print("The equivalent integer value is:", result)