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
        self.DATA_FILES = {
            "punctuation" : self.DATA_PATH + "polish_punctuation.txt",
            "stopwords" : self.DATA_PATH + "polish_stopwords.txt",
            "diacritical" : self.DATA_PATH + "polish_diacritical.txt"
        }
    
    def get_punctuation(self) -> Iterable[str]:
        """ Return list of punctuation marks from file.
        
        Returns:
            Iterable[str] -- [list of punctuation marks]
        """
        data = pandas.read_fwf(self.DATA_FILES["punctuation"])
        punctuation_marks = [ "".join(mark) for mark in data.values.tolist() ]
        return punctuation_marks

    def get_diacritical(self) -> Iterable[str]:
        """ Return list of diacritical marks from file.
        
        Returns:
            Iterable[str] -- [list of diacritical marks.]
        """
        diacritical_marks = {} # initialization of empty polish mark map
        data = pandas.read_fwf(self.DATA_FILES["diacritical"], delimiter=",", header = None).values
        for row in data:
            diacritical_marks[row[0]] = row[1] # {polish_mark = clear_mark}
        return diacritical_marks


    def get_stopwords(self) -> Iterable[str]:
        """ Return list of stopwords.
        
        Returns:
            Iterable[str] -- [list of stopwords]
        """
        data = pandas.read_fwf(self.DATA_FILES["stopwords"])
        stopwords = [ "".join(mark) for mark in data.values.tolist() ]
        return stopwords