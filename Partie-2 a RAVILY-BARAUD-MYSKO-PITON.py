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
'''
On définit une fonction remplissage_malle.
Entrée:On va chercher dans la liste des fournitures les éléments dans l'ordre
Sortie:On renvoye la fonction malle_harry ou on a rempli avec les éléments dans l'ordre sans dépasser le poids maximal
'''
def remplissage_malle(fournitures):
    malle_harry = []    
    poids_max = 4
    
    for element in fournitures:
        if element['Poids'] <= poids_max :
            malle_harry.append(element)
            poids_max -= element['Poids']

    return malle_harry

nouvelle_malle = remplissage_malle(fournitures_scolaires)
print(nouvelle_malle)