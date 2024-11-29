s = "is2 Thi1s T4est 3a"

s = s.split()

def numFinder(e):
    for str in e:
        if str.isnumeric():
            return str

print(s)
s.sort(key = numFinder)
print(s)


