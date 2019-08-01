import sys

def encode(in_message):
    """Converts a message to Morse code."""
    out_message = [MORSE_CODE_DICTIONARY[char] for char in in_message.upper()]
    return ' '.join(out_message)

def decode(in_message):
    """Converts a message from Morse code."""
    MC_DICT_INVERTED = {value: key for key, value in MORSE_CODE_DICTIONARY.items()}
    in_message = in_message.split(' ')
    out_message = [MC_DICT_INVERTED[char] for char in in_message]
    return ''.join(out_message)


MORSE_CODE_DICTIONARY = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    ' ': '/',
}

if len(sys.argv) < 3:
    sys.exit()
command = sys.argv[1].lower()
message = ' '.join(sys.argv[2:])

if command == 'encode':
    print(encode(message))
elif command == 'decode':
    print(decode(message))