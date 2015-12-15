__author__ = 'rostyslav'
import unittest
import markovlib
import comunication_layer

class TestStringMethods(unittest.TestCase):

    def setUp(self):
        pass

    def test_file_load(self):
        file = comunication_layer.GetFile()
        self.assertIsNotNone(file.readfile(),'No text loaded')

    def test_check_text_clean(self):
        markov = markovlib.Markov('asdfghjkl;098765rfbnm bgt678iolmngf43ef!@#$%^&*()g')
        self.assertDictContainsSubset('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ',markov.generate_markov_text(10),'Message')


if __name__ == '__main__':
    unittest.main()