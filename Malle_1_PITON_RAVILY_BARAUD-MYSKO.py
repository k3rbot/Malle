from random import randint

def Fleury_and_bott(monnaie):
    monnaie_dispo = (500, 200, 100, 50, 20, 10, 5, 2, 1)
    monnaie_rendue = {500 : 0, 200 : 0, 100 : 0, 50 : 0,
                    20 : 0, 10 : 0, 5 : 0, 2 : 0, 1 : 0}
    while monnaie != 0:
        for billet in monnaie_dispo:
            if monnaie >= billet:
                monnaie -= billet
                monnaie_rendue[billet] += 1

    return monnaie_rendue

print(Fleury_and_bott(0))
print(Fleury_and_bott(60))
print(Fleury_and_bott(63))
print(Fleury_and_bott(231))
print(Fleury_and_bott(899))
