class Author:
    def __init__(self, name):
        self.name = name

class Book:
    def __init__(self, title):
        if not isinstance(title, str):
            raise TypeError("Title must be a string")
        self.title = title



class Contract:
    pass

