args =  [-55, -53, -52, -49, -48, -46, -43, -40, -37, -36, -35, -33, -31, -28, -27, -26, -24, -22, -19, -16, -13, -10, -9]
def solution(args):
    output = ''
    linked = False
    seriesCounter = 0

    for i in range(len(args)): 
        # for the final value in the list as difference checks for next value
        if i == (len(args) - 1):
            # the last number in the linked series
            if linked == True and seriesCounter > 1:
                output += '-' + str(args[i])
                break
            # only 2 number in series counts as standalone
            elif linked == True and seriesCounter == 1:
                output += ',' + str(args[i])
                break
            # standalone number
            else:
                output += str(args[i])
                break
        
        # checks if next value is linked
        difference = args[i + 1] - args[i]
        
        # if next value is linked
        if difference == 1:
            # number in the middle of linked series
            if linked == True:
                seriesCounter += 1
                continue
            # the first number in the linked series
            else:
                output += str(args[i])
                linked = True
                seriesCounter += 1
        
        # if next value not linked
        else:
            # the final number in the linked series
            if linked == True and seriesCounter > 1:
                output += '-' + str(args[i]) + ','
                linked = False
                seriesCounter = 0
            # only 2 number in series counts as standalone
            elif linked == True and seriesCounter == 1:
                output += ',' + str(args[i]) + ','
                linked = False
                seriesCounter = 0
            # standalone number
            else:
                output += str(args[i]) + ','       
            
    return output


print(solution(args))