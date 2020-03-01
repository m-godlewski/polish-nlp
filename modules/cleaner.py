try:
    import time
    from data_manager import DataManager
except ImportError as ie:
    print(f"IMPORT ERROR -> {ie}")


class Cleaner(object):
    """ Class used for cleaning texts from unwanted signs.

    - lowering
    - removing punctuation
    - removing diacritical
    - removing stopwords
    - removing rarewords
    - removing frequent words
    
    """

    def __init__(self):
        pass

    def lower(self, text:str) -> str:
        """ Returns lowercased wersion of text given as argument.
        
        Arguments:
            text {str} -- [text to lowercase]
        
        Returns:
            str -- [lowercased text]

        """
        return text.lower()

    def remove_punctuation(self, text:str) -> str:
        """ Returns text without punctuation marks.
        
        Arguments:
            text {str} -- [text]
        
        Returns:
            str -- [text without punctuation]
        """
        punctuation_marks = DataManager().get_punctuation()
        for mark in punctuation_marks:
            text = text.replace(mark, "")
        return text