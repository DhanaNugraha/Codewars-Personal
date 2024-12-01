# a = [1, 2, 3, 100]

# for i in range(len(a)):
#     s = a.pop(i)
#     print(s)
#     print(a)
#     a.insert(i, s)

# a = 'MCMCMXC'
# library = {'CM':1000}
# total = 0
# if 'CM' in a:
#     count = a.count('CM')
#     total += library['CM'] *count
#     a = a.replace('CM', '')
#     print(a)
#     print(count, total)

# a = {'a': 1, 'b':2} 

# for letter in a.keys():
#     print(letter)


# word ='ABAB'
# print(sorted(set(word)))

# a = [1, 2, 3, 100, 100]

# print(a.count(100))


# if nextLetterLen == 0 and nextLetter == startLetter:
#                 nextLetterLen += 1


# if nextLetterLen == letterAmount[nextLetter]:
#     nextLetterIndex += 1
#     nextLetterLen = 0
#     print(nextLetterIndex, 'this is next letter')


# for letter in letterList:   
#         letterAmount[letter] = word.count(letter)

#     print(letterList, wordLength, letterAmount)

#     stack = []
#     found = False
    
#     def decisionTree(startLetter, nextLetterIndex, nextLetterLen, curStackLength, rank):
#         if found == True:
#             return rank
        
#         elif curStackLength == wordLength:
#             curWord = ''.join(stack)
#             rank += 1
            
#             if curWord == word:
#                 found == True
        
#             return rank

#         else:
#             nextLetter = letterList[nextLetterIndex]

#             if stack == []:
#                 stack.append(startLetter)

#                 decisionTree(startLetter, nextLetterIndex,nextLetterLen, curStackLength + 1, rank)

#                 stack.pop()
                
            
#             if nextLetterLen == 0 and nextLetter == startLetter:
#                 nextLetterLen += 1

#             if nextLetterLen < letterAmount[nextLetter]:
#                 stack.append(nextLetter)
#                 nextLetterLen += 1

#                 decisionTree(startLetter, nextLetterIndex, nextLetterLen, curStackLength + 1, rank)
#                 print(stack)
#                 stack.pop()

#             if nextLetterLen == letterAmount[nextLetter]:
#                 for i in range(len(letterList)):
#                     if stack.count(letterList[i]) < letterAmount[letterList[i]]:
#                         nextLetterIndex = i
#                         nextLetterLen = 0
#                         print('im here', stack, nextLetterIndex)

#                 print(nextLetterIndex, 'this is next letter')

#                 decisionTree(startLetter, nextLetterIndex, nextLetterLen, curStackLength, rank)

#     while found == False:
#         for letter in letterList:
#             rank = decisionTree(letter, 0, 0, 0, 0)


# import math

# a = {'a':1, 'b':2, 'c':3}
# n = 1

# for duplicate in list(a.values()):
#     n *= math.factorial(duplicate)

# z = n * 2

# print(n, z)

# word = 'IMMUNOELECTROPHORETICALLY'

# print(word)


# wordAmount = {'I': 2, 'M': 2, 'U': 1, 'N': 1, 'O': 3, 'E': 3, 'L': 3, 'C': 2, 'T': 2, 'R': 2, 'P': 1, 'H': 1, 'A': 1, 'Y': 1} 

# letterList = sorted(set(word))
# print(letterList)
# print(wordAmount)
# print(len(word))
# print(sum(wordAmount.values()))

# import math

# rank = 0
# divider = 1

# n = len(word) -1 - 0

# wordAmount['C'] -= 1

# for duplicate in list(wordAmount.values()):
#     if duplicate > 1:
#         divider *= math.factorial(duplicate)
#         print(duplicate, divider)

# print(math.factorial(n))

# rank += math.factorial(n) / divider


# print(int(rank))

# test = 620448401733239439360000 / 3456

# print('this is test', int(test))
# 620448401733239439360000

# 620448401733239439360000

a = {4: '2', 3:'28 18', 1: '17'}

output = ' '.join(a.values())

print(output)

sortedKey= sorted(a.keys())

valueList = [a[i] for i in sortedKey]

output = ' '.join(valueList)

print(output)

# a = 28

# z = sum([int(i) for i in str(a)])

# print(z)