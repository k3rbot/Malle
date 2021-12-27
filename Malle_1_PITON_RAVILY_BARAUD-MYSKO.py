import os
import pygame as pg

pg.init()

os.environ["SDL_VIDEO_CENTERED"] = "1"  # On centre la fenêtre PyGame
# On initialise la fenêtre de 1624 par 1080 pixels (la taille de la photo)
screen = pg.display.set_mode((1624, 1080))

# On définit plusieurs couleurs au format rgb
white = (255, 255, 255)
black = (0, 0, 0)
green = (34, 139, 34)
violet = (128, 0, 128)
yellow = (255, 255, 0)
transparent_yellow = (255, 240, 0, 85)
orange = (255, 140, 0)

# On utilise une police d"écriture spécifique
font = "HarryPotterFont.ttf"
Font = pg.font.Font(font, 20)

# On charge les différentes images
img_chemin = pg.image.load("chemin_de_traverse.png")
img_malkin = pg.image.load("malkin_shop.jpg")
img_ollivander = pg.image.load("ollivander_shop.jpg")
img_flourish_and_blotts = pg.image.load("flourish_and_blotts_shop.jpg")

# On définit la vitesse de rafraichissement à 30 FPS
clock = pg.time.Clock()
FPS = 30

# On définit le titre de la fenêtre
pg.display.set_caption("Harry Potter se fait la malle au chemin de traverse")

# Polygone d'une boutique
ollivander_cords = (
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
ollivander_rect = pg.draw.polygon(ollivander_poly, transparent_yellow, ollivander_cords)

flourish_and_blotts_cords = (
    (1243, 451), (1426, 381), (1456, 338), (1486, 308),
    (1523, 279), (1558, 256), (1621, 239), (1622, 859),
    (1578, 847), (1578, 837), (1522, 833), (1283, 790),
    (1281, 740), (1275, 732), (1283, 724), (1271, 524),
    (1270, 509), (1271, 504), (1270, 480), (1262, 473),
    (1255, 472), (1252, 467), (1249, 467), (1244, 458),
    (1241, 447)
)
flourish_and_blotts_poly = pg.Surface((1634, 1080), flags=pg.SRCALPHA)
flourish_and_blotts_rect = pg.draw.polygon(flourish_and_blotts_poly, transparent_yellow, flourish_and_blotts_cords)

malkin_cords = (
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
malkin_rect = pg.draw.polygon(malkin_poly, transparent_yellow, malkin_cords)

# On prépare une surface sur laquelle on met un rectangle noir 
# semi-transparent pour réduire la luminosité de l'image derrière
dim = pg.Surface((1634, 1080), flags=pg.SRCALPHA)
pg.draw.rect(dim, (0, 0, 0, 150), (0, 0, 1664, 1080))

# Tous les tests à faire pour chaque maisons
ollivander_tests_list = ((0, 0, 0), (0, 0, 654), (0, 23, 78), (2, 11, 9), (7, 531, 451))
flourish_and_blotts_tests_list = (0, 60, 63, 231, 899)
malkin_tests_list = (0, 8, 62, 231, 497, 842)


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

    monnaie_rendue = [0, 0, 0]
    monnaie_rendue[1] = monnaie[2] // 29 + monnaie[1]
    monnaie_rendue[2] = monnaie[2] % 29
    monnaie_rendue[0] = monnaie_rendue[1] // 17 + monnaie[0]
    monnaie_rendue[1] %= 17

    return monnaie_rendue


def user_entry(nb='') -> str:
    """
    Fonction permettant de récupérer les entrées de l'utilisateur

    Entrée: variable sur lequelle sera concaténée ou écrasée la
    valeur de l'entrée utilisateur
    Sortie: entrées de l'utilisateur
    """
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()
        elif event.type == pg.KEYDOWN:
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
            elif (event.key == pg.K_RETURN or event.key == pg.K_KP_ENTER) and nb != '':
                nb += '\n'
            elif event.key == pg.K_ESCAPE:
                nb = 'QUIT'
            elif event.key == pg.K_RIGHT:
                nb += 'SKIP'
    return nb


def give_back(repaid: dict or list):
    """
    Fonction permettant d'afficher le rendu pour n'importe quelle boutique

    Entrée: Un dictionnaire comportant les différentes monnaie et leur nombre
    """
    if repaid == {}:
        return
    display_text("I'm giving you back :", font, 60, orange, 812, 450 if type(repaid) == dict else 560)
    i = 0
    for amount in repaid:
        if amount == "impossible":
            break
        if type(repaid) == list and amount > 0:
            i += 1
            display_text(f"{amount} {('Galleon' if i == 1 else 'Sickle' if i == 2 else 'Knut') + ('s' if amount > 1 else '')}", font, 80, green, 630, 590 + 85*i, alignment=0)
        elif repaid[amount] > 0:
            i += 1
            display_text((f"{repaid[amount]} {('note' if amount > 2 else 'piece') + ('s' if repaid[amount] > 1 else '')} of {amount} euros")
            if type(amount) == int else f"{repaid[amount]} {amount}", font, 50, green, 600, 465 + 65*i, alignment=0)
    if type(repaid) == dict and repaid["impossible"]:
        display_text("Can't give you enough money !", font, 70, green, 812, 950, alignment=1)
    elif i == 0:
        display_text("Nothing to give you back !", font, 70, green, 812, 525 if type(repaid) == dict else 650, alignment=1)


def shop(shop: int):
    """
    Fonction permettant l'affichage et la gestion de n'importe quelle boutique

    Entrée: id de la boutique 0: Malkin, 1: Ollivander,
    2: Flourish and Blotts
    """
    assert shop == 0 or shop == 1 or shop == 2, "Wrong shop id: Unexistant"

    # On prépare les variables communes à toutes les boutiques
    nb = ''  # Entrées de l'utilisateur
    repaid = {}  # Rendu de la boutique
    nbs_entered = [0, 0, 0]  # Nombres entrés chez Ollivander
    money_entered = 0  # Nombre entré par l'utilisateur
    tests_needed = True  # Doit on faire les tests de la boutique
    nb_tests = 0  # Nombre d'itérations pour l'affichage des tests
    step_ollivander_test = 0  # Etape de l'entrée de valeur chez Ollivander
    money_list = (" euros", " galleons", " sickles", " knuts")
    if shop == 1:
        # On est en Gallions chez Ollivander
        money_type = 1
    else:
        money_type = 0

    while 1:
        # On affiche l'image de la boutique
        if shop == 0:
            screen.blit(img_malkin, (0, 0))
            display_text("Welcome to Madam's Malkin shop !", font, 90, violet, 812, 100)
        elif shop == 1:
            screen.blit(img_ollivander, (0, 0))
            display_text("Welcome to Ollivander's shop !", font, 90, violet, 812, 100)
        else:
            screen.blit(img_flourish_and_blotts, (0, 0))
            display_text("Welcome to Flourish and Blotts shop !", font, 90, violet, 812, 100)
        # On l'assombrit
        screen.blit(dim, (0, 0))
        display_text("Enter amount :", font, 70, yellow, 812, 250)

        # On fait les tests pour chaque boutique
        if tests_needed:
            # Chez Malkin
            if shop == 0:
                # On récupère la valeur du test
                nb = str(malkin_tests_list[nb_tests])
                if nb_tests == 4:
                    tests_needed = False
            # Chez Ollivander
            elif shop == 1:
                if step_ollivander_test != 3 and not(nb_tests == 0 and step_ollivander_test == 0):
                    nb = str(ollivander_tests_list[(nb_tests - 1)//4][step_ollivander_test])
                if step_ollivander_test >= 3:
                    step_ollivander_test = 0
                    nbs_entered = [0, 0, 0]
                    money_type = 1
                elif not(nb_tests == 0 and step_ollivander_test == 0):
                    step_ollivander_test += 1
                if nb_tests == 19:
                    tests_needed = False
            # Chez Fleury
            elif shop == 2:
                nb = str(flourish_and_blotts_tests_list[nb_tests])
                if nb_tests == 3:
                    tests_needed = False
            # On est prêts à afficher le nombre pour le test
            if shop != 1 or ((step_ollivander_test != 0 and step_ollivander_test != 4) and nb_tests != 0):
                nb += '\n'
            nb_tests += 1

            # On récupère les entrées de l'utilisateur
            entry = user_entry()
            # Il a appuyé sur esc
            if entry == 'QUIT':
                return
            # Il a appuyé sur la flèche de droite
            elif entry == 'SKIP':
                # On passe toute la phase d'affichage des tests
                tests_needed = False
                step_ollivander_test = 0
                nb_tests = 0
                nbs_entered = [0, 0, 0]
                if shop == 1:
                    money_type = 1
                else:
                    money_type = 0

        # L'utilisateur choisit le montant à rendre
        else:
            nb = user_entry(nb)

        if nb == 'QUIT':
            return
        elif nb[-4:] == 'SKIP':
            # On enlève le caractère puisqu'on ne fait plus les tests
            nb = nb[:-4]
        # L'utilisateur à appuyé sur entrée
        elif nb[-1:] == '\n':
            if shop == 0:
                # On récupère le rendu chez Malkin
                money_entered = int(nb[:-1])
                repaid = malkin(money_entered)
            elif shop == 1:
                # On récupère le rendu petit à petit en fonction
                # de la pièce de monnaie chez Ollivander
                if money_type == 1:
                    # Gallions
                    money_type = 2
                    nbs_entered[0] = int(nb[:-1])
                elif money_type == 2:
                    # Mornilles
                    money_type = 3
                    nbs_entered[1] = int(nb[:-1])
                elif money_type == 3:
                    # Noises
                    nbs_entered[2] = int(nb[:-1])
                    repaid = ollivander(nbs_entered)
                    # On ne fait pas les test du coup on efface
                    # le résulat dès qu'on appuie sur entrée
                    if not(tests_needed):
                        money_type = 1
                        nbs_entered = [0, 0, 0]
                money_entered = int(nb[:-1])
            else:
                # On récupère le rendu chez Fleury
                money_entered = int(nb[:-1])
                repaid = flourish_and_blotts(money_entered)
            # On réinitialise les entrées de l'utilisateur
            nb = ''
        # Affichage du nombre entré
        if shop == 1:
            # Chez Ollivander
            for i in range(money_type):
                if i == money_type - 1:
                    display_text(nb + (str(nbs_entered[i]) if nb == '' else '') + money_list[i + 1], font, 75, yellow, 812, 260 + 75*(i +1))
                else:
                    display_text(str(nbs_entered[i]) + money_list[i + 1], font, 60, yellow, 812, 260 + 75*(i +1))
        else:
            # Chez les autres
            display_text(nb + (str(money_entered) if nb == '' and tests_needed else '') + money_list[money_type], font, 80, yellow, 812, 350)
        # On affiche le rendu de la boutique avec le montant "repaid"
        give_back(repaid)
        # On rafraîchit l'écran
        pg.display.update()

        # On attends plus ou moins longtemps pour mieux
        # voir les tests s'effectuer automatiquement
        # en plus de vérifier si l'on ne quitte/skippe pas
        if tests_needed or nb_tests == 20:
            for _ in range(35 if shop != 1 or step_ollivander_test == 3 else 10):
                entry = user_entry()
                if entry == 'QUIT':
                    return
                elif entry == 'SKIP':
                    # On passe les exemples
                    tests_needed = False
                    step_ollivander_test = 0
                    nb_tests = 0
                    nbs_entered = [0, 0, 0]
                    if shop == 1:
                        money_type = 1
                    else:
                        money_type = 0
                # On attends 100 millisecondes
                pg.time.wait(100)

            # On réinitialise les variables à la fin de tous les tests
            if nb_tests == 20:
                step_ollivander_test = 0
                nb_tests = 0
                nbs_entered = [0, 0, 0]
                money_type = 1
        clock.tick(FPS)


def description(mouse_pos, shop):
    """
    Fonction affichant un rectangle noir indiquant le magasin
    sur lequel la souris est placée
    
    Entrée: La position de la souris
            Le magasin pointé
    """
    shop_text = Font.render(shop, 0, violet)
    shop_text_rect = shop_text.get_rect()

    # On affiche le rectangle à doite puisqu'il y a de la place
    if shop_text_rect[2] + mouse_pos[0] + 26 <= 1624:
        # On affiche un rectangle blanc puis noir puis on ymet le nom de la boutique
        pg.draw.rect(screen, black, (mouse_pos[0] + 12, mouse_pos[1] + 2, shop_text_rect[2] + 11, 36))
        pg.draw.rect(screen, white, (mouse_pos[0] + 10, mouse_pos[1], shop_text_rect[2] + 15, 40), width=3)
        screen.blit(shop_text, (mouse_pos[0] + 15, mouse_pos[1] + 10))
    # Il n'y a pas de place à droite, donc on le met à gauche
    else:
        pg.draw.rect(screen, black, (mouse_pos[0] - shop_text_rect[2] - 22, mouse_pos[1] + 2, shop_text_rect[2] + 16, 36))
        pg.draw.rect(screen, white, (mouse_pos[0] - shop_text_rect[2] - 25, mouse_pos[1], shop_text_rect[2] + 20, 40), width=3)
        screen.blit(shop_text, (mouse_pos[0] - shop_text_rect[2] - 15, mouse_pos[1] + 10))


def alley(mouse_pos):
    """
    Fonction affichant le menu de sélection de la boutique,
    elle est ssurlignée quand la souris passe dessus et si l'on
    clique on est transporté dedans

    Entrée: La position de la souris
    """
    # On affiche l'image du chemin de traverse
    screen.blit(img_chemin, (0, 0))
    # On surligne le magasin si on a la souris dessus
    if ollivander_rect.collidepoint(mouse_pos[0], mouse_pos[1]):
        screen.blit(ollivander_poly, (0, 0))
        description(mouse_pos, "Ollivander")
        # Un bouton de la souris a été pressé
        if pg.event.peek(pg.MOUSEBUTTONDOWN):
            shop(1)
    elif flourish_and_blotts_rect.collidepoint(mouse_pos[0], mouse_pos[1]):
        screen.blit(flourish_and_blotts_poly, (0, 0))
        description(mouse_pos, "Flourish and Blotts")
        if pg.event.peek(pg.MOUSEBUTTONDOWN):
            shop(2)
    elif malkin_rect.collidepoint(mouse_pos[0], mouse_pos[1]):
        screen.blit(malkin_poly, (0, 0))
        description(mouse_pos, "Madam Malkin's Robes for All Occasions")
        if pg.event.peek(pg.MOUSEBUTTONDOWN):
            shop(0)


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
