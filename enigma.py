#!/usr/bin/env python


class Crypto(object):

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


    def encrypt(self, letter, params, first_gear):

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


    def decrypt(self, letter, params, first_gear):
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


    def init_gear(self, num, key):
        letters = self.gears[num]
        result = {
            'letters': letters,
            'keyIndex': letters.index(key.upper())
        }
        return result


    def init_gears(self, num1, num2, num3, key):
        return [
            self.init_gear(num1, key[0]),
            self.init_gear(num2, key[1]),
            self.init_gear(num3, key[2])
        ]


    def encrypt_message(self, gears, message):
        count = 0
        result = ''
        first_gear = True
        for m in message:
            #print m
            if m.upper() in self.alphabet:
                result += self.encrypt(m.upper(), gears, first_gear)
                first_gear = not first_gear
            else:
                continue
            count += 1
            if count == 4:
                result += ' '
                count = 0
        return result


    def decrypt_message(self, gears, message):
        count = 0
        result = ''
        first_gear = True
        for m in message:
            if m.upper() in self.alphabet:
                result += self.decrypt(m.upper(), gears, first_gear)
                first_gear = not first_gear
                count += 1
                if count == 4:
                    result += ' '
                    count = 0
        return result


    def run_enigma_encryption(self, gear_one, gear_two, gear_three, enc_key, message):

        igears = self.init_gears(gear_one, gear_two, gear_three, enc_key)  # initiated gears
        return self.encrypt_message(igears, ' '.join(message))

    def run_enigma_decryption(self, gear_one, gear_two, gear_three, enc_key, message):

        igears = self.init_gears(gear_one, gear_two, gear_three, enc_key)  # initiated gears
        return self.decrypt_message(igears, ' '.join(message))


