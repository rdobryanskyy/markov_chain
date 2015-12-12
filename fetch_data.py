__author__ = 'rostyslav'
#this class should get data form the source and parse it


from bs4 import BeautifulSoup
import nltk
import markovlib
import comunication_layer


class Create_Text(object):

    def __init__(self,data):
        self.data = data


    # def usual_words(self):
    #    soup = BeautifulSoup(self.data,'lxml')
    #    text_no_html = soup.get_text()
    #    text = text_no_html.split()
    #    usual = []
    #    text_vocab = set(w.lower() for w in text if w.isalpha())
    #    english_vocab = set(w.lower() for w in nltk.corpus.words.words())
    #    for w in text_vocab:
    #        if w in english_vocab:
    #            usual.append(w)
    #    return usual

    def generate_text(self,number):
        # book_voc = self.usual_words()
        source_no_tags = (BeautifulSoup(self.data,'lxml')).get_text()
        string_source = str(source_no_tags)
        string_source = string_source.replace('\r\n',' ')
        string_source = string_source.replace('=97','')
        string_source = string_source.replace('attr(title)','')
        string_source = string_source.replace('=','')
        string_source = string_source.replace('[','')
        string_source = string_source.replace(']','')
        string_list = string_source.split()
        # for w in string_list:
        #     if w in book_voc:
        #         pass
        #     elif len(w) > 45:
        #         string_list.remove(w)
        #     else:
        #         string_list.remove(w)
        clean = string_list
        markov = markovlib.Markov(clean)
        #print markov
        #return markov.generate_markov_text(number)
        print markov.generate_markov_text(number)