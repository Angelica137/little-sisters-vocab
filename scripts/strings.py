import string


def add_prefix_un(word: str) -> str:
    """"
    This function takes `word` as a paramater and returns a new word with an 'un' prefix.
    """
    return 'un' + word  # O(n^2)


def make_word_groups(vocab_words: list) -> str:
    """
    This function takes a `vocab_words` list and returns a strong with the prefix and the words with the prefix applied, separated by '::'.
    """
    return (' :: ' + vocab_words[0]).join(vocab_words)  # O(n)


def remove_suffix_ness(word: str) -> str:
    """
    This function takes in a word and returns the base word with `ness` removed
    """
    root = word[:-4]
    return root[:-1] + 'y' if (root.endswith('i')) else word[:-4]


def adjective_to_verb(sentence: str, index: int) -> str:
    """
    This function takes a `sentence` using the vocablulary word and the `index` of the word.
    The function returns the extracted adjective as a verb.

    words = sentence.translate(str.maketrans(
        '', '', string.punctuation)).split()
    return words[index] + 'en'
    """
    return word + 'en' if (word := sentence.split(" ")[index])[-1] not in string.punctuation else word[:-1] + 'en'
