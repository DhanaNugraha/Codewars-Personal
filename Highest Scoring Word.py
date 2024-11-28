x = 'what time are we climbing up the volcano'


def high(x):
    x = x.split()
    maxScore = 0
    finalWord = ""
    
    for word in x:

        currentScore = 0
        for letter in word:
            currentScore += ord(letter) - 96

        if currentScore > maxScore:
            maxScore = currentScore
            finalWord = word

    return finalWord

print(high(x))