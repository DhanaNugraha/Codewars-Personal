word = "Success" 

def duplicate_encode(word):
    output = ''
    word = list(word.lower())

    for i in range(len(word)):
        letter = word.pop(i)

        if letter in word:
            output += ')'

        else:
            output += '('
        
        word.insert(i, letter)

    return output

print(duplicate_encode(word))