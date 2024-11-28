string_ = "This website is for losers LOL!"

def disemvowel(string_):
    vowels = {'a', 'i', 'u', 'e', 'o' }
    newStr = ''

    for str in string_:
        if str.lower() in vowels:
            continue
        else:
            newStr += str

    string_ = newStr
    
    return string_

print(disemvowel(string_))