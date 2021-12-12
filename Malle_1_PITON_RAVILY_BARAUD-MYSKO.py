import os
from typing import NoReturn
import pygame as pg
from pygame.constants import K_0, K_1, K_2, K_3, K_4, K_5, K_6, K_7, K_8, K_9, K_BACKSPACE, K_ESCAPE, K_KP0, K_KP1, K_KP2, K_KP3, K_KP4, K_KP5, K_KP6, K_KP7, K_KP8, K_KP9, K_KP_ENTER, K_RETURN, KEYDOWN, QUIT

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
# On charge l'image du chemin de traverse
img_chemin = pg.image.load("chemin_de_traverse.png")

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
        while rendu >= thune:
            rendu -= thune
            rendu_caisse[thune] += 1
    
    return rendu_caisse


print(malkin(0))
print(malkin(8))
print(malkin(62))
print(malkin(231))
print(malkin(497))
print(malkin(842))

def user_entry(nb):
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            quit()
        elif event.type == KEYDOWN:
            if event.key == K_KP0:
                nb += '0'
            elif event.key == K_KP1:
                nb += '1'
            elif event.key == K_KP2:
                nb += '2'
            elif event.key == K_KP3:
                nb += '3'
            elif event.key == K_KP4:
                nb += '4'
            elif event.key == K_KP5:
                nb += '5'
            elif event.key == K_KP6:
                nb += '6'
            elif event.key == K_KP7:
                nb += '7'
            elif event.key == K_KP8:
                nb += '8'
            elif event.key == K_KP9:
                nb += '9'
            elif event.key == K_BACKSPACE:
                nb = nb[:-1]
            elif (event.key == K_RETURN or event.key == K_KP_ENTER) and nb != '':
                nb += '\n'
            elif event.key == K_ESCAPE:
                nb = 'QUIT'
    return nb

def ollivander_shop():
    Font = pg.font.Font(font, 80)
    shop_img = pg.image.load("ollivander_shop.jpg")
    nb = ''
    while 1:
        screen.blit(shop_img, (0, 0))
        nb = user_entry(nb)
        if nb == 'QUIT':
            break
        elif nb[-1:] == '\n':
            print(flourish_and_blotts(int(nb[:-1])))
            nb = ''
        nb_text = Font.render(nb, 0, yellow)
        nb_text_rect = nb_text.get_rect()
        screen.blit(nb_text, (817 - (nb_text_rect[2]/2), 400))
        screen.blit(update_fps(), (10,0)) ################
        pg.display.update()
        clock.tick(FPS)

def flourish_and_blotts_shop():
    shop_img = pg.image.load("flourish_and_blotts_shop.jpg")

def malkin_shop():
    shop_img = pg.image.load("malkin_shop.jpg")

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
            ollivander_shop()
    elif flourish_and_blotts_rect.collidepoint(mouse_pos[0], mouse_pos[1]):
        screen.blit(flourish_and_blotts_poly, (0, 0))
        description(mouse_pos, "Flourish and Blotts")
        if pg.event.peek(pg.MOUSEBUTTONDOWN):
            flourish_and_blotts_shop()
    elif malkin_rect.collidepoint(mouse_pos[0], mouse_pos[1]):
        screen.blit(malkin_poly, (0, 0))
        description(mouse_pos, "Madam Malkin's Robes for All Occasions")
        if pg.event.peek(pg.MOUSEBUTTONDOWN):
            malkin_shop()

# Affichage du nombre de FPS -- TEMPORAIRE ###########
def update_fps():
    Font = pg.font.SysFont("Arial", 18)
    fps = str(int(clock.get_fps()))
    fps_text = Font.render(fps, 1, pg.Color("coral"))
    return fps_text

def main():
    while 1:
        for event in pg.event.get():
            if event.type == QUIT or (event.key == K_ESCAPE if event.type == KEYDOWN else 0):
                pg.quit()
                quit()

        alley(pg.mouse.get_pos())

        screen.blit(update_fps(), (10,0))
        pg.display.update()
        clock.tick(FPS)

main()