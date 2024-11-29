arr = [':)',':(',':D',':O',':;']

def count_smileys(arr):
    output = 0
    valid = {':', ';', '-', '~', ')', 'D'}
    eyes = {':', ';'}
    nose = {'-', '~'}
    mouth = {')', 'D'}

    for face in arr:
        face = list(face)
        notValid = False
        eyesCounter = 0
        noseCounter = 0
        mouthCounter = 0

        for feature in face:
            if feature not in valid:
                notValid = True
                break

            if feature in eyes:
                eyesCounter += 1
            elif feature in nose:
                noseCounter += 1
            else:
                mouthCounter += 1

        if notValid == False and eyesCounter == 1 and mouthCounter == 1 and noseCounter <= 1:
            output += 1

    return output

print(count_smileys(arr))