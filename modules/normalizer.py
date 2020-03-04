try:
    import time
    import morfeusz2
    from tokenizer import Tokenizer
    from corrector import Corrector
except ImportError as ie:
    print(f"IMPORT ERROR -> {ie}")


class Normalizer(object):
    """ Class used for text normalization (stemming and lemmatization)

    - Lemmatization
    - Stemming

    """

    def __init__(self):
        self.tokenizer = Tokenizer()
        self.morpheus = morfeusz2.Morfeusz()