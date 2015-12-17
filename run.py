__author__ = 'rostyslav'
import fetch_data
import comunication_layer
import enigma


getfilefrom = comunication_layer.GetFile()
html = getfilefrom.readfile()
newbook = fetch_data.Create_Text(html)

book_for_enc = str(newbook.generate_text(5000))

encrypt = enigma.Crypto()
print book_for_enc
print encrypt.run_enigma(51,61,71,'AAA',book_for_enc.strip())