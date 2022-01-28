

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
POIDS_MAXIMUM = 4 
def max_mana(fournitures, poids_max):
    '''
    Entrée : Objets de la table fournitures scolaires
    Sortie : Objets de la tables fournitures triéq par mana et ne dépassant pas la capacité de poids
    
    '''
    liste_objet = []
    for i in range(len(fournitures_scolaires)):
        temp = fournitures_scolaires[i]
        indice = i- 1
        while temp['Mana'] > fournitures[indice]['Mana'] and indice >= 0:
            fournitures[indice+1] = fournitures[indice]
            indice -= 1
            fournitures[indice + 1] = temp
    
    for element in fournitures: 
        if element['Poids'] < poids_max:
            liste_objet.append(element)
            poids_max -= element['Poids']
    return liste_objet

nouvelle_malle = max_mana(fournitures_scolaires, POIDS_MAXIMUM)
print(nouvelle_malle)



poids_total = 0
mana_total= 0
for element in nouvelle_malle:
        poids_total += element['Poids']
        mana_total += element['Mana']
print(f'Le poids total de la malle est {poids_total}')
print(f'Le mana total de la malle est {mana_total}')


