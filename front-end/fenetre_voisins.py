from tkinter import *
from time import sleep
from random import randint
import pygame
from PIL import Image
# from fenetre_question import *
import sys
sys.path.append("back-end")
from def_class import Animal
from init_grille import initialisation_vide

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


def creation_matrice(nb_voisins):
    """
    Tarik se charge de poser la question "combien de voisins au minimum doivent influer?
    La réponse ici correspond à nb_voisins, il faut ensuite demander à l'utilisateur de remplir un tableau donnant l'influence des voisins et cette fonction donne la taille nécessaire du tableau

    """
    racine = (nb_voisins+1)**0.5
    if racine == int(racine):
        return (racine)
    return (int(racine)+2)


def importance_voisins(nb_min):
    n = int(creation_matrice(int(nb_min)))
    grille = [[0 for i in range(n)] for j in range(n)]
    modele = grille.copy()
    fen_question = pygame.display.set_mode((1200, 700), 0, 24)
    cote = 700/int(nb_min)
    image2 = pygame.image.load("front-end/image/blanc.jpg").convert()
    font = pygame.font.Font(None, 36)
    fen_question.blit(image2, (0, 0))
    for i in range(n):
        for j in range(n):
            grille[i][j] = pygame.Rect(cote*i, cote*j, cote, cote)
            pygame.draw.rect(fen_question, GRAY, grille[i][j], 2)
    rien = True
    running2 = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running2 = Falseinput_active = False
    milieu = (n-1)/2
    running = True
    for i in range(n):
        for j in range(n):
            running2 = True
            if (i, j) != (milieu, milieu):
                input_rect = grille[i][j]
                user_text = ''
                while running2:
                    for k in range(n):
                        for p in range(n):
                            if (k, p) != (i, j) and (k, p) != (milieu, milieu):
                                pygame.draw.rect(fen_question, GRAY,  pygame.Rect(
                                    cote*k, cote*p, cote, cote), 2)
                            elif (k, p) == (milieu, milieu):
                                pygame.draw.rect(fen_question, RED,  pygame.Rect(
                                    cote*k, cote*p, cote, cote), 2)
                            else:
                                pygame.draw.rect(fen_question, BLACK, pygame.Rect(
                                    cote*k, cote*p, cote, cote), 2)
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            running2 = False
                        elif event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_RETURN:
                                running2 = False
                            elif event.key == pygame.K_BACKSPACE:
                                caracteres = list(user_text)
                                caracteresbis = [caracteres[i]
                                                 for i in range(len(caracteres)-1)]
                                user_text = "".join(caracteresbis)
                            else:
                                user_text += event.unicode
                    text_surface = font.render(user_text, True, BLACK)
                    fen_question.blit(text_surface, (cote*i + 5, cote*j + 5))
                    modele[i][j] = user_text
                    pygame.display.flip()
            else:
                modele[i][j] = 0
    return (modele)
