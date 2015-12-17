__author__ = 'rostyslav'

import enigma

encrypt = enigma.Crypto()

print encrypt.run_enigma(51,61,71,'AAA','BLAblabla')

#print encrypt.init_gears(51,61,71,'ooo')
