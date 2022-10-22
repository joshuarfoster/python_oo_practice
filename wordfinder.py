"""Word Finder: finds random words from a dictionary."""

import random

class WordFinder:
    """
    Random Generator of words from a source file
    """
    def __init__(self, file):
        """
        Reads the file and reports how many words read
        """
        dict_file = open(file)
        self.words = self.parse(dict_file)
        print(f"{len(self.words)} words read")
    
    def parse(self, dict_file):
        """
        Makes list of words
        """
        return [w.strip() for w in dict_file]
    
    def random(self):
        """
        Returns random word from file
        """
        return random.choice(self.words)

class SpecialWordFinder(WordFinder):
    """
    WordFinder that excludes coments and blank lines
    """
    def parse(self, dict_file):
        """Parse dict_file -> list of words, skipping blanks/comments."""

        return [w.strip() for w in dict_file
                if w.strip() and not w.startswith("#")]
    


