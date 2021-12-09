import os
import pygame as pg

pg.init()

os.environ["SDL_VIDEO_CENTERED"] = "1"  # On centre la fenêtre PyGame
# On initialise la fenêtre de 800 par 600 pixels
screen = pg.display.set_mode((0, 0), pg.FULLSCREEN, pg.RESIZABLE)

# On définit plusieurs couleurs au format rgb
white = (255, 255, 255)
black = (0, 0, 0)
gray = (50, 50, 50)
red = (255, 0, 0)
green = (34, 139, 34)
violet = (128, 0, 128)
blue = (0, 0, 255)
yellow = (255, 255, 0)
golden = (212, 175, 55)
silver = (192, 192, 192)
bronze = (205, 127, 50)
orange = (255, 140, 0)

clock = pg.time.Clock()
FPS = 30
# On utilise une police d"écriture spécifique
font = "HarryPotterFont.ttf"
pg.display.update()
# On définit la vitesse de rafraichissement à 30 FPS
clock.tick(FPS)
# On définit le titre de la fenêtre
pg.display.set_caption("HARRY POTTER SE FAITY LA MALLE")
# On affiche l'image du chemin de traverse
img_chemin = pg.image.load("chemin_de_traverse.png")
screen.blit(img_chemin, (0, 0))
pg.display.update()

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
pg.time.wait(10000)