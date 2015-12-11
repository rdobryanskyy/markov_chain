__author__ = 'rostyslav'
#this class should get data form the source


from bs4 import BeautifulSoup
import nltk


response = open('The Project Gutenberg eBook of Planet of the Damned, by Harry Harrison.txt', 'r')
html = response.read()



def usual_words(unformated_text):
    soup = BeautifulSoup(unformated_text,'lxml')
    text_no_html = soup.get_text()
    text = text_no_html.split(' ')
    usual = []
    text_vocab = set(w.lower() for w in text if w.isalpha())
    english_vocab = set(w.lower() for w in nltk.corpus.words.words())
    print text_vocab
    for w in text_vocab:
        if w in english_vocab:
            usual.append(w)
    return usual




usual_words(html)
