

class RomanNumerals:
    @staticmethod
    def to_roman(val : int) -> str:
        conversion = {1000: 'M', 900:'CM', 500:'D', 400:'CD', 100:'C', 90:'XC', 50:'L', 40:'XL', 10:'X', 9:'IX', 5:'V', 4:'IV', 1:'I'}

        output = ''

        for check in conversion.keys():
            while val >= check:
                val -= check
                output += conversion[check]

        return output

    @staticmethod
    def from_roman(roman_num : str) -> int:
        twoLetters = {'CM':900, 'CD':400, 'XC':90, 'XL':40, 'IX': 9, 'IV':4}
        oneLetters = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}

        output = 0

        for check in twoLetters.keys():
            if check in roman_num :
                count = roman_num.count(check)

                output += twoLetters[check] * count

                roman_num = roman_num.replace(check, '')
        
        for check in oneLetters.keys():
            if check in roman_num :
                count = roman_num.count(check)

                output += oneLetters[check] * count
                
        return output
    

output1 = RomanNumerals.to_roman(1666)
output2 = RomanNumerals.from_roman('MDCLXVI')

print(output1, output2)