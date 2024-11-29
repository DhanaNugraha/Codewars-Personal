s = "CoDeWaRs is niCe"

def generate_hashtag(s):
    s = s.split()

    for i in range(len(s)):
        word = list(s[i])

        for j in range(len(word)):
            if j == 0:
                word[j] = word[j].upper()
            else:
                word[j] = word[j].lower()

        s[i] = ''.join(word)

    s = '#' + ''.join(s)

    if s == '#' or len(s) > 140:
        return False

    return s

print(generate_hashtag(s))