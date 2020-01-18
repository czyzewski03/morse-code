#!/usr/bin/env python3

import sys
import argparse

def encode(in_message):
    """Converts a message to Morse code."""
    out_message = [TEXT_TO_MORSE[char] for char in in_message.upper() if char in TEXT_TO_MORSE.keys()]
    return ' '.join(out_message)

def decode(in_message):
    """Converts a message from Morse code."""
    in_message = in_message.split(' ')
    out_message = [MORSE_TO_TEXT[char] for char in in_message if char in MORSE_TO_TEXT.keys()]
    return ''.join(out_message)


TEXT_TO_MORSE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    ' ': '/',
}
MORSE_TO_TEXT = {value: key for key, value in TEXT_TO_MORSE.items()}

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', dest='input', help='input', required=True)
parser.add_argument('-m', '--mode', dest='mode', help='mode (encode/decode)', required=True)
args = parser.parse_args()

if args.mode.lower() in ('encode', 'e'):
    output = encode(args.input)
elif args.mode.lower() in ('decode', 'd'):
    output = decode(args.input)
else:
    parser.error("argument -m/--mode: expected 'encode' or 'decode'")

print(output)