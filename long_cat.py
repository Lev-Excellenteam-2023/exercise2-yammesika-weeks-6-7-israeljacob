import re


def count_words(words: str) -> dict:
    """
    Counts the number of alphabetic words in a string and returns a dictionary with word lengths.

    Parameters:
        words (str): The input string containing words.

    Returns:
        dict: A dictionary with words as keys and their lengths as values.
    """
    return {word: len(word) for word in re.split('([A-z]+)', words) if word.isalpha()}