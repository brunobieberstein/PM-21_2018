import random

caves = [1,2,3]
counter_andromeda_in_original_cave = 0
counter_andromeda_in_third_cave = 0

def kein_monster():
    monster_liste = [1,2,3]
    monster_liste.remove(random.choice(caves))
    return monster_liste

def wahl_1(caves):
    wahl_1 = random.choice(caves)
    return wahl_1

def tipp(monster_liste, wahl_1):
    if wahl_1 in monster_liste:
        x = 1
        tipp_liste = monster_liste[:]
        tipp_liste.remove(wahl_1)
        tipp = random.choice(tipp_liste)
    else:
        tipp = random.choice(monster_liste)
        x = 0
    return tipp, x



trials = 10000
for trial in range(trials):
    counter_andromeda_in_third_cave += tipp(kein_monster(),wahl_1(caves))[1]

print(
    'Reconsidering his original choice would have been good for Perseus in '
    '{0} out of {1} cases.'.format(counter_andromeda_in_third_cave, trials)
    )
    
