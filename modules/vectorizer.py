try:
    import time
    from tokenizer import Tokenizer
    from corrector import Corrector
except ImportError as ie:
    print(f"IMPORT ERROR -> {ie}")


class Vectorizer(object):
    """ Class used for word vectorization

    """

    def __init__(self):
        pass