n = 1234

def count_bits(n):
    reversedBits = []

    while n > 0:
        reversedBits.append(n % 2)
        n = int(n / 2)

    count = 0

    for bit in reversedBits:
        if bit == 1:
            count += 1

    return count

print(count_bits(n))