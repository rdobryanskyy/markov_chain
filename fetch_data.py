__author__ = 'rostyslav'
#this class should get data form the source and parse it


from bs4 import BeautifulSoup
import nltk
import re


response = open('The Project Gutenberg eBook of Planet of the Damned, by Harry Harrison.txt', 'r')
html = response.read()

def usual_words(unformated_text):
    soup = BeautifulSoup(unformated_text,'lxml')
    text_no_html = soup.get_text()
    text = text_no_html.split(' ')
    usual = []
    text_vocab = set(w.lower() for w in text if w.isalpha())
    english_vocab = set(w.lower() for w in nltk.corpus.words.words())
    for w in text_vocab:
        if w in english_vocab:
            usual.append(w)
    return usual

book_voc = usual_words(html)
source_no_tags = (BeautifulSoup(html,'lxml')).get_text()

string_source = str(source_no_tags)
string_source = string_source.replace('\r\n',' ')
string_list = string_source.split(' ')

#print type(string_source)
#print string_source
print str(string_list)
