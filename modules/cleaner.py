try:
    import time
    import unicodedata
    from data_manager import DataManager
except ImportError as ie:
    print(f"IMPORT ERROR -> {ie}")


class Cleaner(object):
    """ Class used for cleaning texts from unwanted marks.

    - lowering
    - removing punctuation
    - removing diacritical
    - removing stopwords
    - removing rarewords
    - removing frequent words
    TODO - add is_x methods - checking correctivity of given word/sentence
    
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
        """ Removing punctuation marks from text.
        
        Arguments:
            text {str} -- [text]
        
        Returns:
            str -- [text without punctuation]
        """
        punctuation_marks = DataManager().get_punctuation()
        for mark in punctuation_marks:
            text = text.replace(mark, "")
        return text

    def remove_diacritical(self, text:str) -> str:
        """ Removing diacritical marks from text.
        
        Arguments:
            text {str} -- [text]
        
        Returns:
            str -- [text without diacritical marks]
        """
        diacritical = DataManager().get_diacritical()
        for key, value in diacritical.items():
            text = text.replace(key, value) # replacing lowercase marks
            text = text.replace(key.upper(), value.upper()) # replacing uppercase marks
        return text

    def remove_stopwords(self, text:str) -> str:
        """ Removing stopwords from text.
        
        Arguments:
            text {str} -- [text]
        
        Returns:
            str -- [text without stopwords]
        """
        stopwords = DataManager().get_stopwords()
        for mark in stopwords:
            text = text.replace(mark, "")
        return text