from entities import grass, rock, hole, player, box, empty

r = rock()
p = player()
b1 = box()
b2 = box()
b3 = box()

e = empty()

h1 = hole(e)
h2 = hole(e)
h3 = hole(e)



level_1 = [
           [grass(r), grass(r), grass(r), grass(r), grass(r), grass(r), grass(r), grass(r)], 
           [grass(r), grass(e), grass(b1), h1, grass(r), grass(r), grass(r), grass(r)],
           [grass(r), grass(e), grass(e), h2, h3, grass(p), grass(r), grass(r)],
           [grass(r), grass(e), grass(e), grass(r), grass(r), grass(b3), grass(r), grass(r)],
           [grass(r), grass(r), grass(e), grass(e), grass(r), grass(e), grass(e), grass(r)],
           [grass(r), grass(r), grass(b2), grass(e), grass(e), grass(e), grass(e), grass(r)],
           [grass(r), grass(r), grass(e), grass(e), grass(r), grass(r), grass(r), grass(r)],
           [grass(r), grass(r), grass(r), grass(r), grass(r), grass(r), grass(r), grass(r)],

]

def get_level_1():
    level_1_dict = {}
    for i, row in enumerate(level_1):
        for j, val in enumerate(row):
            level_1_dict[(j, i)] = val
    return level_1_dict, p, h1, h2, h3


