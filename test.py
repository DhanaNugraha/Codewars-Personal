s = "is2 Thi1s T4est 3a"

s = s.split()

def numFinder(e):
    for str in e:
        if str.isnumeric():
            return str

print(s)
s.sort(key = numFinder)
print(s)

'-55,-53,-52,-49,-48,-46,-43,-40,-37--35,-33,-31,-28--26,-24,-22,-19,-16,-13,-10--9' should equal 
'-55,-53,-52,-49,-48,-46,-43,-40,-37--35,-33,-31,-28--26,-24,-22,-19,-16,-13,-10,-9'


