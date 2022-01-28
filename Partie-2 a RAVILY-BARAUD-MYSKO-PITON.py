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



for element in fournitures_scolaires:
    element['Ratio'] = element['Mana'] / element['Poids']


for i in range(len(fournitures_scolaires) - 1):
    indice_du_mini = i
    for j in range(i + 1, len(fournitures_scolaires)) :
        if fournitures_scolaires[j]['Ratio'] < fournitures_scolaires[indice_du_mini]['Ratio']:
            indice_du_mini = j
    fournitures_scolaires[i], fournitures_scolaires[indice_du_mini] = fournitures_scolaires[indice_du_mini], fournitures_scolaires[i]

print(fournitures_scolaires)