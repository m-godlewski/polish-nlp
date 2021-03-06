# -*- coding: utf-8 -*-
import time
import unicodedata
import traceback

from modules.data_manager import DataManager


class Cleaner(object):
    """ Class used for cleaning texts from unwanted marks.

    - lowercasing
    - removing punctuation
    - removing diacritical
    - removing stopwords
    - removing rare words TODO
    - removing frequent words TODO

    """

    def __init__(self):
        pass

    def lower(self, text: str) -> str:
        """ Returns lowercased text.

        Arguments:
            text {str} -- [text to lowercase]

        Returns:
            str -- [lowercased text]
        """
        return text.lower()

    def upper(self, text: str) -> str:
        """ Returns uppercased text.

        Arguments:
            text {str} -- [text to uppercase]

        Returns:
            str -- [uppercased text]
        """
        return text.upper()

    def has_punctuation(self, text: str) -> bool:
        """ Checking if text contains punctuation marks.

        Arguments:
            text {str} -- [text]

        Returns:
            bool -- True - if text have punctuation marks
                    False - if text don't have punctuation marks
        """
        punctuation_marks = DataManager().get_punctuation()
        for word in text:
            if word in punctuation_marks:
                return True
        return False

    def remove_punctuation(self, text: str) -> str:
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

    def has_diacritical(self, text: str) -> bool:
        """ Checking if text contains diacritical marks.

        Arguments:
            text {str} -- [text]

        Returns:
            bool -- [ True - if text have diacritical marks | False - if text don't have diacritical marks ]
        """
        diacritical_marks = DataManager().get_diacritical()
        for word in text:
            if word in diacritical_marks:
                return True
        return False

    def remove_diacritical(self, text: str) -> str:
        """ Removing diacritical marks from text.

        Arguments:
            text {str} -- [text]

        Returns:
            str -- [text without diacritical marks]
        """
        diacritical_marks_map = DataManager().get_diacritical_map()
        for key, value in diacritical_marks_map.items():
            # replacing lowercase marks
            text = text.replace(key, value)
            # replacing uppercase marks
            text = text.replace(key.upper(), value.upper())
        return text

    def has_stopwords(self, text: str) -> bool:
        """ Checking if text contains stopwords marks.

        Arguments:
            text {str} -- [text]

        Returns:
            bool -- [ True - if text have stopwords marks | False - if text don't have stopwords marks ]
        """
        stopwords = DataManager().get_stopwords()
        for word in text.split():
            if word in stopwords:
                return True
        return False

    def remove_stopwords(self, text: str) -> str:
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