# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 09:22:23 2022

@author: BARAUD--MYSKO
"""


fournitures_scolaires = \
[{'Nom' : 'Manuel scolaire', 'Poids' : 0.55, 'Mana' : 11},
{'Nom' : 'Baguette magique', 'Poids' : 0.085, 'Mana' : 120},
{'Nom' : 'Chaudron', 'Poids' : 2.5, 'Mana' : 2},
{'Nom' : 'Boîte de fioles', 'Poids' : 1.2, 'Mana' : 4},
{'Nom' : 'Téléscope', 'Poids' : 1.9, 'Mana' : 6},
{'Nom' : 'Balance de cuivre', 'Poids' : 1.3, 'Mana' : 3},
{'Nom' : 'Robe de travail', 'Poids' : 0.5, 'Mana' : 8},
{'Nom' : 'Chapeau pointu', 'Poids' : 0.7, 'Mana' : 9},
{'Nom' : 'Gants', 'Poids' : 0.6, 'Mana' : 25},
{'Nom' : 'Cape', 'Poids' : 1.1, 'Mana' : 13}]



def remplissage_max(fournitures: list, poids_max: int) -> list:
    """
    Remplis une liste avec le plus d'éléments possibles sans que
    la somme de leurs poids ne dépasse un poids maximal.

    Entrée : La liste des fournitures
    Sortie : La liste des éléments remplis au maximum
    """
    poids_liste = []
    for element in fournitures:
        poids_liste.append(element["Poids"])
    

    for i in range (1, len(poids_liste)):
        while poids_liste[i] < poids_liste[i - 1] and i > 0:
            poids_liste[i], poids_liste[i - 1] = poids_liste[i - 1],\
                poids_liste[i]
            i = i - 1

    somme_poids = 0
    liste_poids = []
    for i in reversed(poids_liste):
        if somme_poids + i < poids_max:
            somme_poids += i
            liste_poids.append(i)

    malle_max = []
    for element in fournitures_scolaires:
        for poids in liste_poids:
            if poids == element["Poids"]:
                malle_max.append(element)

    return(malle_max)

print(remplissage_max(fournitures_scolaires, 4))



