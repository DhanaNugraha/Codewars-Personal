# condition of overlap -> num 1 <= left <= num2, num 1 <= right <= num2, left<= num1<= right, left<= num2 <= right
# make a new list 
# count difference

intervals = [[1, 4],[7, 10],[3, 5]]

def sum_of_intervals(intervals):
    newList = []

    for curLeft, curRight in intervals:
        if newList == []:
            newList.append([curLeft,curRight])

        # check for overlap
        else:
            for i in range(len(newList)):
                checkLeft, checkRight = newList.pop(i)
                
                # If any number is sandwiched, it counts as an overlap
                if checkLeft <= curLeft <= checkRight or\
                checkLeft <= curRight <= checkRight or\
                curLeft <= checkLeft <= curRight or\
                curLeft <= checkRight <= curRight:

                    # insert back a new overlap range
                    newList.insert(i, [min(curLeft, checkLeft), max(curRight, checkRight)])

                    break
                
                else:
                    # insert back the check that was popped
                    newList.insert(i, [checkLeft, checkRight])

                    # append new range in list
                    newList.append([curLeft, curRight])

        output = 0

        # calc the interval of the new list
        for left, right in newList:
            output += right - left

    return output


print(sum_of_intervals(intervals))