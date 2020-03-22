import time
import morfeusz
from stempel import StempelStemmer


class Normalizer(object):
    """ Class used for text normalization (stemming and lemmatization)

    - Lemmatization
    - Stemming

    """

    def __init__(self):
        self.stemmer = StempelStemmer.default()

    def word_lemmatization(self, word:str) -> str:
        """ Word lemmatization.
        
        Arguments:
            word {str} -- [word]
        
        Returns:
            str -- [lemmatized form of given word]
        """
        word_analyse = morfeusz.analyse(word)
        word_base_form = word_analyse[0][0][1]
        if word_base_form:
            # if there is a base form in morpheus module
            return word_base_form
        else:
            # if morpheus module has no base form of word
            return word

    def word_stemming(self, word:str) -> str:
        """ Word stemming.
        
        Arguments:
            word {str} -- [word]
        
        Returns:
            str -- [stemmed verstion of word]
        """
        return self.stemmer.stem(word)