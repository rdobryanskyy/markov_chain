__author__ = 'rostyslav'
import fetch_data
import comunication_layer


getfilefrom = comunication_layer.GetFile()
html = getfilefrom.readfile()
newbook = fetch_data.Create_Text(html)

print newbook.generate_text(100)