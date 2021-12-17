import os
import pygame as pg

pg.init()

os.environ["SDL_VIDEO_CENTERED"] = "1"  # On centre la fenêtre PyGame
# On initialise la fenêtre de 1624 par 1080 pixels (la taille de la photo)
screen = pg.display.set_mode((1624, 1080))

# On définit plusieurs couleurs au format rgb
white = (255, 255, 255)
black = (0, 0, 0)
gray = (50, 50, 50)
red = (255, 0, 0)
green = (34, 139, 34)
violet = (128, 0, 128)
blue = (0, 0, 255)
yellow = (255, 255, 0)
transparent_yellow = (255, 240, 0, 85)
golden = (212, 175, 55)
silver = (192, 192, 192)
bronze = (205, 127, 50)
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
pg.display.set_caption("HARRY POTTER SE FAIT LA MALLE")

# Polygones des boutiques
ollivander_cords = (
    (781, 704), (784, 711), (815, 709), (818, 716),
    (871, 718), (871, 485), (848, 483), (830, 484),
    (816, 488), (808, 495), (813, 501), (816, 507),
    (814, 513), (807, 514), (802, 509), (796, 504),
    (787, 508), (772, 512), (778, 530), (780, 582),
    (778, 584), (778, 596), (783, 602), (783, 669),
    (784, 677), (780, 707)
)
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

dim = pg.Surface((1634, 1080), flags=pg.SRCALPHA)
pg.draw.rect(dim, (0, 0, 0, 150), (0, 0, 1664, 1080))

ollivander_tests_list = ((0, 0, 0), (0, 0, 654), (0, 23, 78), (2, 11, 9), (7, 531, 451))
flourish_and_blotts_tests_list = (0, 60, 63, 231, 899)
malkin_tests_list = (0, 8, 62, 231, 497, 842)


def display_text(text, font, size, color, x, y, alignment=1):
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
    billets/pièces à rendre pour un montant donné

    Entrée: Montant à rendre
    Sortie: Dictionnaire comprenant la valeur de
            le pièce/du billet et le nombre à rendre
    """
    assert type(monnaie) == int, "Vous devez rentrer un nombre conforme"

    monnaie_dispo = (500, 200, 100, 50, 20, 10, 5, 2, 1)
    monnaie_rendue = {500: 0, 200: 0, 100: 0, 50: 0,
                    20: 0, 10: 0, 5: 0, 2: 0, 1: 0}
    for billet in monnaie_dispo:
        monnaie_rendue[billet] = monnaie // billet
        monnaie %= billet

    return monnaie_rendue


def malkin(rendu:int) -> dict:
   assert type(rendu) == int
   if rendu > 590:
       return

   monnaie_dispo = {200: 1, 100: 3, 50: 1, 20: 1, 10: 1, 2: 5}
   rendu_caisse = {200: 0, 100: 0, 50: 0, 20: 0, 10: 0, 2: 0}

   for billet in monnaie_dispo:
        while rendu >= billet and monnaie_dispo[billet] > 0:
            monnaie_dispo[billet] -= 1
            rendu -= billet
            rendu_caisse[billet] += 1

   return rendu_caisse


print(malkin(0))
print(malkin(8))
print(malkin(62))
print(malkin(231))
print(malkin(497))
print(malkin(842))


def ollivander(monnaie:list):
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


def user_entry(nb=''):
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
    return nb


def give_back(repaid):
    if repaid == {}:
        return
    display_text("I'm giving you back :", font, 60, orange, 812, 450 if type(repaid) == dict else 560)
    i = 0
    for amount in repaid:
        if type(repaid) == list and amount > 0:
            i += 1
            display_text(f"{amount} {('Galleon' if i == 1 else 'Sickle' if i == 2 else 'Knut') + ('s' if amount > 1 else '')}", font, 80, green, 630, 590 + 85*i, alignment=0)
        elif repaid[amount] > 0:
            i += 1
            display_text((f"{repaid[amount]} {('note' if amount > 2 else 'piece') + ('s' if repaid[amount] > 1 else '')} of {amount} euros")
            if type(amount) == int else f"{repaid[amount]} {amount}", font, 50, green, 600, 465 + 65*i, alignment=0)
    if i == 0:
        display_text("Nothing to give you back !", font, 70, green, 812, 525 if type(repaid) == dict else 650, alignment=1)


def shop(shop):
    assert shop == 0 or shop == 1 or shop == 2, "Wrong shop id: Unexistant"
    nb = ''
    repaid = {}
    nbs_entered = [0, 0, 0]
    money_entered = 0
    tests_needed = True
    nb_tests = 0
    step_ollivander_test = 0
    money_list = (" euros", " galleons", " sickles", " knuts")
    if shop == 1:
        money_type = 1
    else:
        money_type = 0

    while 1:
        # On affiche l'image de la boutique puis on l'assombrit
        if shop == 0:
            screen.blit(img_malkin, (0, 0))
            display_text("Welcome to Madam's Malkin shop !", font, 90, violet, 812, 100)
        elif shop == 1:
            screen.blit(img_ollivander, (0, 0))
            display_text("Welcome to Ollivander's shop !", font, 90, violet, 812, 100)
        else:
            screen.blit(img_flourish_and_blotts, (0, 0))
            display_text("Welcome to Flourish and Blotts shop !", font, 90, violet, 812, 100)
        screen.blit(dim, (0, 0))
        display_text("Enter amount :", font, 70, yellow, 812, 250)

        if tests_needed:
            if shop == 0:
                nb = str(malkin_tests_list[nb_tests])
                if nb_tests == 4:
                    tests_needed = False
            elif shop == 1:
                if step_ollivander_test != 3 and not(nb_tests == 0 and step_ollivander_test == 0):
                    nb = str(ollivander_tests_list[(nb_tests - 1)//4][step_ollivander_test])
                if step_ollivander_test >= 3:
                    step_ollivander_test = 0
                    nbs_entered = [0, 0, 0]
                    money_type = 1
                elif not(nb_tests == 0  and step_ollivander_test == 0):
                    step_ollivander_test += 1
                if nb_tests == 19:
                    tests_needed = False
            elif shop == 2:
                nb = str(flourish_and_blotts_tests_list[nb_tests])
                if nb_tests == 3:
                    tests_needed = False
            if shop != 1 or ((step_ollivander_test != 0 and step_ollivander_test != 4) and nb_tests != 0):
                nb += '\n'
            nb_tests += 1
            if user_entry() == 'QUIT':
                return
        else:
            nb = user_entry(nb)
        if nb == 'QUIT':
            return
        elif nb[-1:] == '\n':
            if shop == 0:
                money_entered = int(nb[:-1])
                repaid = malkin(money_entered)
            elif shop == 1:
                if money_type == 1:
                    money_type = 2
                    nbs_entered[0] = int(nb[:-1])
                elif money_type == 2:
                    money_type = 3
                    nbs_entered[1] = int(nb[:-1])
                elif money_type == 3:
                    nbs_entered[2] = int(nb[:-1])
                    repaid = ollivander(nbs_entered)
                    if not(tests_needed):
                        money_type = 1
                money_entered = int(nb[:-1])
            else:
                money_entered = int(nb[:-1])
                repaid = flourish_and_blotts(money_entered)
            print(nb[:-1], "----", nbs_entered, nb_tests, step_ollivander_test)
            nb = ''
        if shop == 1:
            for i in range(money_type):
                if i == money_type - 1:
                    display_text(nb + (str(nbs_entered[i]) if nb == '' else '') + money_list[i + 1], font, 75, yellow, 812, 260 + 75*(i +1))
                else:
                    display_text(str(nbs_entered[i]) + money_list[i + 1], font, 60, yellow, 812, 260 + 75*(i +1))
        else:
            display_text(nb + (str(money_entered) if nb == '' and tests_needed else '') + money_list[money_type], font, 80, yellow, 812, 350)
        give_back(repaid)
        screen.blit(update_fps(), (10,0)) ################
        pg.display.update()
        if tests_needed or nb_tests == 20:
            for _ in range(35 if shop != 1 or step_ollivander_test == 3 else 10):
                if user_entry() == 'QUIT':
                    return
                pg.time.wait(100)
        clock.tick(FPS)


def description(mouse_pos, shop):
    shop_text = Font.render(shop, 0, violet)
    shop_text_rect = shop_text.get_rect()
    if shop_text_rect[2] + mouse_pos[0] + 26 <= 1624:
        pg.draw.rect(screen, black, (mouse_pos[0] + 12, mouse_pos[1] + 2, shop_text_rect[2] + 11, 36))
        pg.draw.rect(screen, white, (mouse_pos[0] + 10, mouse_pos[1], shop_text_rect[2] + 15, 40), width=3)
        screen.blit(shop_text, (mouse_pos[0] + 15, mouse_pos[1] + 10))
    else :
        pg.draw.rect(screen, black, (mouse_pos[0] - shop_text_rect[2] - 22, mouse_pos[1] + 2, shop_text_rect[2] + 16, 36))
        pg.draw.rect(screen, white, (mouse_pos[0] - shop_text_rect[2] - 25, mouse_pos[1], shop_text_rect[2] + 20, 40), width=3)
        screen.blit(shop_text, (mouse_pos[0] - shop_text_rect[2] - 15, mouse_pos[1] + 10))


def alley(mouse_pos):
    # On affiche l'image du chemin de traverse
    screen.blit(img_chemin, (0, 0))
    # On surligne le magasin si on a la souris dessus
    if ollivander_rect.collidepoint(mouse_pos[0], mouse_pos[1]):
        screen.blit(ollivander_poly, (0, 0))
        description(mouse_pos, "Ollivander")
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


# Affichage du nombre de FPS -- TEMPORAIRE ###########
def update_fps():
    Font = pg.font.SysFont("Arial", 18)
    fps = str(int(clock.get_fps()))
    fps_text = Font.render(fps, 1, pg.Color("coral"))
    return fps_text


def main():
    while 1:
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.key == pg.K_ESCAPE if event.type == pg.KEYDOWN else 0):
                pg.quit()
                quit()

        alley(pg.mouse.get_pos())

        screen.blit(update_fps(), (10, 0))
        pg.display.update()
        clock.tick(FPS)

main()
