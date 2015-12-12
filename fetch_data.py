__author__ = 'rostyslav'
#this class should get data form the source and parse it


from bs4 import BeautifulSoup
import nltk
import markovlib
import comunication_layer

getfilefrom = comunication_layer.GetFile()
html = getfilefrom.readfile()

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
string_source = string_source.replace('=97','')
string_list = string_source.split(' ')


markov = markovlib.Markov(string_list)

#print markov.generate_markov_text(500)


print markov.generate_markov_text(1700)