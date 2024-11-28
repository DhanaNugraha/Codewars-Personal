text = "The_stealth-warrior"

def to_camel_case(text):
    text = list(text)
    output = []

    for i in range(len(text)):

        if text[i].isalpha():

            if text[i - 1].isalpha():
                output.append(text[i])

            else:
                output.append(text[i].upper())

    return "".join(output)

print(to_camel_case(text))