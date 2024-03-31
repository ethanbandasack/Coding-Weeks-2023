from time import sleep
from random import randint
import pygame
from PIL import Image
from fenetre_simulation import fenetre_simulation
from fenetre_simulation import jours_d_immunite
import sys
sys.path.append("back-end")
from def_class import *
from init_grille import *
from statistiques import *


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
GREEN2 = (0, 210, 0)
DARKGREEN = (0, 169, 0)
DARKGREEN2 = (0, 100, 0)
GRAY = (169, 169, 169)
RED = (255, 0, 0)
RED2 = (169, 0, 0)
BROWN = (200, 160, 120)
BROWN2 = (165, 42, 42)
PURPLE = (255, 0, 255)
PURPLE2 = (169, 0, 169)

color_select = ["plante", "contamine"]
color_preview = [GREEN2, RED2, DARKGREEN2, BROWN2, PURPLE2]


def draw_block(x, y, color, fenetre, block_size, x0, y0, circ=False):
    """
    trace un rectangle ou un cercle sur une case de coordonnées (x,y) de la grille donnée
    :param x: (int) abscisse de la case choisie sur la grille
    :param y: (int) ordonnée de la case choisie sur la grille
    :param color: tuple(int) couleur choisie
    :param fenetre: (pygame.surface.Surface) fenêtre sur laquelle la grille est
    :param block_size: (int) taille d'une case de la grille
    :param circ: (bool) trace un disque si circ=True, colore la case entière sinon"""

    if circ:
        pygame.draw.circle(fenetre, color, (x0+(x+.5)*block_size //
                           1, y0+(y+.5)*block_size//1), block_size//3)
    else:
        pygame.draw.rect(fenetre, color, (x0+x*block_size,
                         y0+y*block_size, block_size, block_size))


def afficher_info(info, y, fenetre, font, x=950, largeur=200, hauteur=20):
    """
    Création d'une zone de texte, texte en blanc
    :param info: (str) chaîne de caractères à afficher, éventuellement un f-string
    :param y: (int) ordonnée du bord supérieur gauche de la zone de texte
    :param fenetre: (pygame.surface.Surface) fenêtre sur laquelle le texte va s'afficher
    :param font: (pygame.font.Font) police d'écriture du texte
    :param x: (int) abscisse du bord supérieur gauche de la zone de texte
    :param largeur: (int) largeur, en pixels, de la zone de texte
    :param hauteur: (int) hauteur, en pixels, de la zone de texte"""

    button_info = pygame.Rect(x, y, largeur, hauteur)
    texte_info = font.render(info, True, WHITE)
    text_info = texte_info.get_rect(center=button_info.center)
    fenetre.blit(texte_info, text_info)


def fenetre_initialisation(valeurs, valeurs2, grille=0, date=0, valeurs_courbes=([], [], [], [], [], [])):
    """affiche la fenêtre qui permet d'initialiser une grille manuellement

    :param valeurs: (tuple(float)), size 10, contient les paramètres concernant les plantes

    :param valeurs2: (tuple(float)), size 11, contient les paramètres concernant les animaux

    :param grille: (Cellule array array), grille à l'état à partir duquel la simulation se fait,
    vaut 0 (type int) si la grille n'est pas initialisée

    :param date: (int) date actuelle, vaut 0 par défaut si on initialise une nouvelle grille
    sans reprendre une simulation en cours

    :param valeurs_courbes: (array(list(int))), size 6, valeurs stockées pour les courbes en cas de pause"""

    # Grille initiale
    m, n = int(valeurs[0]), int(valeurs[1])

    xmax, ymax = 1200, 700
    initialisation = pygame.display.set_mode((xmax, ymax), 0, 24)
    pygame.display.set_caption("Jeu de la survie - Initilisation")
    initialisation.fill(BLACK)

    color_selector = 0
    appui = False
    running, start = True, True
    while running:

        block_size = min((xmax-300)//m, ymax//n)
        x0, y0 = (xmax-300 - block_size*m)//2, (ymax - block_size*n)//2

        if type(grille) == int:  # grille vide si la grille n'a pas été spécifiée
            grille = initialisation_vide((m, n))

        pygame.draw.rect(initialisation, BLACK, (0, 0, 900, 700))
        for i in range(m):
            for j in range(n):
                pygame.draw.rect(initialisation, WHITE, (x0+i*block_size+1,
                                 y0+j*block_size+1, block_size-2, block_size-2))

        pygame.display.flip()
        sleep(0.1)

        indicex, indicey = 0, 0

        appui_gauche, appui_droit = False, False
        start = True
        while start:

            initialisation.fill(BLACK)

            mouse_pos = pygame.mouse.get_pos()
            x_i = mouse_pos[0]
            y_i = mouse_pos[1]
            if 0 <= x_i-x0 < m*block_size and 0 <= y_i-y0 < n*block_size:
                indicex = (x_i-x0)//block_size
                indicey = (y_i-y0)//block_size

            for i in range(m):
                for j in range(n):
                    case = grille[i, j]
                    if case.status == "plante":
                        if case.is_immune(date):
                            draw_block(i, j, DARKGREEN,
                                       initialisation, block_size, x0, y0)
                        else:
                            draw_block(i, j, GREEN, initialisation,
                                       block_size, x0, y0)
                    elif case.status == "vide":
                        draw_block(i, j, WHITE, initialisation,
                                   block_size, x0, y0)
                    elif case.status == "contamine":
                        draw_block(i, j, RED, initialisation,
                                   block_size, x0, y0)

                    if case.nb_mout() and case.nb_loup():
                        pygame.draw.circle(
                            initialisation, PURPLE, (x0+(i+.5)*block_size//1, y0+(j+.5)*block_size//1), block_size//3)
                        pygame.draw.circle(
                            initialisation, BROWN, (x0+(i+.5)*block_size//1, y0+(j+.5)*block_size//1), block_size//6)
                    elif case.nb_loup():
                        draw_block(i, j, PURPLE, initialisation,
                                   block_size, x0, y0, True)
                    elif case.nb_mout():
                        draw_block(i, j, BROWN, initialisation,
                                   block_size, x0, y0, True)

            cell = grille[indicex, indicey]
            if color_selector < 2:  # placement des plantes saines et infectées
                if cell.status == color_select[color_selector]:
                    draw_block(indicex, indicey, GRAY,
                               initialisation, block_size, x0, y0)
                else:
                    draw_block(
                        indicex, indicey, color_preview[color_selector], initialisation, block_size, x0, y0)
            elif color_selector == 2:  # placement des plantes immunisées
                if cell.is_immune(date):
                    draw_block(indicex, indicey, GRAY,
                               initialisation, block_size, x0, y0)
                else:
                    draw_block(
                        indicex, indicey, color_preview[color_selector], initialisation, block_size, x0, y0)
            elif color_selector == 3:  # placement des moutons (1 par case)
                if cell.nb_mout():
                    draw_block(indicex, indicey, GRAY,
                               initialisation, block_size, x0, y0, True)
                else:
                    draw_block(
                        indicex, indicey, color_preview[color_selector], initialisation, block_size, x0, y0, True)
            elif color_selector == 4:  # placement des loups (1 par case)
                if cell.nb_loup():
                    draw_block(indicex, indicey, GRAY,
                               initialisation, block_size, x0, y0, True)
                else:
                    draw_block(
                        indicex, indicey, color_preview[color_selector], initialisation, block_size, x0, y0, True)

            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    running = False
                    start = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 5:  # si la molette descend
                        color_selector = (color_selector-1) % 5
                    elif event.button == 4:  # si la molette monte
                        color_selector = (color_selector+1) % 5
                    elif event.button == 1:  # si clic gauche
                        appui_gauche = True
                    elif event.button == 3:  # si clic droit
                        appui_droit = True
                elif event.type == pygame.MOUSEBUTTONUP:
                    appui_gauche, appui_droit = False, False

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT and m > 2:
                        m -= 1
                        grille = grille[:m]
                    elif event.key == pygame.K_RIGHT:
                        m += 1
                        grille2 = initialisation_vide((m, n))
                        grille2[:m-1, :] = grille
                        grille = grille2.copy()
                    elif event.key == pygame.K_DOWN and n > 2:
                        n -= 1
                        grille = grille[:, :n]
                    elif event.key == pygame.K_UP:
                        n += 1
                        grille2 = initialisation_vide((m, n))
                        grille2[:, :n-1] = grille
                        grille = grille2.copy()
                    elif event.key == pygame.K_SPACE:
                        running = False
                        fenetre_simulation(
                            [m, n]+valeurs[2:], valeurs2, grille, date, valeurs_courbes)
                    start = False

            if appui_droit:  # retirer
                if color_selector < 2 and cell.status == color_select[color_selector]:
                    cell.status = "vide"
                if color_selector == 2 and cell.is_immune(date):
                    cell.immune = date
                if color_selector == 3 and cell.nb_mout():
                    cell.anim.pop("mouton")
                if color_selector == 4 and cell.nb_loup():
                    cell.anim.pop("loup")

            if appui_gauche:  # placer
                if color_selector < 2:
                    cell.status = color_select[color_selector]
                    cell.immune = date-1
                if color_selector == 2:
                    cell.status = "plante"
                    cell.immune = date + jours_d_immunite
                if color_selector == 3 and cell.nb_mout() == 0:
                    cell.ajoute_anim(
                        Animal("mouton", date, randint(0, 1), date))
                if color_selector == 4 and cell.nb_loup() == 0:
                    cell.ajoute_anim(Animal("loup", date, randint(0, 1), date))

            # affichage de la légende
            afficher_info('clic gauche pour placer', 300,
                          initialisation, pygame.font.SysFont(None, 24), 970, 200)

            pygame.draw.rect(initialisation, GREEN, (920, 325, 20, 20))
            afficher_info('plante saine', 325, initialisation,
                          pygame.font.SysFont(None, 24), 950, 180)
            pygame.draw.rect(initialisation, GREEN2, (1150, 325, 20, 20))

            pygame.draw.rect(initialisation, RED, (920, 350, 20, 20))
            afficher_info('plante infectée', 350, initialisation,
                          pygame.font.SysFont(None, 24), 950, 180)
            pygame.draw.rect(initialisation, RED2, (1150, 350, 20, 20))

            pygame.draw.circle(initialisation, BROWN, (930, 385), 10)
            afficher_info('mouton', 375, initialisation,
                          pygame.font.SysFont(None, 24), 950, 180)
            pygame.draw.circle(initialisation, BROWN2, (1160, 385), 10)

            pygame.draw.circle(initialisation, PURPLE, (930, 410), 10)
            afficher_info('loup', 400, initialisation,
                          pygame.font.SysFont(None, 24), 950, 180)
            pygame.draw.circle(initialisation, PURPLE2, (1160, 410), 10)

            pygame.draw.rect(initialisation, DARKGREEN, (920, 432.5, 20, 20))
            afficher_info('clic gauche pour', 425, initialisation,
                          pygame.font.SysFont(None, 24), 950, 180)
            afficher_info('immuniser une plante', 440, initialisation,
                          pygame.font.SysFont(None, 24), 950, 180)
            pygame.draw.rect(initialisation, DARKGREEN2, (1150, 432.5, 20, 20))

            afficher_info('clic droit pour retirer', 500,
                          initialisation, pygame.font.SysFont(None, 24), 950, 190)
            afficher_info("l'entité ou l'immunité", 525, initialisation,
                          pygame.font.SysFont(None, 24), 950, 190)
            pygame.draw.rect(initialisation, GRAY, (1150, 500, 20, 20))
            pygame.draw.circle(initialisation, GRAY, (1160, 535), 10)

            # affichage des informations sur la grille
            vides, plantes, contamines, immunisees, moutons, loups = count(
                grille, date)
            afficher_info('Taille de la grille', 10, initialisation,
                          pygame.font.SysFont(None, 32), 950, 160)
            afficher_info('Nombre de cases', 35, initialisation,
                          pygame.font.SysFont(None, 32), 950, 160)
            afficher_info('Plantes saines', 60, initialisation,
                          pygame.font.SysFont(None, 32), 950, 160)
            afficher_info('dont immunisées', 85, initialisation,
                          pygame.font.SysFont(None, 32), 950, 160)
            afficher_info('Plantes infectées', 110, initialisation,
                          pygame.font.SysFont(None, 32), 950, 160)
            afficher_info('Nombre de moutons', 135, initialisation,
                          pygame.font.SysFont(None, 32), 950, 160)
            afficher_info('Nombre de loups', 160, initialisation,
                          pygame.font.SysFont(None, 32), 950, 160)
            afficher_info('Date', 185, initialisation,
                          pygame.font.SysFont(None, 32), 950, 160)

            afficher_info(f'{m}×{n}', 10, initialisation,
                          pygame.font.SysFont(None, 32), 1140, 40)
            afficher_info(str(m*n), 35, initialisation,
                          pygame.font.SysFont(None, 32), 1140, 40)
            afficher_info(str(plantes), 60, initialisation,
                          pygame.font.SysFont(None, 32), 1140, 40)
            afficher_info(str(immunisees), 85, initialisation,
                          pygame.font.SysFont(None, 32), 1140, 40)
            afficher_info(str(contamines), 110, initialisation,
                          pygame.font.SysFont(None, 32), 1140, 40)
            afficher_info(str(moutons), 135, initialisation,
                          pygame.font.SysFont(None, 32), 1140, 40)
            afficher_info(str(loups), 160, initialisation,
                          pygame.font.SysFont(None, 32), 1140, 40)
            afficher_info(str(date), 185, initialisation,
                          pygame.font.SysFont(None, 32), 1140, 40)

            afficher_info("Presser la barre ESPACE", 600,
                          initialisation, pygame.font.SysFont(None, 32), 950, 200)
            afficher_info("pour lancer la simulation", 625,
                          initialisation, pygame.font.SysFont(None, 32), 950, 200)
            afficher_info("avec la grille ci-contre", 650,
                          initialisation, pygame.font.SysFont(None, 32), 950, 200)

            pygame.display.flip()  # On actualise la fenetre
