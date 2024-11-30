# make a tree for input if combination is found, return the rank

word = 'BOOKKEEPER'
# try ABB

def list_position(word):
    import math
    letterList = sorted(set(word))
    word = list(word)
    rank = 0
    print(sorted(word))

    # Calc the amount of duplicates for each letter
    letterAmount = {}

    for i in range(0, len(word)): 
        if word[i] in letterAmount:
            letterAmount[word[i]] += 1
        
        else:
            letterAmount[word[i]] = 1
    
    print(letterAmount)

    # traverse check 1 by 1
    for i in range(len(word)):
        print(i)
        # Decision tree but cutting branch if letter not appropriate
        for checkLetter in letterList:
            if letterAmount[checkLetter] == 0:
                continue

            curWord = word[i]

            if curWord == checkLetter:
                letterAmount[curWord] -= 1
                print(checkLetter, letterAmount, 'correct')
                break
            
            # calc how much branch we skipped
            else: 
                # temp letter amount for skipped branch with the head check letter
                print(letterAmount, 'this is letter amount', i)
                tempLetterAmount = letterAmount.copy()
                tempLetterAmount[checkLetter] -= 1

                print('this is temp letter amount', tempLetterAmount)

                n = len(word) - 1 - i

                divider = 1

                for duplicate in list(tempLetterAmount.values()):
                    if duplicate > 1:
                        divider *= math.factorial(duplicate)

                rank += math.factorial(n) / divider

                print( rank , 'this is rank')
    
    rank += 1

    return int(rank)

print(list_position(word))