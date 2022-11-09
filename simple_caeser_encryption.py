# Ceaser Encryption 
# Idea to encrypt a message by shifting the alphabet
# ABCDEFG
# shift by 3--> CDEFGAB
# BEE --> DGG


import string


def ceaser (text, shift, alphabets):
    """Return an encrypted text/word/letter
    
    Parameters:
    
    text = text which is going to be encrypted
    shift = number of shifting
    alphabets = multiple alphabets as a list 
    """

    def shift_alphabet(alphabet):
        """Shift function: Return of the shifted alphabet"""
        return alphabet[shift:] + alphabet[:shift]

    shifted_alphabets = tuple(map(shift_alphabet, alphabets))
    final_alphabet = ''.join(alphabets)
    final_shifted_alphabet = ''.join(shifted_alphabets)
    print(final_shifted_alphabet)

    table = str.maketrans(final_alphabet, final_shifted_alphabet)
    return text.translate(table)

plain_text = "Hello Wolrd!"

encrypt = ceaser(plain_text, 5, [string.ascii_lowercase, string.ascii_uppercase, string.punctuation])
print(encrypt)

decrypt = ceaser(encrypt, 26-5, [string.ascii_lowercase, string.ascii_uppercase, string.punctuation])

print(decrypt)
print(encrypt)