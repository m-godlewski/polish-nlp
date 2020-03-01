try:
    import time
    from cleaner import Cleaner
    from tokenizer import Tokenizer
    from corrector import Corrector
    from normalizer import Normalizer
    from vectorizer import Vectorizer
except ImportError as ie:
    print(f"IMPORT ERROR -> {ie}")


class NLP(object):
    """ Class that handle all of NLP subclasses.

    This class contain subclasses like:
    - Cleaner
    - Tokenizer
    - Corrector
    - Normalizer
    - Vectorizer
    
    """
    
    def __init__(self):
        """ Initialization of NLP class object.

        This function initialize NLP class objects,
        with creation of inner objects of all NLP subclasses.

        """
        self.cleaner = Cleaner()
        self.tokenizer = Tokenizer()
        self.corrector = Corrector()
        self.normalizer = Normalizer()
        self.vectorizer = Vectorizer()