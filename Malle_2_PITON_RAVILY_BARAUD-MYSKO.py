from msilib import Binary
import os
import pygame as pg

pg.init()

os.environ["SDL_VIDEO_CENTERED"] = "1"  # On centre la fenêtre PyGame
# On initialise la fenêtre de 1624 par 1080 pixels (la taille de la photo)
screen = pg.display.set_mode((1624, 1080))

pg.event.set_allowed([pg.QUIT, pg.KEYDOWN])


# On définit plusieurs couleurs au format rgb
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (34, 139, 34)
VIOLET = (128, 0, 128)
YELLOW = (255, 255, 0)
TRANSPARENT_YELLOW = (255, 240, 0, 85)
ORANGE = (255, 140, 0)
GREY = (225, 200, 200)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# On "génère" la police d'écriture Harry Potter en 100 tailles différentes;
# Si on la "générais" au moment de l'utiliser on utiliserai énormément 
# le disque dur et on perdrai du temps inutilement
# En faisant ainsi on multiplie par 2 voire 3 le nombre de FPS
Font = []
for i in range(100):
    Font.append(pg.font.Font("HarryPotterFont.ttf", i))

# On charge les différentes images
IMG_CHEMIN = pg.image.load("chemin_de_traverse.png").convert()
IMG_MALKIN = pg.image.load("malkin_shop.jpg").convert()
IMG_OLLIVANDER = pg.image.load("ollivander_shop.jpg").convert()
IMG_FLOURISH_AND_BLOTTS = pg.image.load("flourish_and_blotts_shop.jpg").convert()
IMG_MALLE = pg.transform.rotozoom(pg.image.load("Malle-Harry-Potter.png"), 0, 1.05).convert_alpha()
IMG_MALLE_OPEN = pg.image.load("Malle-Harry-Potter-ouverte.png").convert_alpha()

# On définit la vitesse de rafraichissement à 30 FPS
clock = pg.time.Clock()
FPS = 60

# On définit le titre de la fenêtre
pg.display.set_caption("Harry Potter se fait la malle au chemin de traverse")

# Polygone d'une boutique
OLLIVANDER_CORDS = (
    (781, 704), (784, 711), (815, 709), (818, 716),
    (871, 718), (871, 485), (848, 483), (830, 484),
    (816, 488), (808, 495), (813, 501), (816, 507),
    (814, 513), (807, 514), (802, 509), (796, 504),
    (787, 508), (772, 512), (778, 530), (780, 582),
    (778, 584), (778, 596), (783, 602), (783, 669),
    (784, 677), (780, 707)
)
# La surface sur laquelle on met notre polygone et qui accepte la notion de transparence
ollivander_poly = pg.Surface((1634, 1080), flags=pg.SRCALPHA)
OLLIVANDER_RECT = pg.draw.polygon(ollivander_poly, TRANSPARENT_YELLOW, OLLIVANDER_CORDS)

FLOURISH_AND_BLOTTS_CORDS = (
    (1243, 451), (1426, 381), (1456, 338), (1486, 308),
    (1523, 279), (1558, 256), (1621, 239), (1622, 859),
    (1578, 847), (1578, 837), (1522, 833), (1283, 790),
    (1281, 740), (1275, 732), (1283, 724), (1271, 524),
    (1270, 509), (1271, 504), (1270, 480), (1262, 473),
    (1255, 472), (1252, 467), (1249, 467), (1244, 458),
    (1241, 447)
)
flourish_and_blotts_poly = pg.Surface((1634, 1080), flags=pg.SRCALPHA)
FLOURISH_AND_BLOTTS_RECT = pg.draw.polygon(flourish_and_blotts_poly, TRANSPARENT_YELLOW, FLOURISH_AND_BLOTTS_CORDS)

MALKIN_CORDS = (
    (294, 804), (295, 503), (291, 482), (286, 468),
    (309, 431), (319, 425), (400, 424), (412, 432),
    (417, 446), (423, 469), (424, 496), (436, 502),
    (428, 510), (424, 515), (436, 517), (448, 525),
    (455, 534), (451, 537), (444, 543), (443, 566),
    (450, 570), (446, 580), (439, 584), (439, 728),
    (444, 729), (439, 735), (438, 750), (372, 756),
    (373, 777), (338, 802), (317, 803), (307, 809)
)
malkin_poly = pg.Surface((1634, 1080), flags=pg.SRCALPHA)
MALKIN_RECT = pg.draw.polygon(malkin_poly, TRANSPARENT_YELLOW, MALKIN_CORDS)

MALLE_CORDS = (
    (649, 811), (858, 791), (868, 792), (957, 819),
    (962, 822), (968, 827), (968, 942), (964, 949),
    (754, 983), (748, 982), (647, 935), (644, 930),
    (642, 924), (643, 816), (645, 813), (649, 811)
)
malle_poly = pg.Surface((1634, 1080), flags=pg.SRCALPHA)
MALLE_RECT = pg.draw.polygon(malle_poly, TRANSPARENT_YELLOW, MALLE_CORDS)

# On prépare une surface sur laquelle on met un rectangle noir 
# semi-transparent pour réduire la luminosité de l'image derrière
dim = pg.Surface((1634, 1080), flags=pg.SRCALPHA)
pg.draw.rect(dim, (0, 0, 0, 150), (0, 0, 1664, 1080))

# Tous les tests à faire pour chaque maisons
OLLIVANDER_TESTS = ('0;0;0', '0;0;654', '0;23;78', '2;11;9', '7;531;451')
FLOURISH_AND_BLOTTS_TESTS = ('0', '60', '63', '231', '899')
MALKIN_TESTS = ('0', '8', '62', '231', '497', '842')

# Les fournitures pour la malle d'Harry
SCHOLAR_FURNITURES = [
    {'Nom': 'Manuel scolaire', 'Poids': 0.55, 'Mana': 11},
    {'Nom': 'Baguette magique', 'Poids': 0.085, 'Mana': 120},
    {'Nom': 'Chaudron', 'Poids': 2.5, 'Mana': 2},
    {'Nom': 'Boîte de fioles', 'Poids': 1.2, 'Mana': 4},
    {'Nom': 'Téléscope', 'Poids': 1.9, 'Mana': 6},
    {'Nom': 'Balance de cuivre', 'Poids': 1.3, 'Mana': 3},
    {'Nom': 'Robe de travail', 'Poids': 0.5, 'Mana': 8},
    {'Nom': 'Chapeau pointu', 'Poids': 0.7, 'Mana': 9},
    {'Nom': 'Gants', 'Poids': 0.6, 'Mana': 25},
    {'Nom': 'Cape', 'Poids': 1.1, 'Mana': 13}
]
MAX_WEIGHT = 4


def display_text(text: str, font: list, size: int, color: tuple, x: int, y: int, alignment=1):
    """
    Fonction permettant l'affichage d'un texte

    Entrée: text: Le texte à afficher
            font: La police d'écriture sous forme d'un tableau de polices toutes les tailles (100 max ici)
            size: La taille de la police
            color: La couleur de la police de type (r, g, b)
            x: L'emplacement du texte sur l'axe horizontal
            y: L'emplacement du texte sur l'axe horizontal
            alignment: Alignement du texte, 
                        0: Texte aligné à gauche,
                        1: Texte centré
                        2: Texte aligné à droite
    """
    assert size <= 100, "Size limit exceeded"
    assert alignment == 0 or alignment == 1 or alignment == 2, "Alignment not valid"

    text = font[size].render(text, 0, color)
    text_rect = text.get_rect()
    if alignment == 0:  # Alignement à gauche
        screen.blit(text, (x, y))
    elif alignment == 1:  # Alignement au centre
        screen.blit(text, (x - (text_rect[2]/2), y))
    else:  # Alignement à droite
        screen.blit(text, (x - text_rect[2], y))


def rectangle_text(pos: tuple, text: str, size: int, color: list) -> pg.Rect:
    """
    Fonction affichant un rectangle contenant du texte

    Entrée: La position du rectangle (en partant de l'angle du haut à gauche + 10 pixels)
            Le texte à afficher dans le rectangle
            La taille de la police d'écriture
    Sortie: Rect du rectangle affiché
    """
    shop_text = Font[size].render(text, 0, color)
    shop_text_rect = shop_text.get_rect()

    # On affiche le rectangle à doite puisqu'il y a de la place
    if shop_text_rect[2] + pos[0] + 26 <= 1624:
        pg.draw.rect(screen, BLACK, (pos[0] + 12, pos[1] + 2, shop_text_rect[2] + 11, 8 + shop_text_rect[3]))
        rect = pg.draw.rect(screen, WHITE, (pos[0] + 10, pos[1], shop_text_rect[2] + 15, 10 + shop_text_rect[3]), width=3)
        screen.blit(shop_text, (pos[0] + 15, pos[1] + 10))
    # Il n'y a pas de place à droite, on le met donc à gauche
    else:
        pg.draw.rect(screen, BLACK, (pos[0] - shop_text_rect[2] - 22, pos[1] + 2, shop_text_rect[2] + 16, 8 + shop_text_rect[3]))
        rect = pg.draw.rect(screen, WHITE, (pos[0] - shop_text_rect[2] - 25, pos[1], shop_text_rect[2] + 20, 10 + shop_text_rect[3]), width=3)
        screen.blit(shop_text, (pos[0] - shop_text_rect[2] - 15, pos[1] + 10))
    return rect


def user_entry(nb='', numbers=True) -> str:
    """
    Fonction permettant de récupérer les entrées de l'utilisateur

    Entrée: - variable sur lequelle sera concaténée ou écrasée la
    valeur de l'entrée utilisateur
            - bouléen pour avoir ou non les chiffres entrés par l'utilisateur
    Sortie: entrées de l'utilisateur
    """
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()
        elif event.type == pg.KEYDOWN:
            if numbers:
                if event.key == pg.K_KP0:
                    nb += '0'
                elif event.key == pg.K_KP1:
                    nb += '1'
                elif event.key == pg.K_KP2:
                    nb += '2'
                elif event.key == pg.K_KP3:
                    nb += '3'
                elif event.key == pg.K_KP4:
                    nb += '4'
                elif event.key == pg.K_KP5:
                    nb += '5'
                elif event.key == pg.K_KP6:
                    nb += '6'
                elif event.key == pg.K_KP7:
                    nb += '7'
                elif event.key == pg.K_KP8:
                    nb += '8'
                elif event.key == pg.K_KP9:
                    nb += '9'
                elif event.key == pg.K_BACKSPACE:
                    nb = nb[:-1]
            if (event.key == pg.K_RETURN or event.key == pg.K_KP_ENTER) and nb != '':
                nb += '\n'
                break
            elif event.key == pg.K_ESCAPE:
                nb = 'QUIT'
                break
            elif event.key == pg.K_RIGHT:
                nb += 'NEXT'
                break
            elif event.key == pg.K_LEFT:
                nb += 'PREVIOUS'
                break
    return nb


def flourish_and_blotts(monnaie: int) -> dict:
    """
    Fonction permettant de savoir le nombre de
    billets/pièces minimum à rendre pour un montant donné

    Entrée: Montant à rendre
    Sortie: Dictionnaire comprenant la valeur de
            le pièce/du billet et le nombre à rendre
    """
    assert type(monnaie) == int, "Vous devez rentrer un nombre conforme"

    monnaie_dispo = (500, 200, 100, 50, 20, 10, 5, 2, 1)
    monnaie_rendue = {500: 0, 200: 0, 100: 0, 50: 0,
                    20: 0, 10: 0, 5: 0, 2: 0, 1: 0, "impossible": False}
    for billet in monnaie_dispo:
        monnaie_rendue[billet] = monnaie // billet
        monnaie %= billet

    return monnaie_rendue


def malkin(rendu: int) -> dict:
    """
    Fonction permettant de savoir le nombre de
    billets/pièces minimum à rendre pour un montant donné
    avec un nombre de pièces/billets limités

    Entrée: Montant à rendre
    Sortie: Dictionnaire comprenant la valeur de
            le pièce/du billet et le nombre à rendre
            ! Si la valeur est trop élevée la fonction ne
            renverra rien
    """
    assert type(rendu) == int

    monnaie_dispo = {200: 1, 100: 3, 50: 1, 20: 1, 10: 1, 2: 5}
    rendu_caisse = {200: 0, 100: 0, 50: 0, 20: 0, 10: 0, 2: 0, "impossible": False}
    for billet in monnaie_dispo:
            while rendu >= billet and monnaie_dispo[billet] > 0:
                monnaie_dispo[billet] -= 1
                rendu -= billet
                rendu_caisse[billet] += 1
    if rendu > 0:
        rendu_caisse["impossible"] = True
    return rendu_caisse


def ollivander(monnaie:list) -> list:
    """
    Fonction permettant de savoir comment rendre une somme
    de noises, mornilles et gallions avec le moins de
    pièces possible.


    Entrée: Montant à rendre
    Sortie: L'équivalent en gallions, mornilles et noises
            rendus avec le moins de pièces possibles.
    """
    for i in range(3):
        if type(monnaie[i]) == str:
            monnaie[i] = int(monnaie[i])

    monnaie_rendue = [0, 0, 0]
    monnaie_rendue[1] = monnaie[2] // 29 + monnaie[1]
    monnaie_rendue[2] = monnaie[2] % 29
    monnaie_rendue[0] = monnaie_rendue[1] // 17 + monnaie[0]
    monnaie_rendue[1] %= 17

    return monnaie_rendue


def give_back(repaid: dict or list):
    """
    Fonction permettant d'afficher le rendu pour n'importe quelle boutique

    Entrée: Un dictionnaire comportant les différentes monnaie et leur nombre
    """
    if repaid == {}:
        return
    display_text("I'm giving you back :", Font, 70, ORANGE, 812, 450 if type(repaid) == dict else 580)
    i = 0
    for amount in repaid:
        if amount == "impossible":
            break
        if type(repaid) == list and amount > 0:
            i += 1
            display_text(f"{amount} {('Galleon' if i == 1 else ('Sickle' if i == 2 else 'Knut')) + ('s' if amount > 1 else '')}", Font, 80, GREEN, 630, 590 + 85*i, alignment=0)
        elif repaid[amount] > 0:
            i += 1
            display_text((f"{repaid[amount]} {('note' if amount > 2 else 'piece') + ('s' if repaid[amount] > 1 else '')} of {amount} euros")
            if type(amount) == int else f"{repaid[amount]} {amount}", Font, 50, GREEN, 600, 465 + 65*i, alignment=0)
    if type(repaid) == dict and repaid["impossible"]:
        display_text("Can't give you enough money !", Font, 70, GREEN, 812, 950, alignment=1)
    elif i == 0:
        display_text("Nothing !", Font, 70, GREEN, 812, 560 if type(repaid) == dict else 700, alignment=1)


def display_furnitures(furnitures: list):
    """
    Fonction permettant l'affichage des fournitures mises dans la valise d'Harry Potter
    avec le poids et le mana total

    Entrée: La liste des fournitures dans la valise
    """
    if furnitures == {}:
        return

    display_text("We have put in Harry's trunk:", Font, 70, GREY, 20, 180, alignment=0)
    weight, mana = 0, 0
    for i, elt in enumerate(furnitures):
        display_text('- 1 ' + elt["Nom"], Font, 60, BLACK, 80, 300 + i*80, alignment=0)
        weight += elt["Poids"]
        mana += elt["Mana"]
        if i == len(furnitures) - 1:
            display_text(f"Total mana: {mana}", Font, 60, BLUE, 40, 975, alignment=0)
            display_text(f"Total weight: {weight}", Font, 60, RED, 525, 975, alignment=0)


def all_possibilities(list):
    n = len(list)
    bin_list = []
    for i in range(2**n):
        nb_bin = bin(i)[2:]
        nb_bin = (n - len(nb_bin)) * '0' + nb_bin
        bin_list.append(nb_bin)

    elts_combination = []
    for str_bin in bin_list:
        combi = []
        for i, str in enumerate(str_bin):
            if str == '1':
                combi.append(list[i])
        elts_combination.append(combi)

    return elts_combination


def brute_force_management(list, max_weight):
    max_mana = 0
    for elts in list:
        weight = 0
        mana = 0
        for elt in elts:
            weight += elt["Poids"]
            mana += elt["Mana"]
        if weight <= max_weight and max_mana < mana:
            best = elts
            max_mana = mana
    return best


def wanky_management(fournitures, poids_max):
    malle_harry = []    

    for element in fournitures:
        if element['Poids'] <= poids_max :
            malle_harry.append(element)
            poids_max -= element['Poids']

    return malle_harry


def max_weight_management(fournitures):
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
    for i in poids_liste:
        somme_poids += i
        liste_poids.append(i)
        if somme_poids > 4:
            somme_poids -= i
            liste_poids.remove(i)
            break

    malle_max = []
    for element in SCHOLAR_FURNITURES:
        for poids in liste_poids:
            if poids == element["Poids"]:
                malle_max.append(element)
    
    return(malle_max)


def shop(shop: int):
    """
    Fonction permettant l'affichage et la gestion de n'importe quelle boutique

    Entrée: id de la boutique 0: Malkin, 1: Ollivander,
    2: Flourish and Blotts
    """
    assert shop == 0 or shop == 1 or shop == 2 or shop == 3, "Wrong shop id: Unexistant"

    nb = ''
    repaid = {}
    money_entered = ''
    money_list = (" euros", " galleons", " sickles", " knuts")
    previous_test = True
    previous_tests = [1]
    trunk_content = {}
    if shop == 0:
        money_type = 0
        previous_tests += list(MALKIN_TESTS)
    elif shop == 1:
        money_type = 1
        previous_tests += list(OLLIVANDER_TESTS)
    elif shop == 2:
        money_type = 0
        previous_tests += list(FLOURISH_AND_BLOTTS_TESTS)
    else:
        button_anything_rect = rectangle_text((1200, 300), "Take anything", 30, WHITE)
        button_weight_rect = rectangle_text((1200, 400), "Max weight", 30, WHITE)
        button_mana_rect = rectangle_text((1200, 500), "Max mana", 30, WHITE)
        button_ratio_rect = rectangle_text((1200, 600), "Best ratio mana/weight", 30, WHITE)
        button_best_rect = rectangle_text((1200, 700), "Best management", 30, WHITE)

    while 1:
        # On affiche l'image de la boutique et on l'assombrit
        if shop == 0:
            screen.blit(IMG_MALKIN, (0, 0))
            display_text("Welcome to Madam's Malkin shop !", Font, 90, VIOLET, 812, 100)
            screen.blit(dim, (0, 0))
        elif shop == 1:
            screen.blit(IMG_OLLIVANDER, (0, 0))
            display_text("Welcome to Ollivander's shop !", Font, 90, VIOLET, 812, 100)
            screen.blit(dim, (0, 0))
        elif shop == 2:
            screen.blit(IMG_FLOURISH_AND_BLOTTS, (0, 0))
            display_text("Welcome to Flourish and Blotts shop !", Font, 90, VIOLET, 812, 100)
            screen.blit(dim, (0, 0))
        else:
            screen.fill((255, 150, 0))
            screen.blit(IMG_MALLE_OPEN, (525, 250))
            display_text("Let's organize Harry's trunk !", Font, 90, VIOLET, 812, 50)
        display_text("press esc to go back to menu", Font, 20, WHITE, 10, 0, alignment=0)

        if shop != 3:
            display_text("Use right and left arrows to move through examples and history", Font, 20, WHITE, 1620, 1050, alignment=2)

            if previous_test:
                display_text("With :", Font, 90, YELLOW, 812, 250)
                nb = previous_tests[previous_tests[0]]
                nb += '\n'
                nb = user_entry(nb, numbers=False)
                if nb[-1:] == '\n' and nb[-2:] == '\n':
                    nb = nb[:-1]
            else:
                display_text("Enter amount :", Font, 70, YELLOW, 812, 250)
                nb = user_entry(nb)

            if nb == 'QUIT':
                return
            elif nb[-4:] == 'NEXT':
                if previous_tests[0] < (len(previous_tests) - 1) and previous_test:
                    previous_tests[0] += 1
                    nb = ''
                elif previous_test:
                    previous_test = False
                    nb = ''
                    money_entered = 0
                nb = nb[:-4]
            elif nb[-8:] == 'PREVIOUS':
                if previous_tests[0] > 1 and previous_test:
                    previous_tests[0] -= 1
                    nb = ''
                elif not(previous_test):
                    previous_test = True
                    nb = ''
                nb = nb[:-8]
            if nb[-1:] == '\n':
                if shop == 0:
                    money_entered = int(nb[:-1])
                    repaid = malkin(money_entered)
                    if not(previous_test):
                        previous_tests.append(str(money_entered))
                        previous_tests[0] += 1
                elif shop == 1:
                    if previous_test:
                        money_type = 3
                        nbs_entered = nb.split(';')
                        for i in range(3):
                            nbs_entered[i] = int(nbs_entered[i])
                    if money_type == 1:  # Gallions
                        money_type = 2
                        nbs_entered.append(int(nb[:-1]))
                    elif money_type == 2:  # Mornilles
                        money_type = 3
                        nbs_entered.append(int(nb[:-1]))
                    elif money_type == 3:  # Noises
                        if not(previous_test):
                            nbs_entered.append(int(nb[:-1]))
                            money_entered = ''
                            for i in range(3):
                                money_entered += str(nbs_entered[i]) + ';'
                            previous_tests.append(money_entered)
                            previous_tests[0] += 1
                        repaid = ollivander(nbs_entered)
                else:
                    money_entered = int(nb[:-1])
                    repaid = flourish_and_blotts(money_entered)
                    if not(previous_test):
                        previous_tests.append(str(money_entered))
                        previous_tests[0] += 1
                nb = ''
            if nb != '' and shop == 1 and money_type == 3 and len(nbs_entered) == 3:
                money_type = 1
                nbs_entered = []

            # Affichage du nombre entré
            if shop == 1:
                for i in range(money_type):
                    if i == money_type - 1:
                        display_text(nb + (str(nbs_entered[i]) if nb == '' and len(nbs_entered) > i else '') + money_list[i + 1], Font, 75, YELLOW, 812, 270 + 78*(i +1))
                    else:
                        display_text(str(nbs_entered[i]) + money_list[i + 1], Font, 60, YELLOW, 812, 270 + 78*(i +1))
            else:
                display_text(nb + (str(money_entered) if nb == '' else '') + money_list[money_type], Font, 80, YELLOW, 812, 350)
            if nb == '' and (shop != 1 or (shop == 1 and money_type == 3 and len(nbs_entered) == 3)):
                give_back(repaid)
        else:
            mouse_down = False
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()
                elif event.type == pg.MOUSEBUTTONDOWN:
                    mouse_down = True
                elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                    return
            mouse_pos = pg.mouse.get_pos()

            rectangle_text((1200, 300), "Take anything", 30, GREEN)
            rectangle_text((1200, 400), "Max weight", 30, GREEN)
            rectangle_text((1200, 500), "Max mana", 30, GREEN)
            rectangle_text((1200, 600), "Best ratio mana/weight", 30, GREEN)
            rectangle_text((1200, 700), "Best management", 30, GREEN)

            if button_anything_rect.collidepoint(mouse_pos[0], mouse_pos[1]):
                rectangle_text((1175, 290), "Take anything", 40, GREEN)
                if mouse_down:
                    trunk_content = wanky_management(SCHOLAR_FURNITURES, MAX_WEIGHT)
            elif button_weight_rect.collidepoint(mouse_pos[0], mouse_pos[1]):
                rectangle_text((1175, 390), "Max weight", 40, GREEN)
                if mouse_down:
                    trunk_content = max_weight_management(SCHOLAR_FURNITURES)
            elif button_mana_rect.collidepoint(mouse_pos[0], mouse_pos[1]):
                rectangle_text((1175, 490), "Max mana", 40, GREEN)
                if mouse_down:
                    print("Mana")
            elif button_ratio_rect.collidepoint(mouse_pos[0], mouse_pos[1]):
                rectangle_text((1175, 590), "Best ratio mana/weight", 40, GREEN)
                if mouse_down:
                    print("Ratio")
            elif button_best_rect.collidepoint(mouse_pos[0], mouse_pos[1]):
                rectangle_text((1175, 690), "Best management", 40, GREEN)
                if mouse_down:
                    trunk_content = brute_force_management(all_possibilities(SCHOLAR_FURNITURES), MAX_WEIGHT)
            display_furnitures(trunk_content)

        pg.display.update()
        clock.tick(FPS)


def alley(mouse_pos: tuple, pressed: bool):
    """
    Fonction affichant le menu de sélection de la boutique,
    elle est surlignée quand la souris passe dessus et si l'on
    clique on est transporté dedans

    Entrée: La position de la souris
    """
    # On affiche l'image du chemin de traverse
    screen.blit(IMG_CHEMIN, (0, 0))
    screen.blit(IMG_MALLE, (600, 750))
    display_text("press esc to exit", Font, 20, WHITE, 10, 0, alignment=0)
    # On surligne le magasin si on a la souris dessus
    if OLLIVANDER_RECT.collidepoint(mouse_pos[0], mouse_pos[1]):
        screen.blit(ollivander_poly, (0, 0))
        rectangle_text(mouse_pos, "Ollivander", 20, VIOLET)
        # Un bouton de la souris a été pressé
        if pressed:
            shop(1)
    elif FLOURISH_AND_BLOTTS_RECT.collidepoint(mouse_pos[0], mouse_pos[1]):
        screen.blit(flourish_and_blotts_poly, (0, 0))
        rectangle_text(mouse_pos, "Flourish and Blotts", 20, VIOLET)
        if pressed:
            shop(2)
    elif MALKIN_RECT.collidepoint(mouse_pos[0], mouse_pos[1]):
        screen.blit(malkin_poly, (0, 0))
        rectangle_text(mouse_pos, "Madam Malkin's Robes for All Occasions", 20, VIOLET)
        if pressed:
            shop(0)
    elif MALLE_RECT.collidepoint(mouse_pos[0], mouse_pos[1]):
        screen.blit(malle_poly, (0, 0))
        rectangle_text(mouse_pos, "Organize Harry's trunk", 20, VIOLET)
        if pressed:
            shop(3)


def main():
    """
    Fonction principale bouclant en continu
    """
    while 1:
        mouse_pressed = False
        # On liste les évenements survenus
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.key == pg.K_ESCAPE if event.type == pg.KEYDOWN else 0):
                pg.quit()
                quit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                mouse_pressed = True

        alley(pg.mouse.get_pos(), mouse_pressed)
        # On rafraîchit l'écran
        pg.display.update()
        # On limite le nombre d'images par secondes
        clock.tick(FPS)

main()
