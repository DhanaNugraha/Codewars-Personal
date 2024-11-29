sentence = "is2 Thi1s T4est 3a"

def order(sentence):
    sentence = sentence.split()

    def numFinder(word):
        for letter in word:
            if letter.isnumeric():
                return letter

    sentence.sort(key = numFinder)
    
    return ' '.join(sentence)

print(order(sentence))