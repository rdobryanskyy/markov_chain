#!/usr/bin/env python

import argparse


gears = {}

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

gears[50] = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
gears[51] = 'ADCBEHFGILJKMPNOQTRSUXVWZY'
gears[52] = 'AYZWVXUSRTQONPMKJLIGFHEBCD'
gears[53] = 'ADCBEHGFILKJMPONQTSRUXWVZY'

gears[60] = 'ACEDFHGIKJLNMOQPRTSUWVXZYB'
gears[61] = 'AZXVTRPNDJHFLBYWUSQOMKIGEC'
gears[62] = 'ACEGIKMOQSUWYBLFHJDNPRTVXZ'
gears[63] = 'ADECFIGHKNLJMPQORUSTWZXVBY'

gears[70] = 'AZYXWVUTSRQPONMLKJIHGFEDCB'
gears[71] = 'AEBCDFJGHIKOLMNPTQRSUYVWXZ'
gears[72] = 'AZXWVYUSRQTPNMLOKIHGJFDCBE'
gears[73] = 'AXYZWTUVSPQROLMNKHIJGDEFBC'


parser = argparse.ArgumentParser(description='Encrypt or decrypt enigma message.',
                                 usage='%(prog)s [options]')
parser.add_argument('-k', '--key', type=str, help='Encryption key.')
parser.add_argument('-g', '--gears', type=int, nargs=3, choices=gears.keys(),
                    help='Gears configuration.')
parser.add_argument('-e', '--encrypt', action='store_true',
                    help='Encrypt message.')
parser.add_argument('-d', '--decrypt', action='store_true',
                    help='Decrypt message.')
parser.add_argument('message', nargs=argparse.REMAINDER,
                    help='Text to encrypt or decrypt.')

args = parser.parse_args()



def encrypt(letter, params, first_gear):

    gear3 = params[2]
    pos_diff3 = gear3['keyIndex'] - gear3['letters'].index(letter)

    if first_gear:
        gear = params[0]
        index = gear['keyIndex'] - pos_diff3
    else:
        gear = params[1]
        index = gear['keyIndex'] + pos_diff3

    result = gear['letters'][index]

    return result


def decrypt(letter, params, first_gear):
    gear1 = params[0]
    gear1letters = gear1['letters']
    gear2 = params[1]
    gear2letters = gear2['letters']
    gear3 = params[2]
    gear3letters = gear3['letters']

    if first_gear:
        pos_diff = gear1['keyIndex'] - gear1letters.index(letter)
    	pos_diff3 = gear3['keyIndex'] - pos_diff
    else:
        pos_diff = gear2['keyIndex'] - gear2letters.index(letter)
    	pos_diff3 = gear3['keyIndex'] + pos_diff

    if pos_diff3 >= len(gear3letters):
        pos_diff3 = pos_diff3 - len(gear3letters)
    if pos_diff3 < -len(gear3letters):
        pos_diff3 = pos_diff3 + len(gear3letters)
    return gear3letters[pos_diff3]


def init_gear(num, key):
    letters = gears[num]
    result = {
        'letters': letters,
        'keyIndex': letters.index(key.upper())
    }
    return result


def init_gears(num1, num2, num3, key):
    return [
        init_gear(num1, key[0]),
        init_gear(num2, key[1]),
        init_gear(num3, key[2])
    ]


def encrypt_message(gears, message):
    count = 0
    result = ''
    first_gear = True
    for m in message:
        if m.upper() in alphabet:
            result += encrypt(m.upper(), gears, first_gear)
            first_gear = not first_gear
        else:
            continue
        count += 1
        if count == 4:
            result += ' '
            count = 0
    return result


def decrypt_message(gears, message):
    count = 0
    result = ''
    first_gear = True
    for m in message:
        if m.upper() in alphabet:
            result += decrypt(m.upper(), gears, first_gear)
            first_gear = not first_gear
            count += 1
            if count == 4:
                result += ' '
                count = 0
    return result


igears = init_gears(args.gears[0], args.gears[1],
                    args.gears[2], args.key)  # initiated gears

if args.encrypt:
    print encrypt_message(igears, ' '.join(args.message))
elif args.decrypt:
    print decrypt_message(igears, ' '.join(args.message))