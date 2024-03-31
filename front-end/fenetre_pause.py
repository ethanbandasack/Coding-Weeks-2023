import pygame
from time import sleep
from importlib import import_module

GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
GRAY = (169, 169, 169)


def fenetre_pause(date, grille, valeurs_courbes, valeurs, valeurs2, fenetre, running_s):

    pygame.display.set_caption("Jeu de la survie - Simulation (pause)")
    paused = True
    while paused:

        # récupération de la position de la souris
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                paused = False
                running_s = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = False
                    running_s = False

                elif event.key == pygame.K_SPACE:
                    paused = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 950 <= mouse_pos[0] <= 1150 and 550 <= mouse_pos[1] <= 600:
                    module_init = import_module("fenetre_initialisation")
                    module_init.fenetre_initialisation(
                        valeurs, valeurs2, grille, date, valeurs_courbes)
                elif 950 <= mouse_pos[0] <= 1150 and 620 <= mouse_pos[1] <= 670:
                    paused = False

        # bouton de modification de la grille
        button_change = pygame.Rect(950, 550, 200, 50)
        pygame.draw.rect(fenetre, GRAY, button_change,
                         border_radius=10)
        if button_change.collidepoint(mouse_pos):
            pygame.draw.rect(fenetre, GREEN, button_change,
                             border_radius=10)
        font = pygame.font.SysFont(None, 36)
        text6 = font.render('Modifier grille', True, BLACK)
        text_change = text6.get_rect(center=button_change.center)
        fenetre.blit(text6, text_change)

        # bouton de mise en pause
        button_pause = pygame.Rect(950, 620, 200, 50)
        pygame.draw.rect(fenetre, GRAY, button_pause,
                         border_radius=10)
        if button_pause.collidepoint(mouse_pos):
            pygame.draw.rect(fenetre, GREEN, button_pause,
                             border_radius=10)
        font = pygame.font.SysFont(None, 36)
        text5 = font.render('Pause', True, BLACK)
        text_pause = text5.get_rect(center=button_pause.center)
        fenetre.blit(text5, text_pause)

        pygame.display.flip()  # On actualise la fenetre

    return running_s
