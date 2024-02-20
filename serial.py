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

    def __init__(self, start):
        """Initializes instance variables start and value"""
        self.start = self.next = start

    def __repr__(self):
        return f"Start value is {self.start}. Current value is {self.next}"

    def generate(self):
        """Increments instance variable value and then returns it"""
        self.next += 1
        return self.next - 1

    def reset(self):
        """Resets instance variable value to the starting value"""
        self.next = self.start