
import math
import re
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
Rttfiuzex kf r sffb Z ivru, kyv Gyfveztzrej, Vxpgkzrej, Yzeulj, reu Argrevjv svczvmvu kyv Vriky yrktyvu wifd r dleurev vxx. Dleurev?“Dfddp, nyrk ufvj dleurev dvre?”
Jyv nrj jkziizex r gfk fw jflg reu Z tflcu jvv jyv nrj efk ze r xffu dffu. Ruvcv nrj gcrpzex, kyviv nrj r sfkkcv crsvccvu “EF KFLTYZEX” fe kyv tflekvi (kyrk nrj kf nrie dv), reu r drikzez xcrjj jzkkzex fe kyv tflekvi yrcw vdgkp. Uruup reu dfddp rixlvu kyzj dfiezex. Zk nfbv dv lg. Z gcrpvu nzky dp ufccj lekzc Z yvriu kyv uffi jcrd. Wifd dp nzeufn Z tflcu jvv dp uruup jnzic flk fw kyv uizmvnrp.

Z glccvu fe yvi k-jyzik. “Dfddp, dleurev?”

“Vrikycp. Ulcc. Efn xf uf pfli tyfivj.”

Flkjzuv kyv urp nrj r avnvc. Kyv xirjj nrj czbv vdvircu uljk. Kyviv nviv wclwwp slk jtrek tcfluj. Kyviv nrj kyv xfcu czxyk fw kyv jle. Fli jdrcc wrid jvvdvu uivetyvu ze crdsvek svrlkp.

“Yfn tflcu kyzj tfdv wifd r dviv dleurev vxx?” Z nfeuvivu.

Z xfk kyv iljkvu, nziv srjbvk kf tfccvtk kyv tyztbve vxxj. Di. Iffjkvi nrj mvip sfjjp kyzj dfiezex jf Z sfjjvu yzd srtb. Kyv yvej tcltbvu rj Z jvrityvu wfi vxxj. Nyve Z wfleu kyv jvmveky fev zk wvcc.
“Fy, ef.” Z tflcu jvv ef sizxyk pfcb. Z jrn r jgyviv nzky czkkcv gvfgcv reu zk nrj xifnzex.
Z ire zejzuv, uifggzex rcc kyv vxxj rj Z yliizvu.
“Dfddp, dfddp. Kyviv j r nficu xifnzex ze fli nficu.” Jyv grzu ef rkkvekzfe. Jyv bvgk jkziizex kyv gcfk rexizcp. Z druv efkv efk kf xvk rexip rj Z xifn fcuvi rj Z nflcu dzjj r xivrk uvrc fw czwv. Z tflcu dzjj czwv zkjvcw.
""".lower()

# to clean cipher text and eliminate all punctuations and spaces
cipher = ''.join(re.sub(r'[^\w\s]', '', ciphertext).split())
print("CIPHER TEXT")
print(cipher)
print()
letter_frequencies = calculate_letter_frequencies(ciphertext)

# print(letter_frequencies)
I = 0.065
min_diff = float('inf')
k = 0
# for the correct key value of summation(pi*qi+k)=0.065 approximately
for j in range(26):
    Ij = 0
    for i in range(26):
        english_original_letter = mapping[i]
        pi = actual_probabilities[english_original_letter]
        shift_index = (i+j) % 26
        cipher_letter = mapping[shift_index]
        if cipher_letter in letter_frequencies:
            qij = letter_frequencies[cipher_letter]
        else:
            qij = 0
        Ij += pi*qij
    if (abs(Ij-I) < min_diff):
        min_diff = abs(Ij-I)
        k = j

print("Key:", end="")
print(k)
print()
print("PLAIN TEXT:")
print(findPlainText(cipher, k))
