strng = "56 65 74 100 99 68 86 180 90"

def order_weight(strng):
    strng = strng.split()
    # sum:num
    sumWeight = {}

    for num in strng:
        curSum = sum([int(i) for i in num])
        print(sumWeight)
        
        if curSum in sumWeight:
            curSumWeight = sumWeight[curSum].split()
            curSumWeight.append(num)
            sumWeight[curSum] = ' '.join(sorted(curSumWeight))

            print(curSumWeight, sumWeight)
        
        else:
            sumWeight[curSum] = str(num)

    sortedKey= sorted(sumWeight.keys())

    valueList = [sumWeight[i] for i in sortedKey]

    output = ' '.join(valueList)

    return output


print(order_weight(strng))