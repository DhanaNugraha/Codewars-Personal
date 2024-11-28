s = "welcome to the jungle"

def find_short(s):
    s = s.split()
    l = None
    for word in s:
        if l == None:
            l = len(word)
        else:
            l = min(l, len(word))
    return l 

print(find_short(s))