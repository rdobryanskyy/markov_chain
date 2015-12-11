__author__ = 'rostyslav'
#this class should get data form the source

import urllib2
from HTMLParser import HTMLParser
import re
from bs4 import BeautifulSoup
import nltk
#nltk.download('all')

response = open('The Project Gutenberg eBook of Planet of the Damned, by Harry Harrison.txt', 'r')
html = response.read()



def usual_words(text):
    usual = []
    text_vocab = set(w.lower() for w in text if w.isalpha())
    english_vocab = set(w.lower() for w in nltk.corpus.words.words())
    for w in text_vocab:
        if w == english_vocab:
            usual.append(w)
    return sorted(usual)

print usual_words(html)



"""
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

"""