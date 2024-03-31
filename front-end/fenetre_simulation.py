import pygame
import numpy as np
import random as rd
from time import sleep
import matplotlib.pyplot as plt
from fenetre_pause import *
from fenetre_voisins import *
from screeninfo import get_monitors
from matplotlib.backends.backend_agg import FigureCanvasAgg
import sys
sys.path.append("back-end")
from init_grille import *
from generation import *
from animaux import *
from statistiques import *

# Paramètres de la simulation

fps = 10

# Récupération du nombre de pixels par pouce sur l'écran
monitor = get_monitors()[0]
ppi = monitor.width / (monitor.width_mm / 25.4)

# Grille initiale
m, n = 10, 10
p_plante = 0.5
p_contamine = 0.2

# Probabilités concernant les plantes
p_tuer = 0.4
p_infect = 0.8
p_repro = 0.7
jours_avant_immunite = 4
jours_d_immunite = 5
mort_de_surpopulation_plantes = 5


# Probabilités concernant les animaux
age_max_moutons = 15
age_max_loups = 15
nb_surpop = 4
nb_jours_avant_famine = 4
proba_dep = 0.5
proba_repro_loup = 0.3
proba_repro_mout = 0.3

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


def draw_block(x, y, color, fenetre, block_size, x0, y0, circ=False):
    """
    trace un rectangle ou un cercle sur une case de coordonnées (x,y) de la grille donnée
    :param x: (int) abscisse de la case choisie sur la grille
    :param y: (int) ordonnée de la case choisie sur la grille
    :param color: (tuple(int)) couleur choisie
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
    Création d'une zone de texte, texte en noir
    :param info: (str) chaîne de caractères à afficher, éventuellement un f-string
    :param y: (int) ordonnée du bord supérieur gauche de la zone de texte
    :param fenetre: (pygame.surface.Surface) fenêtre sur laquelle le texte va s'afficher
    :param font: (pygame.font.Font) police d'écriture du texte
    :param x: (int) abscisse du bord supérieur gauche de la zone de texte
    :param largeur: (int) largeur, en pixels, de la zone de texte
    :param hauteur: (int) hauteur, en pixels, de la zone de texte"""

    button_info = pygame.Rect(x, y, largeur, hauteur)
    texte_info = font.render(info, True, BLACK)
    text_info = texte_info.get_rect(center=button_info.center)
    fenetre.blit(texte_info, text_info)


def fenetre_simulation(valeurs, valeurs2, grille=0, date=0, valeurs_courbes=([], [], [], [], [], [])):
    """
    fenêtre dans laquelle la simulation tourne,
    des courbes peuvent être affichées ou non ;
    la grille utilise les paramètres de la fenêtre d'accueil,
    et est par défaut générée aléatoirement selon ces paramètres

    :param valeurs: (tuple(float)), size 10, contient les paramètres concernant les plantes

    :param valeurs2: (tuple(float)), size 11, contient les paramètres concernant les animaux

    :param grille: (Cellule array array), grille à l'état à partir duquel la simulation se fait,
    vaut 0 (type int) si la grille n'est pas initialisée

    :param date: (int) date actuelle, vaut 0 par défaut si on initialise une nouvelle grille
    sans reprendre une simulation en cours

    :param valeurs_courbes: (array(list(int))), size 6, valeurs stockées pour les courbes en cas de pause"""

    x, courbe_plante, courbe_contamine, courbe_immunise, courbe_mouton, courbe_loup = valeurs_courbes
    # Grille initiale
    m, n = int(valeurs[0]), int(valeurs[1])
    p_plante = valeurs[2]
    p_contamine = valeurs[3]
    # Probabilités
    p_tuer = valeurs[4]
    p_infect = valeurs[5]
    p_repro = valeurs[6]
    jours_avant_immunite = valeurs[7]
    jours_d_immunite = valeurs[8]
    mort_de_surpopulation = valeurs[9]

    # Paramètres animaux

    age_max_moutons = valeurs2[0]
    age_max_loups = valeurs2[1]
    nb_surpop = valeurs2[2]
    nb_jours_avant_famine = valeurs2[3]
    proba_dep = valeurs2[4]
    proba_repro_loup = valeurs2[5]
    proba_repro_mout = valeurs2[6]
    proba_poisson_loup = valeurs2[7]
    proba_poisson_mouton = valeurs2[8]
    proba_uniforme_loup = valeurs2[9]
    proba_uniforme_mouton = valeurs2[10]
    loi = valeurs2[11]

    if type(grille) == int:  # si la grille n'est pas spécifiée
        grille = initialisation_rdm((m, n), p_plante, p_contamine)
        if loi:
            random_spawn(grille, proba_uniforme_loup, proba_uniforme_mouton)
        else:
            random_spawn_poisson(
                grille, proba_poisson_loup, proba_poisson_mouton)

    xmax, ymax = 1200, 700
    block_size = min((xmax-300)//m, ymax//n)
    x0, y0 = (xmax-300 - block_size*m)//2, (ymax - block_size*n)//2

    # Initialisation des données Matplotlib
    vides, plantes, contamines, immunisees, moutons, loups = count(
        grille, date)
    x.append(date)
    courbe_plante.append((plantes-immunisees)/m/n)
    courbe_contamine.append(contamines/m/n)
    courbe_immunise.append(immunisees/m/n)
    courbe_mouton.append(moutons/m/n)
    courbe_loup.append(loups/m/n)

    simulation = pygame.display.set_mode((xmax, ymax), flags=pygame.RESIZABLE)

    pygame.display.set_caption("Jeu de la survie - Simulation")
    clock = pygame.time.Clock()

    # affiche par défaut la grille en grand et les courbes en petit
    courbe = False
    slow = False  # matplotlib ralentit le script

    running_s = True
    while running_s:

        # récupération de la position de la souris
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running_s = False

            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    running_s = False

                elif event.key == pygame.K_a:  # relance une simulation aléatoire
                    grille = initialisation_rdm((m, n), p_plante, p_contamine)
                    random_spawn_poisson(grille, 3, 3)
                    date = 0

                elif event.key == pygame.K_c:  # change de mode d'affichage
                    courbe = not courbe

                elif event.key == pygame.K_s:  # génère ou non les courbes
                    slow = not slow

                elif event.key == pygame.K_SPACE:
                    valeurs_courbes = (
                        x, courbe_plante, courbe_contamine, courbe_immunise, courbe_mouton, courbe_loup)
                    running_s = fenetre_pause(date, grille, valeurs_courbes, valeurs,
                                              valeurs2, fenetre=simulation, running_s=running_s)
                    pygame.display.set_caption("Jeu de la survie - Simulation")

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 950 <= mouse_pos[0] <= 1150 and 550 <= mouse_pos[1] <= 600 and courbe:
                    courbe = False
                elif 950 <= mouse_pos[0] <= 1150 and 620 <= mouse_pos[1] <= 670:
                    valeurs_courbes = (
                        x, courbe_plante, courbe_contamine, courbe_immunise, courbe_mouton, courbe_loup)
                    running_s = fenetre_pause(date, grille, valeurs_courbes, valeurs,
                                              valeurs2, fenetre=simulation, running_s=running_s)
                    pygame.display.set_caption("Jeu de la survie - Simulation")
                elif mouse_pos[0] >= 900 and not courbe:
                    courbe = True

        simulation.fill(WHITE)

        if courbe:  # bouton de retour sur la grille
            button_courbe = pygame.Rect(950, 550, 200, 50)
            pygame.draw.rect(simulation, GRAY, button_courbe,
                             border_radius=10)
            if button_courbe.collidepoint(mouse_pos):
                pygame.draw.rect(simulation, GREEN, button_courbe,
                                 border_radius=10)
            font = pygame.font.SysFont(None, 36)
            text4 = font.render('Grille', True, BLACK)
            text_courbe = text4.get_rect(center=button_courbe.center)
            simulation.blit(text4, text_courbe)

        if mouse_pos[0] >= 900 and not courbe:
            pygame.draw.rect(simulation, GRAY, (900, 0, 300, 700))

        # bouton de mise en pause
        button_pause = pygame.Rect(950, 620, 200, 50)
        pygame.draw.rect(simulation, GRAY, button_pause,
                         border_radius=10)
        if button_pause.collidepoint(mouse_pos):
            pygame.draw.rect(simulation, GREEN, button_pause,
                             border_radius=10)
        font = pygame.font.SysFont(None, 36)
        text5 = font.render('Pause', True, BLACK)
        text_pause = text5.get_rect(center=button_pause.center)
        simulation.blit(text5, text_pause)

        # remplissage de la grille en cas de mode grille
        if not courbe:
            for i in range(m):
                for j in range(n):
                    case = grille[i, j]
                    if case.status == "plante":
                        if case.is_immune(date):
                            draw_block(i, j, DARKGREEN, simulation,
                                       block_size, x0, y0)
                        else:
                            draw_block(i, j, GREEN, simulation,
                                       block_size, x0, y0)
                    elif case.status == "vide":
                        draw_block(i, j, WHITE, simulation, block_size, x0, y0)
                    elif case.status == "contamine":
                        draw_block(i, j, RED, simulation, block_size, x0, y0)

                    if case.nb_mout() and case.nb_loup():
                        pygame.draw.circle(
                            simulation, PURPLE, (x0+(i+.5)*block_size//1, y0+(j+.5)*block_size//1), block_size//3)
                        pygame.draw.circle(
                            simulation, BROWN, (x0+(i+.5)*block_size//1, y0+(j+.5)*block_size//1), block_size//6)
                    elif case.nb_loup():
                        draw_block(i, j, PURPLE, simulation,
                                   block_size, x0, y0, True)
                    elif case.nb_mout():
                        draw_block(i, j, BROWN, simulation,
                                   block_size, x0, y0, True)

        # mise à jour de la grille
        grille = update_grille(grille, p_repro, p_infect, p_tuer, date,
                               jours_avant_immunite, jours_d_immunite, mort_de_surpopulation)
        update_animaux(grille, date, age_max_moutons, age_max_loups, nb_surpop,
                       nb_jours_avant_famine, proba_dep, proba_repro_loup, proba_repro_mout)

        vides, plantes, contamines, immunisees, moutons, loups = count(
            grille, date)

        if slow:
            # initialisation de Matplotlib
            if courbe:
                fig, (ax, ax_animaux) = plt.subplots(
                    2, 1, figsize=(1100/ppi, 900/ppi))
            else:
                fig, (ax, ax_animaux) = plt.subplots(
                    2, 1, figsize=(400/ppi, 550/ppi))
            canvas = FigureCanvasAgg(fig)

            # mise à jour de l'animation Matplotlib
            x.append(date)
            courbe_plante.append((plantes-immunisees)/m/n)
            courbe_contamine.append(contamines/m/n)
            courbe_immunise.append(immunisees/m/n)
            courbe_mouton.append(moutons/m/n)
            courbe_loup.append(loups/m/n)

            ax.clear()
            ax.stackplot(x, courbe_plante, courbe_immunise, courbe_contamine, labels=[
                "Plantes saines", "Plantes immunisées", "Plantes contaminées"])            
            legende_plantes = ax.legend(loc="upper left")

            ax_animaux.clear()
            ax_animaux.plot(x, courbe_mouton, label="Moutons")
            ax_animaux.plot(x, courbe_loup, label="Loups")
            
            # affiche la partie intéressante du graphique sur les animaux
            if date > 50:
                ylim = max(courbe_mouton[-50:]+courbe_loup[-50:])
                ax_animaux.set_ylim(0, ylim)
                ax_animaux.set_xlim(date-50, date)

            legende_animaux = ax_animaux.legend(loc="upper left")

            if not courbe:
                for text in legende_plantes.get_texts():
                    text.set_fontsize(8)
                for text in legende_animaux.get_texts():
                    text.set_fontsize(8)

            canvas.draw()

            # Affichage de l'image Matplotlib dans la fenêtre Pygame
            renderer = canvas.get_renderer()
            raw_data = renderer.tostring_rgb()
            size = canvas.get_width_height()
            img_surface = pygame.image.fromstring(raw_data, size, "RGB")

            if courbe:
                simulation.blit(img_surface, (25, 50))
            else:
                simulation.blit(img_surface, (910, 225))

        else:
            afficher_info("Appuyer sur S pour", 400, simulation,
                          pygame.font.SysFont(None, 32), 950, 200)
            afficher_info("afficher les graphiques", 425, simulation,
                          pygame.font.SysFont(None, 32), 950, 200)
            afficher_info("(attention aux", 450, simulation,
                          pygame.font.SysFont(None, 32), 950, 200)
            afficher_info("ralentissements !)", 475, simulation,
                          pygame.font.SysFont(None, 32), 950, 200)

        # affichage des informations sur la grille
        afficher_info('Taille de la grille', 10, simulation,
                      pygame.font.SysFont(None, 32), 950, 160)
        afficher_info('Nombre de cases', 35, simulation,
                      pygame.font.SysFont(None, 32), 950, 160)
        afficher_info('Plantes saines', 60, simulation,
                      pygame.font.SysFont(None, 32), 950, 160)
        afficher_info('dont immunisées', 85, simulation,
                      pygame.font.SysFont(None, 32), 950, 160)
        afficher_info('Plantes infectées', 110, simulation,
                      pygame.font.SysFont(None, 32), 950, 160)
        afficher_info('Nombre de moutons', 135, simulation,
                      pygame.font.SysFont(None, 32), 950, 160)
        afficher_info('Nombre de loups', 160, simulation,
                      pygame.font.SysFont(None, 32), 950, 160)
        afficher_info('Date', 185, simulation,
                      pygame.font.SysFont(None, 32), 950, 160)

        afficher_info(f'{m}×{n}', 10, simulation,
                      pygame.font.SysFont(None, 32), 1140, 40)
        afficher_info(str(m*n), 35, simulation,
                      pygame.font.SysFont(None, 32), 1140, 40)
        afficher_info(str(plantes), 60, simulation,
                      pygame.font.SysFont(None, 32), 1140, 40)
        afficher_info(str(immunisees), 85, simulation,
                      pygame.font.SysFont(None, 32), 1140, 40)
        afficher_info(str(contamines), 110, simulation,
                      pygame.font.SysFont(None, 32), 1140, 40)
        afficher_info(str(moutons), 135, simulation,
                      pygame.font.SysFont(None, 32), 1140, 40)
        afficher_info(str(loups), 160, simulation,
                      pygame.font.SysFont(None, 32), 1140, 40)
        afficher_info(str(date), 185, simulation,
                      pygame.font.SysFont(None, 32), 1140, 40)

        if courbe:
            afficher_info("Proportion sur la grille", 20, simulation,
                          pygame.font.SysFont(None, 48), 20, 400, 75)
        else:
            afficher_info("Proportion sur la grille", 235,
                          simulation, pygame.font.SysFont(None, 32), 950, 200)

        pygame.display.flip()  # on actualise la fenetre
        plt.close("all")  # fermeture de toutes les figures matplotlib
        date += 1
        clock.tick(fps)  # réglage du framerate
