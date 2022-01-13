import os
import pygame as pg

pg.init()

os.environ["SDL_VIDEO_CENTERED"] = "1"  # On centre la fenêtre PyGame
# On initialise la fenêtre de 1624 par 1080 pixels (la taille de la photo)
screen = pg.display.set_mode((1624, 1080))

# On définit plusieurs couleurs au format rgb
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (34, 139, 34)
VIOLET = (128, 0, 128)
YELLOW = (255, 255, 0)
TRANSPARENT_YELLOW = (255, 240, 0, 85)
ORANGE = (255, 140, 0)

# On utilise une police d"écriture spécifique
font = "HarryPotterFont.ttf"
Font = pg.font.Font(font, 20)

# On charge les différentes images
IMG_CHEMIN = pg.image.load("chemin_de_traverse.png")
IMG_MALKIN = pg.image.load("malkin_shop.jpg")
IMG_OLLIVANDER = pg.image.load("ollivander_shop.jpg")
IMG_FLOURISH_AND_BLOTTS = pg.image.load("flourish_and_blotts_shop.jpg")
IMG_MALLE = pg.transform.rotozoom(pg.image.load("Malle-Harry-Potter.png"), 0, 1.05)

# On définit la vitesse de rafraichissement à 30 FPS
clock = pg.time.Clock()
FPS = 30

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
# La surface sur laquelle on met notre polygone accepte la notion de transparence
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
OLLIVANDER_TESTS = (('0', '0', '0'), ('0', '0', '654'), ('0', '23', '78'), ('2', '11', '9'), ('7', '531', '451'))
FLOURISH_AND_BLOTTS_TESTS = ('0', '60', '63', '231', '899')
MALKIN_TESTS = ('0', '8', '62', '231', '497', '842')


def display_text(text: str, font: pg.font.Font, size: int, color: tuple, x: int, y: int, alignment=1):
    """
    Fonction permettant l'affichage d'un texte

    Entrée: text: Le texte à afficher
            font: La police d'écriture à utiliser
            size: La taille de la police
            color: La couleur de la police de type (r, g, b)
            x: L'emplacement du texte sur l'axe horizontal
            y: L'emplacement du texte sur l'axe horizontal
            alignment: Alignement du texte, 
                        0: Texte aligné à gauche,
                        1: Texte centré
                        2: Texte aligné à droite
    """
    assert alignment == 0 or alignment == 1 or alignment == 2, "Alignment not valid"

    font = pg.font.Font(font, size)
    text = font.render(text, 0, color)
    text_rect = text.get_rect()
    if alignment == 0:  # Alignement à gauche
        screen.blit(text, (x, y))
    elif alignment == 1:  # Alignement au centre
        screen.blit(text, (x - (text_rect[2]/2), y))
    else:  # Alignement à droite
        screen.blit(text, (x - text_rect[2], y))


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


def give_back(repaid: dict or list):
    """
    Fonction permettant d'afficher le rendu pour n'importe quelle boutique

    Entrée: Un dictionnaire comportant les différentes monnaie et leur nombre
    """
    if repaid == {}:
        return
    display_text("I'm giving you back :", font, 60, ORANGE, 812, 450 if type(repaid) == dict else 560)
    i = 0
    for amount in repaid:
        if amount == "impossible":
            break
        if type(repaid) == list and amount > 0:
            i += 1
            display_text(f"{amount} {('Galleon' if i == 1 else 'Sickle' if i == 2 else 'Knut') + ('s' if amount > 1 else '')}", font, 80, GREEN, 630, 590 + 85*i, alignment=0)
        elif repaid[amount] > 0:
            i += 1
            display_text((f"{repaid[amount]} {('note' if amount > 2 else 'piece') + ('s' if repaid[amount] > 1 else '')} of {amount} euros")
            if type(amount) == int else f"{repaid[amount]} {amount}", font, 50, GREEN, 600, 465 + 65*i, alignment=0)
    if type(repaid) == dict and repaid["impossible"]:
        display_text("Can't give you enough money !", font, 70, GREEN, 812, 950, alignment=1)
    elif i == 0:
        display_text("Nothing to give you back !", font, 70, GREEN, 812, 525 if type(repaid) == dict else 650, alignment=1)


def shop(shop: int):
    """
    Fonction permettant l'affichage et la gestion de n'importe quelle boutique

    Entrée: id de la boutique 0: Malkin, 1: Ollivander,
    2: Flourish and Blotts
    """
    assert shop == 0 or shop == 1 or shop == 2, "Wrong shop id: Unexistant"

    nb = ''
    repaid = {}
    money_entered = ''
    tests_needed = True
    nb_tests = 0
    money_list = (" euros", " galleons", " sickles", " knuts")
    previous_test = False
    previous_tests = [0]
    if shop == 1:
        # On est en Gallions chez Ollivander
        money_type = 1
    else:
        money_type = 0

    while 1:
        # On affiche l'image de la boutique
        if shop == 0:
            screen.blit(IMG_MALKIN, (0, 0))
            display_text("Welcome to Madam's Malkin shop !", font, 90, VIOLET, 812, 100)
        elif shop == 1:
            screen.blit(IMG_OLLIVANDER, (0, 0))
            display_text("Welcome to Ollivander's shop !", font, 90, VIOLET, 812, 100)
        else:
            screen.blit(IMG_FLOURISH_AND_BLOTTS, (0, 0))
            display_text("Welcome to Flourish and Blotts shop !", font, 90, VIOLET, 812, 100)
        # On l'assombrit
        screen.blit(dim, (0, 0))
        display_text("Enter amount :", font, 70, YELLOW, 812, 250)

        # On fait les tests pour chaque boutique
        if tests_needed:
            # Chez Malkin
            if shop == 0:
                nb = MALKIN_TESTS[nb_tests]
                if nb_tests == 4:
                    tests_needed = False
            # Chez Ollivander
            elif shop == 1:
                for i in range(3):
                    nb += OLLIVANDER_TESTS[nb_tests][i] + (';' if i != 2 else '')
                if nb_tests == 4:
                    tests_needed = False
                    money_type = 0
                else:
                    money_type = 3
            # Chez Fleury
            elif shop == 2:
                nb = FLOURISH_AND_BLOTTS_TESTS[nb_tests]
                if nb_tests == 3:
                    tests_needed = False
            nb += '\n'
            nb = user_entry(nb, numbers=False)
            if nb[-1:] == '\n' and nb[-2:] == '\n':
                nb = nb[:-1]
        elif previous_test:
            nb = previous_tests[previous_tests[0]] + '\n'
            nb = user_entry(nb, numbers=False)
            if nb[-1:] == '\n' and nb[-2:] == '\n':
                nb = nb[:-1]
        else:
            nb = user_entry(nb)

        if nb == 'QUIT':
            return
        elif nb[-4:] == 'NEXT':
            if tests_needed:
                if nb_tests != 5 and shop == 0 or nb_tests != 4 and shop == 1 or nb_tests != 4 and shop == 2:
                    nb_tests += 1
                else:
                    tests_needed = False
                    nb = ''
            if previous_tests[0] < len(previous_tests) -1:
                previous_tests[0] += 1
                nb = ''
            elif not(tests_needed):
                previous_test = False
                nb = nb[:-4]
                if nb[-1:] == '\n':
                    nb = nb[:-1]
            else:
                nb = nb[:-4]
                if nb[-1:] == '\n':
                    nb = nb[:-1]
        elif nb[-8:] == 'PREVIOUS':
            if tests_needed and nb_tests != 0:
                nb_tests -= 1
            if previous_tests[0] > 1:
                previous_tests[0] -= 1
                nb = ''
            elif not(tests_needed):
                previous_test = True
                nb = nb[:-8]
                if nb[-1:] == '\n':
                    nb = nb[:-1]
            else:
                nb = nb[:-8]
                if nb[-1:] == '\n':
                    nb = nb[:-1]
        # L'utilisateur à appuyé sur entrée
        elif nb[-1:] == '\n':
            if shop == 0:
                money_entered = int(nb[:-1])
                repaid = malkin(money_entered)
                if previous_tests[previous_tests[0]] != str(money_entered):
                    previous_tests.append(str(money_entered))
                    previous_tests[0] += 1
            elif shop == 1:
                if money_type == 1:  # Gallions
                    money_type = 2
                    money_entered = nb[:-1] + ';'
                    previous_tests.append(money_entered)
                    previous_tests[0] += 1
                elif money_type == 2:  # Mornilles
                    money_type = 3
                    money_entered += nb[:-1] + ';'
                elif money_type == 3:  # Noises
                    money_entered += nb[:-1]
                    nbs_entered = money_entered.split(';')
                    repaid = ollivander(nbs_entered)
                    if previous_tests[previous_tests[0]] != money_entered:
                        if previous_tests[previous_tests[0]] != nbs_entered:
                            previous_tests.append(nbs_entered)
                            previous_tests[0] += 1
            else:
                money_entered = int(nb[:-1])
                repaid = flourish_and_blotts(money_entered)
                if previous_tests[previous_tests[0]] != str(money_entered):
                    previous_tests.append(str(money_entered))
                    previous_tests[0] += 1
            nb = ''
        # Affichage du nombre entré
        if shop == 1:
            nbs_entered = money_entered.split(';')
            for i in range(money_type):
                if i == money_type - 1:
                    display_text(nb + (str(nbs_entered[i]) if nb == '' else '') + money_list[i + 1], font, 75, YELLOW, 812, 260 + 75*(i +1))
                else:
                    display_text(str(nbs_entered[i]) + money_list[i + 1], font, 60, YELLOW, 812, 260 + 75*(i +1))
        else:
            display_text(nb + (str(money_entered) if nb == '' else '') + money_list[money_type], font, 80, YELLOW, 812, 350)
        give_back(repaid)
        print(previous_tests, nb_tests)

        pg.display.update()
        clock.tick(FPS)


def description(mouse_pos, shop):
    """
    Fonction affichant un rectangle noir indiquant le magasin
    sur lequel la souris est placée
    
    Entrée: La position de la souris
            Le magasin pointé
    """
    shop_text = Font.render(shop, 0, VIOLET)
    shop_text_rect = shop_text.get_rect()

    # On affiche le rectangle à doite puisqu'il y a de la place
    if shop_text_rect[2] + mouse_pos[0] + 26 <= 1624:
        pg.draw.rect(screen, BLACK, (mouse_pos[0] + 12, mouse_pos[1] + 2, shop_text_rect[2] + 11, 36))
        pg.draw.rect(screen, WHITE, (mouse_pos[0] + 10, mouse_pos[1], shop_text_rect[2] + 15, 40), width=3)
        screen.blit(shop_text, (mouse_pos[0] + 15, mouse_pos[1] + 10))
    # Il n'y a pas de place à droite, on le met donc à gauche
    else:
        pg.draw.rect(screen, BLACK, (mouse_pos[0] - shop_text_rect[2] - 22, mouse_pos[1] + 2, shop_text_rect[2] + 16, 36))
        pg.draw.rect(screen, WHITE, (mouse_pos[0] - shop_text_rect[2] - 25, mouse_pos[1], shop_text_rect[2] + 20, 40), width=3)
        screen.blit(shop_text, (mouse_pos[0] - shop_text_rect[2] - 15, mouse_pos[1] + 10))


def alley(mouse_pos):
    """
    Fonction affichant le menu de sélection de la boutique,
    elle est surlignée quand la souris passe dessus et si l'on
    clique on est transporté dedans

    Entrée: La position de la souris
    """
    # On affiche l'image du chemin de traverse
    screen.blit(IMG_CHEMIN, (0, 0))
    screen.blit(IMG_MALLE, (600, 750))
    # On surligne le magasin si on a la souris dessus
    if OLLIVANDER_RECT.collidepoint(mouse_pos[0], mouse_pos[1]):
        screen.blit(ollivander_poly, (0, 0))
        description(mouse_pos, "Ollivander")
        # Un bouton de la souris a été pressé
        if pg.event.peek(pg.MOUSEBUTTONDOWN):
            shop(1)
    elif FLOURISH_AND_BLOTTS_RECT.collidepoint(mouse_pos[0], mouse_pos[1]):
        screen.blit(flourish_and_blotts_poly, (0, 0))
        description(mouse_pos, "Flourish and Blotts")
        if pg.event.peek(pg.MOUSEBUTTONDOWN):
            shop(2)
    elif MALKIN_RECT.collidepoint(mouse_pos[0], mouse_pos[1]):
        screen.blit(malkin_poly, (0, 0))
        description(mouse_pos, "Madam Malkin's Robes for All Occasions")
        if pg.event.peek(pg.MOUSEBUTTONDOWN):
            shop(0)
    elif MALLE_RECT.collidepoint(mouse_pos[0], mouse_pos[1]):
        screen.blit(malle_poly, (0, 0))
        description(mouse_pos, "Organize Harry's trunk")
        if pg.event.peek(pg.MOUSEBUTTONDOWN):
            shop(3)


def main():
    """
    Fonction principale ne se terminant que si l'utilisateur
    quitte la fenêtre ou appuie sur esc
    """
    while 1:
        # On liste les évenements survenus
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.key == pg.K_ESCAPE if event.type == pg.KEYDOWN else 0):
                pg.quit()
                quit()

        # On affiche l'allée (menu principal)
        alley(pg.mouse.get_pos())
        # On rafraîchit l'écran et on limite le nombre
        # de FPS à 30
        pg.display.update()
        clock.tick(FPS)

main()
