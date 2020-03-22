# -*- coding: utf-8 -*-
""" This module contains main class of polish NLP module.

Polish NLP module contains the following functionalities:

- Cleaning
- Tokenization
- Corrector
- Normalization
- Vectorization

"""


from modules.cleaner import Cleaner
from modules.tokenizer import Tokenizer
from modules.corrector import Corrector
from modules.normalizer import Normalizer
from modules.vectorizer import Vectorizer


class NLP(object):
    """ Class that handle all of Polish NLP subclasses.

    This class contains subclasses like:
    - Cleaner from cleaner module
    - Tokenizer from tokenizer module
    - Corrector from corrector module
    - Normalizer from normalizer module
    - Vectorizer from vectorizer module
    
    """
    
    def __init__(self):
        """ Initialization of NLP class object.

        This function initialize NLP class object,
        by creation of inner objects of all NLP subclasses.

        """
        self.cleaner = Cleaner()
        self.tokenizer = Tokenizer()
        self.corrector = Corrector()
        self.normalizer = Normalizer()
        self.vectorizer = Vectorizer()