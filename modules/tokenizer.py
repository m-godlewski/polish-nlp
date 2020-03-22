import re
import time


class Tokenizer(object):
    """ Class used for tokenization of sentences

    Functionality included:
    - sentence tokenization
    - text tokenization
    
    """

    def __init__(self):
        pass

    def sentence_tokenization(self, text:str) -> list:
        """ Tokenization of sentence to list of words.
        
        Arguments:
            text {str} -- [text]
        
        Returns:
            list -- [list of tokens]
        """
        return re.findall(r"[\w']+", text)

    def text_tokenization(self, text:str, division_marks:bool=True) -> list:
        """ Tokenization of text to list of sentences, by '!', '?' and '.' marks.
        
        Arguments:
            text {str} -- [text]
        
        Returns:
            list -- [list of sentences in given text]
        """
        tokens = re.split(r'(?<=[.!?]) +',text) # splitting by division marks
        if division_marks:
            return tokens
        else:
            return [ token[:-1] for token in tokens ] # removing division marks