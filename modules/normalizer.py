try:
    import time
    from tokenizer import Tokenizer
    from corrector import Corrector
except ImportError as ie:
    print(f"IMPORT ERROR -> {ie}")


class Normalizer(object):
    """ Class used for text normalization (stemming and lemmatization)

    """

    def __init__(self):
        pass