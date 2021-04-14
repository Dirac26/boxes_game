from entities import grass, rock, hole, player, box, empty
from abc import ABC, abstractmethod
r = rock()
p = player()
b1 = box()
b2 = box()
b3 = box()

e = empty()

h1 = hole(e)
h2 = hole(e)
h3 = hole(e)

class Map(ABC):    
    def __iter__(self):
        self.i = 0
        self.j = 0
        return self
    @abstractmethod
    def get_player(self):
        pass
    @abstractmethod
    def get_name(self):
        pass
    @abstractmethod
    def __len__(self):
        pass

class Map1(Map):
    def __init__(self):
        self.level = [
            [grass(r), grass(r), grass(r), grass(r), grass(r), grass(r), grass(r), grass(r)], 
            [grass(r), grass(p), grass(b1), h1, grass(r), grass(r), grass(r), grass(r)],
            [grass(r), grass(e), grass(b3), h2, h3, grass(e), grass(r), grass(r)],
            [grass(r), grass(e), grass(e), grass(r), grass(r), grass(e), grass(r), grass(r)],
            [grass(r), grass(r), grass(e), grass(e), grass(r), grass(e), grass(e), grass(r)],
            [grass(r), grass(r), grass(b2), grass(e), grass(e), grass(e), grass(e), grass(r)],
            [grass(r), grass(r), grass(e), grass(e), grass(r), grass(r), grass(r), grass(r)],
            [grass(r), grass(r), grass(r), grass(r), grass(r), grass(r), grass(r), grass(r)],
    ]

    def get_player(self):
        return p
    
    def get_name(self):
        return "level 1"

    def __len__(self):
        return len(self.level[0])



