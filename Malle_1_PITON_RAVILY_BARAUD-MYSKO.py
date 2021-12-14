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
    monnaie_rendue = {500 : 0, 200 : 0, 100 : 0, 50 : 0,
                    20 : 0, 10 : 0, 5 : 0, 2 : 0, 1 : 0}
    for billet in monnaie_dispo:
        while monnaie >= billet:
            monnaie -= billet
            monnaie_rendue[billet] += 1

    return monnaie_rendue

print(flourish_and_blotts(0))
print(flourish_and_blotts(60))
print(flourish_and_blotts(63))
print(flourish_and_blotts(231))
print(flourish_and_blotts(899))


def malkin(rendu:int) -> dict:
    assert type(rendu) == int

    caisse_dispo = {200 : 1, 100 : 3, 50 : 1 , 20 : 1, 10: 1, 2 :5}
    rendu_caisse ={200 : 0, 100 : 0, 50 : 0, 20 : 0, 10: 0, 2 : 0}
    
    for thune in caisse_dispo:
        while rendu >= thune :
            while caisse_dispo[200] <= 1 :
                caisse_dispo[200] = caisse_dispo[200] + 1
            while caisse_dispo[100] <= 3 :
                caisse_dispo[100] = caisse_dispo[100] + 1  
            while caisse_dispo[50] <= 1 :
                caisse_dispo[50] = caisse_dispo[50] + 1
            while caisse_dispo[20] <= 1 :
                caisse_dispo[20] = caisse_dispo[20] +1
            while caisse_dispo[10] <= 1 :
                caisse_dispo[10] = caisse_dispo[10] +1
            while caisse_dispo[2] <= 1 :
                caisse_dispo[2] = caisse_dispo[2] + 1 
       
        else :
            print('La valeur de rendu souhaitée est au-dela des capacités de la caisse,désolé')
        return rendu_caisse
"""
print(malkin(0))
print(malkin(8))
print(malkin(62))
print(malkin(231))
print(malkin(497))
print(malkin(842))
"""

def ollivander(monnaie):
    print("Ollivander ", monnaie)

def user_entry(nb):
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

def give_back(money):
    if money == '':
        return
    display_text("I'm giving you back :", font, 60, orange, 812, 430)
    n = 0
    for amount in money:
        if money[amount] > 0:
            n += 1
            display_text((f"{money[amount]} {('note' if amount > 2 else 'piece') + ('s' if money[amount] > 1 else '')} of {amount} euros")
            if type(amount) == int else f"{money[amount]} {amount}", font, 50, green, 600, 465 + 65*n, alignment=0)

def shop(shop):
    assert shop == 0 or shop == 1 or shop == 2, "Wrong shop id: Unexistant"
    nb = ''
    money = ''
    hp_money = [0, 0, 0]
    money_entered = 0
    
    if shop == 1:
        money_type = " galleons"
    else:
        money_type = " euros"
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

        nb = user_entry(nb)
        if nb == 'QUIT':
            break
        elif nb[-1:] == '\n':
            if shop == 0:
                money_entered = int(nb[:-1])
                money = malkin(money_entered)
            elif shop == 1:
                if money_type == " galleons":
                    money_type = " sickles"
                    hp_money[0] = (int(nb[:-1]))
                elif money_type == " sickles":
                    money_type = " knuts"
                    hp_money[1] = (int(nb[:-1]))
                else:
                    money_type = " galleons"
                    hp_money[2] = (int(nb[:-1]))
                    money = ollivander(hp_money)
            else:
                money_entered = int(nb[:-1])
                money = flourish_and_blotts(money_entered)
            nb = ''

        display_text(nb + (str(money_entered) if nb == '' and money_entered != 0 else '') + money_type, font, 80, yellow, 812, 350)
        give_back(money)
        screen.blit(update_fps(), (10,0)) ################
        pg.display.update()
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

        screen.blit(update_fps(), (10,0))
        pg.display.update()
        clock.tick(FPS)

main()