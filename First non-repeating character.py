s = 'sTreSS'

def first_non_repeating_letter(s):
    lowerS = list(s.lower())
    s = list(s)

    for i in range(len(lowerS)):
        letter = lowerS.pop(i)

        if letter not in lowerS:
            return s[i]

        lowerS.insert(i, letter)

    return ''

print(first_non_repeating_letter(s))