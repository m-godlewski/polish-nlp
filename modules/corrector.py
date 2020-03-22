try:
    import time
except ImportError as ie:   
    print(f"Import error in {__name__} ---> {ie}")


class Corrector(object):
    """ Class used for correcting misspells.
    
    """

    def __init__(self):
        pass