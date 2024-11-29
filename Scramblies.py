s1 = "cedewaraaossoqqyt"
s2 = "codewars"

def scramble(s1, s2):
    s2Counter = {}

    for letter in s2:
        if letter in s2Counter:
            s2Counter[letter] += 1

        else:
            s2Counter[letter] = 1

    for check in s2Counter.keys():
        if check not in s1:
            return False
        
        s1Counter = s1.count(check)

        if s1Counter < s2Counter[check]:
            return False

    return True

print(scramble(s1, s2))

