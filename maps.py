from entities import grass, rock, hole, player, box, empty
from abc import ABC, abstractmethod
r = rock()
p = player()
e = empty()

class Map(ABC):    
    def __iter__(self):
        self.i = 0
        self.j = 0
        yield self

    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def __len__(self):
        pass

    def get_level(self):
        return self.level

    def get_player(self):
        return p

class Map1(Map):
    def __init__(self):
        self.level = [
            [grass(r), grass(r), grass(r), grass(r), grass(r), grass(r), grass(r), grass(r)], 
            [grass(r), grass(p), grass(box()), hole(e), grass(r), grass(r), grass(r), grass(r)],
            [grass(r), grass(e), grass(box()), hole(e), hole(e), grass(e), grass(r), grass(r)],
            [grass(r), grass(e), grass(e), grass(r), grass(r), grass(e), grass(r), grass(r)],
            [grass(r), grass(r), grass(e), grass(e), grass(r), grass(e), grass(e), grass(r)],
            [grass(r), grass(r), grass(box()), grass(e), grass(e), grass(e), grass(e), grass(r)],
            [grass(r), grass(r), grass(e), grass(e), grass(r), grass(r), grass(r), grass(r)],
            [grass(r), grass(r), grass(r), grass(r), grass(r), grass(r), grass(r), grass(r)],
    ]
    def get_name(self):
        return "level 1"

    def __len__(self):
        return len(self.level[0])

class Map2(Map):
    def __init__(self):
        self.level = [
            [grass(r), grass(r), grass(r), grass(r), grass(r), grass(r), grass(r), grass(r), grass(r), grass(e), grass(e), hole(e), grass(r), grass(r), grass(r), grass(r)], 
            [grass(r), grass(p), grass(box()), hole(e), grass(r), grass(r), grass(r), grass(r), grass(r), grass(e), grass(e), hole(e), grass(r), grass(r), grass(r), grass(r)],
            [grass(r), grass(r), grass(box()), hole(e), hole(e), grass(e), grass(r), grass(r), grass(r), grass(e), grass(e), hole(e), grass(r), grass(r), grass(r), grass(r)],
            [grass(r), grass(e), grass(e), grass(r), grass(r), grass(e), grass(r), grass(r), grass(r), grass(e), grass(e), grass(e), grass(r), grass(r), grass(r), grass(r)],
            [grass(r), grass(r), grass(e), grass(e), grass(r), grass(e), grass(e), grass(r), grass(r), grass(e), grass(e), grass(e), grass(r), grass(r), grass(r), grass(r)],
            [grass(r), grass(r), grass(box()), grass(e), grass(e), grass(e), grass(e), grass(r), grass(r), grass(e), grass(e), grass(e), grass(r), grass(r), grass(r), grass(r)],
            [grass(r), grass(r), grass(e), grass(e), grass(r), grass(r), grass(r), grass(r), grass(r), grass(e), grass(e), grass(e), grass(r), grass(r), grass(r), grass(r)],
            [grass(r), grass(r), grass(e), grass(e), grass(r), grass(r), grass(r), grass(r), grass(r), grass(e), grass(e), grass(e), grass(r), grass(r), grass(r), grass(r)],
            [grass(r), grass(r), grass(e), grass(e), grass(r), grass(r), grass(r), grass(r), grass(r), grass(e), grass(e), grass(e), grass(r), grass(r), grass(r), grass(r)],
            [grass(r), grass(r), grass(e), grass(e), grass(r), grass(r), grass(r), grass(r), grass(r), grass(e), grass(e), grass(e), grass(r), grass(r), grass(r), grass(r)],
            [grass(r), grass(r), grass(e), grass(e), grass(r), grass(r), grass(r), grass(r), grass(r), grass(e), grass(e), grass(e), grass(r), grass(r), grass(r), grass(r)],
            [grass(r), grass(r), grass(e), grass(e), grass(r), grass(r), grass(r), grass(r), grass(r), grass(e), grass(e), grass(e), grass(r), grass(r), grass(r), grass(r)],
            [grass(r), grass(r), grass(e), grass(e), grass(r), grass(r), grass(r), grass(r), grass(r), grass(e), grass(e), grass(e), grass(r), grass(r), grass(r), grass(r)],
            [grass(r), grass(r), grass(e), grass(e), grass(r), grass(r), grass(r), grass(r), grass(r), grass(e), grass(e), grass(e), grass(r), grass(r), grass(r), grass(r)],
            [grass(r), grass(r), grass(r), grass(r), grass(r), grass(r), grass(r), grass(r), grass(r), grass(e), grass(e), grass(e), grass(r), grass(r), grass(r), grass(r)]
    ]
    def get_name(self):
        return "level 2"

    def __len__(self):
        return len(self.level[0])




