
import math

def char_to_prob(char):
    if char is None or len(char) != 1:
        return None

    q = ord(char) - 33

    if q < 0:
        return None

    prob = 10 ** (-q / 10)
    return prob


def prob_to_char(prob):
    if prob is None or prob <= 0 or prob > 1:
        return None

    q = -10 * math.log10(prob)
    char = chr(round(q) + 33)
    return char


print(char_to_prob('A'))
print(prob_to_char(0.001))





