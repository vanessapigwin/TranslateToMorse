# I converted the word into a list of upper case characters to match the dictionary. I also added a ' ' to the keys to account for spaces.
#
# Implemented key error handle to store the erring key into another variable which will notify the user later on. User can try again on fail of translation.

# morse code, plus space char ' ' at last entry
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ',':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-',' ':' '}


def encrypt():
    translation = ''
    error_char = ''
    word = list(input("Enter the word to be translated to Morse: ").upper())

    for char in word:
        try:
            translation += MORSE_CODE_DICT[char]+" "
        except KeyError:
            error_char += char

    if error_char:
        print(f'Sorry, the character/s {error_char} could not be converted. Please try again.')
        encrypt()
    else:
        print(translation)


encrypt()
