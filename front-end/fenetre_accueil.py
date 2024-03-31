import pygame
from fenetre_initialisation import fenetre_initialisation
from fenetre_simulation import fenetre_simulation
import pygame_widgets
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox
from time import sleep

# On indique le chemin vers l'image d'accueil
image_path = "front-end/image/ecran_affichage_dessin.jpg"

# On initialise les couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
DARKGREEN = (0, 169, 0)
GRAY = (169, 169, 169)
RED = (255, 0, 0)
GRAY_FAIBLE = (200, 200, 200)
# On initiliase les liste qui contiendront les sliderbar et les textbox pour les pages 1 et 2 de parametre
# Ainsi que la liste qui contiendra les valeurs données pour les pages 1 et 2
slider_list_1 = []
slider_list_2 = []
text_box_1 = []
text_box_2 = []
valeur_1 = [10, 10, 0.5, 0.2, 0.02, 0.8, 0.5, 5, 5, 6]
valeur_2 = [60, 60, 4, 20, 0.5, 0.3, 0.3, 0.2, 0.5, 0.1, 0.3]
loi = 0  # Lorsque loi vaut 0 on a une loi de poisson et sinon une loi uniforme

# La fonction fenetre_parametre permet d'afficher la première fenetre de paramètre


def fenetre_parametre(fen_parametre):
    """permet d'afficher la première fenetre de paramètre
    :param fen_parametre: (pygame.surface.Surface) fenêtre sur laquelle sera affichée les paramètres"""

    pygame.draw.rect(fen_parametre, WHITE, pygame.Rect(
        25, 25, 475, 525), border_radius=20)
    # On remplit en blanc l'endroit où seront mis les sliders pour les paramètres
    nom_param = ["Largeur de la grille", "Hauteur de la grille", "Probabilité plante", "Probabilité contaminé", "Probabilité tuer",
                 "Probabilité d'infection", "Probabilité reproduction", "Jours avant immunité", "jours d'immunité", "Mort de surpopulation"]
    # Les noms des paramètres à choisir
    font = pygame.font.Font(None, 36)
    for i in range(len(nom_param)):  # On affiche les noms des paramètres
        text = font.render(f"{nom_param[i]}:", True, BLACK)
        fen_parametre.blit(text, (50, 50 + i * 50))

    for i in range(10):
        # On affecte à la variable valeur_1 la liste des valeurs des sliders
        valeur_1[i] = slider_list_1[i].getValue()
        # On limite à 2 chiffres après la virgule pour plus de lisibilité
        valeur_1[i] = int(valeur_1[i]*100)/100
        text_box_1[i].setText(valeur_1[i])  # On affiche la variable


# la fonction fenetre_parametre2 permet d'afficher la seconde fenetre de paramètres
def fenetre_parametre2(fen_parametre):
    """permet d'afficher la seconde fenetre de paramètre
    :param fen_parametre: (pygame.surface.Surface) fenêtre sur laquelle sera affichée les paramètres"""

    pygame.draw.rect(fen_parametre, WHITE, pygame.Rect(
        25, 25, 475, 525), border_radius=20)

    # On remplit en blanc l'endroit où seront mis les sliders pour les paramètres
    nom_param = ["Age max mout", "Age max loup", "Nombre avant surpop",
                 "Famine", "Proba déplacement", "Proba repro loup", "Proba repro mout"]
    # Les noms des paramètres à choisir
    font = pygame.font.Font(None, 36)
    for i in range(len(nom_param)):  # On affiche les noms des paramatres
        text = font.render(f"{nom_param[i]}:", True, BLACK)
        fen_parametre.blit(text, (50, 50 + i * 50))

    for i in range(len(nom_param)):
        # On affecte la variable valeur_1 à la liste des valeurs des slide_bar
        valeur_2[i] = slider_list_2[i].getValue()
        # On limite à 2 chiffres après la virgule pour plus de fluidité
        valeur_2[i] = int(valeur_2[i]*100)/100
        text_box_2[i].setText(valeur_2[i])  # On affiche la variable

    # On initialise les parametres des boutons liés aux lois
    button_width_loi = 200
    button_height_loi = 50
    button_radius_loi = 10
    button_thickness = 3
    button_poisson = pygame.Rect(50, 400, button_width_loi, button_height_loi)
    button_uniforme = pygame.Rect(
        275, 400, button_width_loi, button_height_loi)
    font = pygame.font.SysFont(None, 36)
    global loi  # On appelle la variable loi qui caractérise si on est dans la version uniforme, ou la version poisson
    if (loi == 0):  # Si on est dans l'état dans lequel on veut une loi de poisson

        # On gère les affichages des différentes barres et de la text box
        slider_list_2[7].show()
        slider_list_2[8].show()
        text_box_2[7].show()
        text_box_2[8].show()
        slider_list_2[9].hide()
        slider_list_2[10].hide()
        text_box_2[9].hide()
        text_box_2[10].hide()

        # On affiche les noms des 2 boutons
        text_bouton_poisson = font.render('Poisson', True, BLACK)
        text_poisson = text_bouton_poisson.get_rect(
            center=button_poisson.center)
        text_bouton_uniforme = font.render('Uniforme', True, WHITE)
        text_uniforme = text_bouton_poisson.get_rect(
            center=button_uniforme.center)

        # On affiche les boutons et le bouton poisson sera creux pour comprendre qu'il est enfoncé
        pygame.draw.rect(fen_parametre, BLACK, button_poisson,
                         border_radius=button_radius_loi)
        pygame.draw.rect(fen_parametre, GRAY_FAIBLE,
                         button_uniforme, border_radius=button_radius_loi)
        pygame.draw.rect(fen_parametre, WHITE, button_poisson.inflate(
            -button_thickness, -button_thickness), border_radius=button_radius_loi)

        # On affiche les noms des variables
        fen_parametre.blit(text_bouton_poisson, text_poisson)
        fen_parametre.blit(text_bouton_uniforme, text_uniforme)
        lambda_text = font.render(f"lambda loup:", True, BLACK)
        fen_parametre.blit(lambda_text, (50, 50 + 8 * 50+15))
        lambda_text = font.render(f"lambda mouton:", True, BLACK)
        fen_parametre.blit(lambda_text, (50, 50 + 8 * 50+55))

        # On relie valeur avec les slidebar et on affiche leur valeur
        valeur_2[7] = slider_list_2[7].getValue()
        valeur_2[7] = int(valeur_2[7]*100)/100
        text_box_2[7].setText(valeur_2[7])
        valeur_2[8] = slider_list_2[8].getValue()
        valeur_2[8] = int(valeur_2[8]*100)/100
        text_box_2[8].setText(valeur_2[8])

    else:  # Sinon on est dans l'état uniforme
        # On gère les affichages des differentes slides bar et text box
        slider_list_2[7].hide()
        slider_list_2[8].hide()
        text_box_2[7].hide()
        text_box_2[8].hide()
        slider_list_2[9].show()
        slider_list_2[10].show()
        text_box_2[9].show()
        text_box_2[10].show()

        # On affiche les noms des 2 boutons
        text_bouton_poisson = font.render('Poisson', True, WHITE)
        text_poisson = text_bouton_poisson.get_rect(
            center=button_poisson.center)
        text_bouton_uniforme = font.render('Uniforme', True, BLACK)
        text_uniforme = text_bouton_poisson.get_rect(
            center=button_uniforme.center)

        # On affiche les boutons et le bouton poisson sera creux pour comprendre qu'il est enfoncé
        pygame.draw.rect(fen_parametre, GRAY_FAIBLE,
                         button_poisson, border_radius=button_radius_loi)
        pygame.draw.rect(fen_parametre, BLACK, button_uniforme,
                         border_radius=button_radius_loi)
        pygame.draw.rect(fen_parametre, WHITE, button_uniforme.inflate(
            -button_thickness, -button_thickness), border_radius=button_radius_loi)

        # On affiche les noms des variables
        fen_parametre.blit(text_bouton_poisson, text_poisson)
        fen_parametre.blit(text_bouton_uniforme, text_uniforme)
        lambda_text = font.render(f"probabilité loup:", True, BLACK)
        fen_parametre.blit(lambda_text, (50, 50 + 8 * 50+15))
        lambda_text = font.render(f"probabilité mouton:", True, BLACK)
        fen_parametre.blit(lambda_text, (50, 50 + 8 * 50+55))

        # On relie valeur avec les sliders et on affiche leurs valeurs
        valeur_2[9] = slider_list_2[9].getValue()
        valeur_2[9] = int(valeur_2[9]*100)/100
        text_box_2[9].setText(valeur_2[9])
        valeur_2[10] = slider_list_2[10].getValue()
        valeur_2[10] = int(valeur_2[10]*100)/100
        text_box_2[10].setText(valeur_2[10])


def fenetre_accueil():
    """apparaît lorsque le programme est lancé et
    permet de choisir les paramètres de la simulation en cliquant sur le bouton Parametre,
    affiche les boutons de la simulation et de l'initialisation (Jouer)"""

    pygame.init()

    # screen_info = pygame.display.Info()
    # screen_size = screen_info.current_w, screen_info.current_h

    accueil = pygame.display.set_mode(
        (1200, 700), 0, 24)  # On initialise la fenetre
    # On choisit le nom de la fenetre
    pygame.display.set_caption("Jeu de la survie - Accueil")

    # On transforme l'image en surface
    image = pygame.image.load(image_path).convert()
    # Initialisation des parametres classiques des boutons
    BUTTON_WIDTH = 200
    BUTTON_HEIGHT = 50
    BUTTON_RADIUS = 10
    font = pygame.font.SysFont(None, 36)
    # On initialise les textes des differents boutons
    text_bouton_jouer = font.render('Jouer', True, BLACK)
    text_bouton_simulation = font.render('Simulation', True, RED)
    text_bouton_parametre = font.render('Parametres', True, DARKGREEN)

    running = True  # Initialisation de running qui permet de decider jusqu'à quand le programme reste ouvert
    affiche_param = 0
    """affiche_param lorsqu'il vaut 0 on affiche pas de page de parametre, lorsqu'il vaut 1 on affiche
    la page et lorsqu'il vaut 2 on affiche la page 2"""
    # Initialisation d'une liste qui contient le minimum, maximum, le pas ainsi que la valeur initial de chaque slidebar
    min_max_step_initial_1 = [(2, 200, 1, valeur_1[0]), (2, 200, 1, valeur_1[1]), (0, 1, 0.01, valeur_1[2]),
                              (0, 1, 0.01, valeur_1[3]), (0, 1, 0.01, valeur_1[4]), (
                                  0, 1, 0.01, valeur_1[5]), (0, 1, 0.01, valeur_1[6]),
                              (0, 100, 1, valeur_1[7]), (0, 100, 1, valeur_1[8]), (0, 10, 1, valeur_1[9])]

    min_max_step_initial_2 = [(1, 300, 1, valeur_2[0]), (1, 300, 1, valeur_2[1]), (0, 10, 1, valeur_2[2]),
                              (0, 300, 1, valeur_2[3]), (0, 1, 0.01, valeur_2[4]), (0, 1, 0.01, valeur_2[5]), (0, 1, 0.01, valeur_2[6])]
    # Initialisation de chaque slidebar à partir des parametres de min_max_step_initial_i avec i=1,2
    for i in range(len(min_max_step_initial_1)):
        min1, max1, step1, initial1 = min_max_step_initial_1[i]
        slider_list_1.append(Slider(accueil, 355, 55+i*50, 100, 10, min=min1,
                             max=max1, step=step1, handleColour=GREEN, initial=initial1))
        text_box_1.append(TextBox(accueil, 385, 100+i*50, 0, 0, fontSize=30))

    for i in range(len(min_max_step_initial_2)):
        min2, max2, step2, initial2 = min_max_step_initial_2[i]
        slider_list_2.append(Slider(accueil, 355, 55+i*50, 100, 10, min=min2,
                             max=max2, step=step2, handleColour=GREEN, initial=initial2))
        text_box_2.append(TextBox(accueil, 385, 100+i*50, 0, 0, fontSize=30))
    global loi

    # Initialisation des slide_bar liés aux lois
    slider_list_2.append(Slider(accueil, 355, 50 + 8 * 50+15, 100,
                         10, min=0, max=10, step=0.1, handleColour=GREEN, initial=3))
    slider_list_2.append(Slider(accueil, 355, 50 + 8 * 50+55, 100,
                         10, min=0, max=10, step=0.1, handleColour=GREEN, initial=3))
    slider_list_2.append(Slider(accueil, 355, 50 + 8 * 50+15, 100,
                         10, min=0, max=1, step=0.01, handleColour=GREEN, initial=0.2))
    slider_list_2.append(Slider(accueil, 355, 50 + 8 * 50+55, 100,
                         10, min=0, max=1, step=0.01, handleColour=GREEN, initial=0.2))
    text_box_2.append(TextBox(accueil, 385, 100 +
                      8 * 50+15, 0, 0, fontSize=30))
    text_box_2.append(TextBox(accueil, 385, 100 +
                      8 * 50+55, 0, 0, fontSize=30))
    text_box_2.append(TextBox(accueil, 385, 100 +
                      8 * 50+15, 0, 0, fontSize=30))
    text_box_2.append(TextBox(accueil, 385, 100 +
                      8 * 50+55, 0, 0, fontSize=30))

    while running:
        accueil.fill(WHITE)  # On remplit la page entierement de blanc
        accueil.blit(image, (0, 0))  # On met l'image convertit precedemment
        # choix = True
        mouse_pos = pygame.mouse.get_pos()  # On récupere la position de la souris
        # On recupere les events (=les actions réalisé par l'utilisateur)
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                running = False  # On ferme le programme si on clique sur certaines touche ou la croix
            elif event.type == pygame.MOUSEBUTTONDOWN:  # Si on clique
                # Sur le bouton Play
                if 500 < mouse_pos[0] < 700 and 632 < mouse_pos[1] < 682:
                    # On appelle la fenetre pour initialisé la grille
                    fenetre_initialisation(valeur_1, valeur_2+[loi])
                # Sur le bouton simulation
                if 900 < mouse_pos[0] < 1100 and 632 < mouse_pos[1] < 682:
                    # On appelle la fenetre simulation
                    fenetre_simulation(valeur_1, valeur_2+[loi])
                # Sur le bouton parametre
                if 100 < mouse_pos[0] < 300 and 632 < mouse_pos[1] < 682:
                    # On change la variable affiche_param pour afficher les parametres
                    affiche_param = (affiche_param + 1) % 3
                if (affiche_param == 2):  # On gère les changements de loi lorsqu'on est dans la page 2
                    if (loi == 1):
                        if 50 < mouse_pos[0] < 250 and 400 < mouse_pos[1] < 450:
                            loi = 0
                    else:
                        if 275 < mouse_pos[0] < 475 and 400 < mouse_pos[1] < 450:
                            loi = 1

        # On dessine les boutons
        button_init = pygame.Rect(500, 632, BUTTON_WIDTH, BUTTON_HEIGHT)
        pygame.draw.rect(accueil, GRAY, button_init,
                         border_radius=BUTTON_RADIUS)
        button_simu = pygame.Rect(900, 632, BUTTON_WIDTH, BUTTON_HEIGHT)
        pygame.draw.rect(accueil, GRAY, button_simu,
                         border_radius=BUTTON_RADIUS)
        button_param = pygame.Rect(100, 632, BUTTON_WIDTH, BUTTON_HEIGHT)
        pygame.draw.rect(accueil, GRAY, button_param,
                         border_radius=BUTTON_RADIUS)

        # Vérifie si la souris survol les boutons et on le met en vert dans ce cas

        if button_init.collidepoint(mouse_pos):
            pygame.draw.rect(accueil, GREEN, button_init,
                             border_radius=BUTTON_RADIUS)

        if button_simu.collidepoint(mouse_pos):
            pygame.draw.rect(accueil, GREEN, button_simu,
                             border_radius=BUTTON_RADIUS)

        if button_param.collidepoint(mouse_pos):
            pygame.draw.rect(accueil, GREEN, button_param,
                             border_radius=BUTTON_RADIUS)

        # On affiche le texte au centre du bouton

        text_init = text_bouton_jouer.get_rect(center=button_init.center)
        accueil.blit(text_bouton_jouer, text_init)

        text_simu = text_bouton_simulation.get_rect(center=button_simu.center)
        accueil.blit(text_bouton_simulation, text_simu)

        text_param = text_bouton_parametre.get_rect(center=button_param.center)
        accueil.blit(text_bouton_parametre, text_param)

        # Si on est à la page 1 on affiche uniquement les widget de la page 1 et on actualise
        if (affiche_param == 1):
            for i in range(len(min_max_step_initial_1)):
                slider_list_1[i].show()
                text_box_1[i].show()
            for i in range(len(slider_list_2)):
                slider_list_2[i].hide()
                text_box_2[i].hide()
            fenetre_parametre(accueil)
            pygame_widgets.update(events)
        # Si on est à la page 2 on affiche uniquement les widget de la page 2 et on actualise
        if (affiche_param == 2):
            for i in range(len(min_max_step_initial_1)):
                slider_list_1[i].hide()
                text_box_1[i].hide()
            for i in range(len(slider_list_2)):
                slider_list_2[i].show()
                text_box_2[i].show()
            fenetre_parametre2(accueil)
            pygame_widgets.update(events)
        pygame.display.flip()  # On actualise la fenetre

    pygame.quit()  # On ferme la fenetre
