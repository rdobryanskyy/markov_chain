__author__ = 'rostyslav'

class GetFile(object):

    def readfile(self):
        response = open('The Project Gutenberg eBook of Planet of the Damned, by Harry Harrison.txt', 'r')
        return response.read()
        

   # def file_from_url(self, url):
