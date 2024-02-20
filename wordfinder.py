from random import choice

class WordFinder:
    """Word Finder: finds random words from a dictionary."""

    def __init__(self, path):
        """Creates attribute words and assigns it to be a list of words
        in the file found at the input path
        Also creates attribute path which saves the input path"""

        self.path = path
        self.words = self.__read_file__(path)

    def __repr__(self):
        """Returns representation of instance of WordFinder class"""
        return f"WordFinder created from {self.path}"


    def __read_file__(self, path):
        """Takes in file path and returns list of words in that file
        If file does not exist then it prints 'File does not exist' and
        returns an empty list"""

        words = []

        try:
            file = open(path)
            for line in file:
                words.append(line.rstrip())
            file.close()

        except FileNotFoundError:
            print('File does not exist')

        return words

    def random(self):
        """Returns a random word from self.words"""
        return choice(self.words)