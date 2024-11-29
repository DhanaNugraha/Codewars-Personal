chars = ['a','b','c','d','f']

def find_missing_letter(chars):
    for i in range(len(chars) - 1):
        difference = ord(chars[i + 1]) - ord(chars[i]) 

        if difference != 1:
            return chr(ord(chars[i]) + 1)

print(find_missing_letter(chars))