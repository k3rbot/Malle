import os
import pygame as pg
from pygame import mouse

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

fleury_and_bott_cords = (
    (1243, 451), (1426, 381), (1456, 338), (1486, 308),
    (1523, 279), (1558, 256), (1621, 239), (1622, 859),
    (1578, 847), (1578, 837), (1522, 833), (1283, 790),
    (1281, 740), (1275, 732), (1283, 724), (1271, 524),
    (1270, 509), (1271, 504), (1270, 480), (1262, 473),
    (1255, 472), (1252, 467), (1249, 467), (1244, 458),
    (1241, 447)
)
fleury_and_bott_poly = pg.Surface((1634, 1080), flags=pg.SRCALPHA)
fleury_and_bott_rect = pg.draw.polygon(fleury_and_bott_poly, transparent_yellow, fleury_and_bott_cords)

guipure_cords = (
    (294, 804), (295, 503), (291, 482), (286, 468),
    (309, 431), (319, 425), (400, 424), (412, 432),
    (417, 446), (423, 469), (424, 496), (436, 502),
    (428, 510), (424, 515), (436, 517), (448, 525),
    (455, 534), (451, 537), (444, 543), (443, 566),
    (450, 570), (446, 580), (439, 584), (439, 728),
    (444, 729), (439, 735), (438, 750), (372, 756),
    (373, 777), (338, 802), (317, 803), (307, 809)
)
guipure_poly = pg.Surface((1634, 1080), flags=pg.SRCALPHA)
guipure_rect = pg.draw.polygon(guipure_poly, transparent_yellow, guipure_cords)

def Fleury_and_bott(monnaie: int) -> dict:
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

print(Fleury_and_bott(0))
print(Fleury_and_bott(60))
print(Fleury_and_bott(63))
print(Fleury_and_bott(231))
print(Fleury_and_bott(899))


def Guipure(rendu:int) -> dict:
    assert type(rendu) == int

    caisse_dispo = {200 : 1, 100 : 3, 50 : 1 , 20 : 1, 10: 1, 2 :5}
    rendu_caisse ={200 : 0, 100 : 0, 50 : 0, 20 : 0, 10: 0, 2 : 0}
    
    for thune in caisse_dispo:
        while rendu >= thune:
            rendu -= thune
            rendu_caisse[thune] += 1
    
    return rendu_caisse


print(Guipure(0))
print(Guipure(8))
print(Guipure(62))
print(Guipure(231))
print(Guipure(497))
print(Guipure(842))

def alley(mouse_pos):
    for event in pg.event.get():
        if event.type == pg.MOUSEBUTTONDOWN :
            print(pg.mouse.get_pos())
        if event.type == pg.QUIT:
            pg.quit()
            quit()
    
    # On affiche l'image du chemin de traverse
    screen.blit(img_chemin, (0, 0))

    # On surligne le magasin si on a la souris dessus
    if ollivander_rect.collidepoint(mouse_pos[0], mouse_pos[1]):
        screen.blit(ollivander_poly, (0, 0))
    elif fleury_and_bott_rect.collidepoint(mouse_pos[0], mouse_pos[1]):
        screen.blit(fleury_and_bott_poly, (0, 0))
    elif guipure_rect.collidepoint(mouse_pos[0], mouse_pos[1]):
        screen.blit(guipure_poly, (0, 0))

# Affichage du nombre de FPS -- TEMPORAIRE
font = pg.font.SysFont("Arial", 18)
def update_fps():
	fps = str(int(clock.get_fps()))
	fps_text = font.render(fps, 1, pg.Color("coral"))
	return fps_text

def main():
    prev_mouse_pos = [0, 0]
    while 1:
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.key == pg.K_ESCAPE if event.type == pg.KEYDOWN else 0):
                pg.quit()
                quit()
        
        # Si la position de la souris n'a pas changé, on n'a pas besoin de refaire une frame
        mouse_pos = pg.mouse.get_pos()
        if prev_mouse_pos != mouse_pos:
            alley(mouse_pos)
            prev_mouse_pos = mouse_pos
        
        screen.blit(update_fps(), (10,0))
        pg.display.update()
        clock.tick(FPS)

main()