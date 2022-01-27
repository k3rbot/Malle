


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

def max_mana(fournitures):

    new_mana = []
    for element in fournitures :
            new_mana.append(element)


    for i in range (1, len(new_mana)):
        while new_mana[i] < new_mana[i - 1] and i > 0:
            new_mana[i], new_mana[i - 1] = new_mana[i - 1], new_mana[i]
            i = i - 1
    
    
    
    poids_total = 0
    liste_du_poids = []
    for j in new_mana :
        poids_total += j
        liste_du_poids.append(element('Poids'))
        if poids_total > 4:
            poids_total -= j
            liste_du_poids.remove(j)
            break





