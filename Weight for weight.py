strng = "56 65 74 100 99 68 86 180 90"

def order_weight(strng):
    # sorts split string 
    return ' '.join(sorted(strng.split(' '), key=lambda x: sum(int(c) for c in x)))

    # first we make a list of sorted split string (no need, explnation in second comment)
    # then we sort again the sorted string by the sum of their integer, when using key, if the value are the same, it will sort based on original strng so only need to sort once based on sum of their int
    # join the resulting sorted list.
print(order_weight(strng))