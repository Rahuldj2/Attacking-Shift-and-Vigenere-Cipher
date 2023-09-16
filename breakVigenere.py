# import math
import re
from collections import Counter
from math import gcd

print("ATTACK ON VIGENERE CIPHER")
print()
actual_probabilities = {
    'a': 0.082,
    'b': 0.015,
    'c': 0.028,
    'd': 0.043,
    'e': 0.13,
    'f': 0.022,
    'g': 0.02,
    'h': 0.061,
    'i': 0.07,
    'j': 0.002,
    'k': 0.008,
    'l': 0.04,
    'm': 0.024,
    'n': 0.067,
    'o': 0.075,
    'p': 0.019,
    'q': 0.001,
    'r': 0.06,
    's': 0.063,
    't': 0.091,
    'u': 0.028,
    'v': 0.01,
    'w': 0.024,
    'x': 0.002,
    'y': 0.02,
    'z': 0.001,
}


mapping = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e',
           5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j', 10: 'k', 11: 'l',
           12: 'm', 13: 'n', 14: 'o', 15: 'p', 16: 'q', 17: 'r', 18: 's', 19: 't',
           20: 'u', 21: 'v', 22: 'w', 23: 'x', 24: 'y', 25: 'z'}


alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
            "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

reverse_mapping = {value: key for key, value in mapping.items()}


def findPlainText(cipher, key):
    plainText = ""

    for letter in cipher:
        # print(letter)
        # if (letter in reverse_mapping):
        c = reverse_mapping[letter]
        p = (c-key) % 26
        plainText += alphabet[p]
    return plainText


def calculate_letter_frequencies(ciphertext):
    # Remove spaces and punctuation, and convert to lowercase
    cleaned_text = ''.join(filter(str.isalpha, ciphertext)).lower()

    # Initialize a dictionary to store letter frequencies
    letter_frequencies = {}

    # Calculate the total number of letters in the cleaned text
    total_letters = len(cleaned_text)

    # Calculate letter frequencies
    for letter in cleaned_text:
        if letter in letter_frequencies:
            letter_frequencies[letter] += 1
        else:
            letter_frequencies[letter] = 1

    # Normalize frequencies by dividing by the total number of letters
    for letter, count in letter_frequencies.items():
        letter_frequencies[letter] = count / total_letters

    return letter_frequencies


Pilist = []
for Pi in actual_probabilities.values():
    Pilist.append(Pi)

# print(Pilist)
ciphertext = """
Bgcrshiqh xo d cson J vede, xhh Qlohomclbrs, Hhcpwjenv, Imngvw, aqe Nasbrevf feojivhe xhh Ferwi lawdleg gvop b quqeenh fkg. Pvrddoi?

“Mrnqy, ziet gpis pvrddoi mhbr?”

Skf aav txiusmnj b tow pj srvt aqe M crvpd vfi skf aav ost lo e grph mrph. Agfpe zbw pobciqh, xhhsi wdt e bruxlh mebhmpeg “OS TRVGHLOK” oq ule fpynwfv (tkbx wdt xo zbvn pf), eng b qauumnl hpavt wiwumnj pr tkf goxoxeu ieli fqpwz. Hagec aqe qopnc auhyeg uliv nsrqjrg. Lu aonf qe xq. M pobceg xmtk nc drmps xoxio J ledsh tkf hors wldn. Jrrn qy zjrdrx M crvpd vfi mb eedgz wwlsp oxu sf wii dujzezbc.

I svplhe sn kfv t-vimrw. “Nsmpz, quqeenh?”

“Ferwipy. Gvpl. Qpa gr es yrvv ckpvev.”

Pytvjhe wii ddz aav b nezfp. Tkf krdtw wdt pinf imhselg eysw. Uleuf aeuf jlxgjy evx sfbrt fmsugt. Xhhsi wdt xhh hslg mmgku sf wii sxo. Suu tqaom jaun wehnid gsinfiid lo papcinw ciaxuc.

“Hrx goxmh tkjw crni fupq a pfve pvrddoi ejh?” M wroheufh.

I jpx tkf vuvuid, zjve ebwkhu xo fpplhdx tkf ghldoeq fkgv. Nv. Rrpwths aav wirb cssvz xhlt qouomnj ts I epwshe lip cecn. Ule kfrs fmycnfh av J wedsghhe jou fkgv. Xleq J joxoh tkf weyfrtk pre lu jeom.

“Sh, qp.” M crvpd vfi nr cvijix yrmo. I vba a vqleuf aiwi piwupe sfspof eng jx wdt krrxmnj.

J vaq jrslei, duptplok aom xhh fkgv bw I kvvrlfh.

“Mrnqy, ppqmb. Uleuf w a zpvlg hvozjrg lo suu xsroe.” Whh qeig os awuinwjsn. Vii khqx swjvrlok tkf tlru enjsmlb. J qagf rowf row us ghu enjsc av J krrx slgfv av J aoxmh mltw a jsiaw eiao pj llgi. I fpylg nmsv mmfh jxshmj.
""".lower()

cipher = ''.join(re.sub(r'[^\w\s]', '', ciphertext).split())
# print(cipher)
print("Cipher text:")
print(cipher)
print()
letter_frequencies = calculate_letter_frequencies(ciphertext)
# print(letter_frequencies)

# KASISKI TEST


def find_most_frequent_ngrams(text, n):
    # Remove spaces and non-alphabetic characters, and convert to lowercase
    cleaned_text = re.sub(r'[^a-zA-Z]', '', text).lower()

    ngrams = [cleaned_text[i:i+n] for i in range(len(cleaned_text) - n + 1)]
    ngram_counts = Counter(ngrams)

    # Sort the ngrams by frequency in descending order
    sorted_ngrams = sorted(ngram_counts.items(),
                           key=lambda x: x[1], reverse=True)

    return sorted_ngrams


# Find the most frequent trigrams along with their relative frequencies
most_frequent_trigrams = find_most_frequent_ngrams(ciphertext, 3)

# KASISKI TEST- to calculate distances between the most occuring trigrams


def calcDistance(sub, cipher):
    res = [i for i in range(len(cipher) - len(sub) + 1)
           if cipher.startswith(sub, i)]
    return res


key_with_max_value = max(most_frequent_trigrams, key=lambda x: x[1])[0]
distances = calcDistance(key_with_max_value, cipher)

# print(distances)
numbers = []
for i in range(len(distances)-1):
    diff = distances[i+1] - distances[i]
    numbers.append(diff)


def find_gcd_of_numbers(numbers):
    if len(numbers) < 2:
        raise ValueError("At least two numbers are required to find the GCD.")

    result = numbers[0]
    for num in numbers[1:]:
        result = gcd(result, num)

    return result


# KASISKI TEST
print("LENGTH OF KEY FOUND USING KASISKI TEST:")
print(find_gcd_of_numbers(numbers))

t = find_gcd_of_numbers(numbers)
I = 0.065
k = 0
min_diff = float('inf')

# verification using index of coincidence
for i in range(26):
    letter_in_cipher = mapping[i]
    S = 0
    if (letter_in_cipher in cipher):
        qi = letter_frequencies[letter_in_cipher]
        S += pow(qi, 2)
    if (abs(S-I) < min_diff):
        min_diff = abs(S-I)
        k = i
print("LENGTH OF KEY VERIFIED USING INDEX OF COINCIDENCE:")
print(k)
k = t

i = -1
stringList = []
actualKeyList = []
# print(cipher[0])


def shiftIc(letter_frequency):
    I = 0.065
    min_diff = float('inf')
    k = 0
    # print(letter_frequency)
    for j in range(26):
        Ij = 0
        for i in range(26):
            english_original_letter = mapping[i]
            pi = actual_probabilities[english_original_letter]
            shift_index = (i+j) % 26
            cipher_letter = mapping[shift_index]
            if cipher_letter in letter_frequency:
                qij = letter_frequency[cipher_letter]
            else:
                qij = 0
            Ij += pi*qij
        if (abs(Ij-I) < min_diff):
            min_diff = abs(Ij-I)
            k = j
    return k


initial = 0
for m in range(k):
    substr = ""
    # substr += cipher[initial]
    x = 2
    i = initial
    while (i < len(cipher)):
        substr += cipher[i]
        i = initial+x*k
        x += 1
    letter_frequencies_sub = calculate_letter_frequencies(substr)
    # print(letter_frequencies)

    # print(substr)
    # print()
    subkeym = shiftIc(letter_frequencies_sub)

    actualKeyList.append(mapping[subkeym])
    initial += 1
    # initial += 1

print("Key is ", end='')
print(actualKeyList)

initial = 0
plainText = ""
flag = 0
ind = 0
for letters in cipher:
    if (ind > 3):
        ind = 0
    cipheri = reverse_mapping[letters]
    pi = (cipheri-reverse_mapping[actualKeyList[ind]]) % 26
    plainText += mapping[pi]
    ind += 1
print("PlainText:")
print(plainText)


# apply shift ioc on
