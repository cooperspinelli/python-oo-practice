class WordFinder:
    """Word Finder: finds random words from a dictionary."""
    # init function takes in a string--> represents a path
    # make a list of the words
    # get len of list

    # call helper function (random()) in a try catch block--> if file doesnt exist
    # function called 'read file' inside the path ^

    def __init__(self, path):
        try:
            self.words = self.__read_file__(path)

        except FileNotFoundError:
            print('File does not exist')

    def __read_file__(self, path):
        # takes in a file path--> either return a list of words present, or error
        # if not found
        words = []

        file = open("/my/file.txt")

        for line in file:
            words.append(line.rstrip())

        file.close()
        return words
