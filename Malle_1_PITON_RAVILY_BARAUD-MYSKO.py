from random import randint
import pygame as pg

pg.init()

def Fleury_and_bott(monnaie: int) -> dict:
    """
    Fonction permettant de savoir le nombre de
    billets/pièces à rendre pour un montant donné

    Entrée: Montant à rendre
    Sortie: Dictionnaire comprenant la valeur de
            le pièce/du billet et le nombre à rendre 
    """
    assert type(monnaie) == int, "Vous devez rentrer un nombre conforme"

    monnaie_dispo = (500, 200, 100, 50, 20, 10, 5, 2, 1)
    monnaie_rendue = {500 : 0, 200 : 0, 100 : 0, 50 : 0,
                    20 : 0, 10 : 0, 5 : 0, 2 : 0, 1 : 0}
    for billet in monnaie_dispo:
        while monnaie >= billet:
            monnaie -= billet
            monnaie_rendue[billet] += 1

    return monnaie_rendue

print(Fleury_and_bott(0))
print(Fleury_and_bott(60))
print(Fleury_and_bott(63))
print(Fleury_and_bott(231))
print(Fleury_and_bott(899))


def Guipure(rendu:int) -> dict:
    assert type(rendu) == int

    caisse_dispo = {200 : 1, 100 : 3, 50 : 1 , 20 : 1, 10: 1, 2 :5}
    rendu_caisse ={200 : 0, 100 : 0, 50 : 0, 20 : 0, 10: 0, 2 : 0}
    
    for thune in caisse_dispo:
        while rendu >= thune:
            rendu -= thune
            rendu_caisse[thune] += 1
    
    return rendu_caisse


print(Guipure(0))
print(Guipure(8))
print(Guipure(62))
print(Guipure(231))
print(Guipure(497))
print(Guipure(842))


