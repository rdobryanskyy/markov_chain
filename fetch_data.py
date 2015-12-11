__author__ = 'rostyslav'
#this class should get data form the source

import urllib2
from HTMLParser import HTMLParser
import re
from bs4 import BeautifulSoup

response = open('The Project Gutenberg eBook of Planet of the Damned, by Harry Harrison.txt', 'r')
html = response.read()

soup = BeautifulSoup(html,'lxml')

text_no_html = soup.get_text()

#print "/*" + "<![" + ".+?>*/"
#text = re.sub(r"/*<![CDATA[  XML blockout */ .+? /* XML end  ]]>*/", '', soup)

style = soup.style

text_list = text_no_html.split(' ')

p_string = soup.p

#print len(p_string)
#for i in soup:
#    print i

#print text_list

for word in text_list:
    if len(word) > 45:
        del text_list.remove(word)

print text_list