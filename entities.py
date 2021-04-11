from abc import ABC, abstractclassmethod

class block(ABC):
    def __init__(self, content):
        self.content = content

class grass(block):
    pass

class hole(block):
    pass



class content(ABC):
    pass

class rock(content):
    pass

class box(content):
    pass

class player(content):
    pass

class empty(content):
    pass
