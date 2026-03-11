s = 'hello    this is fun!'
chars = [0] * 128


for c in s:
    ascii_val = ord(c)
    chars[ascii_val] += 1


for i in range(len(chars)):
    if chars[i] == 0:
        continue
    print(i, chars[i])
