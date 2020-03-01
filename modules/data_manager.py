try:
    import time
    import pandas
    from typing import Iterable
except ImportError as ie:
    print(f"IMPORT ERROR -> {ie}")


class DataManager(object):
    """ Class used for managing polish linguistics data storaged in files.
    
    """

    def __init__(self):
        self.DATA_PATH = "../data/"
        self.PUNCTUATION_FILE = self.DATA_PATH + "polish_punctuation.txt"
    
    def get_punctuation(self) -> Iterable[str]:
        """ Return list of punctuation marks from file.
        
        Returns:
            Iterable[str] -- [list of punctuation marks]
        """
        data = pandas.read_fwf(self.PUNCTUATION_FILE)
        punctuation_marks = [ "".join(mark) for mark in data.values.tolist() ]
        return punctuation_marks

    def get_stopwords(self):
        pass