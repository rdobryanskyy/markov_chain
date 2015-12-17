__author__ = 'rostyslav'
import fetch_data
import comunication_layer
import enigma


getfilefrom = comunication_layer.GetFile()
html = getfilefrom.readfile()
newbook = fetch_data.Create_Text(html)
#Encrypting the book
encrypt = enigma.Crypto()
book_for_enc = str(newbook.generate_text(100))
enc_book = encrypt.run_enigma_encryption(51,61,71,'AAA',book_for_enc.strip())


print book_for_enc
print '\n' + enc_book

#Decrypting the book

print '-----------------------------------------------'

decr_book = encrypt.run_enigma_decryption(51,61,71,'AAA',enc_book)

print decr_book