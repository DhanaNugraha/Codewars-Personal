# make a tree for input if combination is found, return the rank

word = 'ABAB'
# try ABB

def list_position(word):
    letterList = sorted(set(word))
    wordLength = len(word)
    letterAmount = {}

    for letter in letterList:   
        letterAmount[letter] = word.count(letter)

    print(letterList, wordLength, letterAmount)

    stack = []
    found = False
    
    def decisionTree(startLetter, nextLetterIndex, nextLetterLen, curStackLength, rank):
        if found == True:
            return rank
        
        elif curStackLength == wordLength:
            curWord = ''.join(stack)
            rank += 1
            
            if curWord == word:
                found == True
        
            return rank

        else:
            nextLetter = letterList[nextLetterIndex]

            if stack == []:
                stack.append(startLetter)

                decisionTree(startLetter, nextLetterIndex,nextLetterLen, curStackLength + 1, rank)

                stack.pop()
                
            
            if nextLetterLen == 0 and nextLetter == startLetter:
                nextLetterLen += 1

            if nextLetterLen < letterAmount[nextLetter]:
                stack.append(nextLetter)
                nextLetterLen += 1

                decisionTree(startLetter, nextLetterIndex, nextLetterLen, curStackLength + 1, rank)
                print(stack)
                stack.pop()

            if nextLetterLen == letterAmount[nextLetter]:
                for i in range(len(letterList)):
                    if stack.count(letterList[i]) < letterAmount[letterList[i]]:
                        nextLetterIndex = i
                        nextLetterLen = 0
                        print('im here', stack, nextLetterIndex)

                print(nextLetterIndex, 'this is next letter')

                decisionTree(startLetter, nextLetterIndex, nextLetterLen, curStackLength, rank)

    while found == False:
        for letter in letterList:
            rank = decisionTree(letter, 0, 0, 0, 0)

    return rank

print(list_position(word))