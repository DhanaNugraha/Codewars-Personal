n = [0,0,0,0,0,0,0,0,0,0]

# '(231) 456-7890' should equal '(123) 456-7890'
# '(1111111111) -' should equal '(111) 111-1111'
# '(231) 456-7890' should equal '(123) 456-7890'
# '(03000) 06-090' should equal '(023) 056-0890'
# '(0000000000) -' should equal '(000) 000-0000'

def create_phone_number(n):
    output1 = ''
    output2 = ''
    output3 = ''

    for i in range(len(n)):
        if 0 <= i < 3:
            output1 += str(n[i])

        elif 3 <= i < 6:
            output2 += str(n[i])

        else:
            output3 += str(n[i])

    output = '(' + output1 + ') ' + output2 + '-' + output3

    return output

print(create_phone_number(n))