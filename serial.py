"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self,start):
        """
        Create serial generator starting at start
        """
        self.start = start
        self.current = start
    
    def generate(self):
        """
        Generate the next number in succession
        """
        print(self.current)
        self.current = self.current + 1

    def reset(self):
        """
        Reset to the original start
        """
        self.current = self.start
