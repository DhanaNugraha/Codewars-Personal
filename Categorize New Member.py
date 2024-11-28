data = [[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]

def open_or_senior(data):
    output = []

    for age, handicap in data:
         
        if age >= 55 and handicap > 7:
            output.append("Senior")

        else:
            output.append("Open")

    return output

print(open_or_senior(data))