a = [1, 2, 3, 100]

for i in range(len(a)):
    s = a.pop(i)
    print(s)
    print(a)
    a.insert(i, s)



