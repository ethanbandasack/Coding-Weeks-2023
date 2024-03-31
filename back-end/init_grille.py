import numpy as np
from def_class import *
import random as rd

# Nous cherchons ici à définir l'environnement de départ du jeu.


def affiche_grille(grille):
    size = np.shape(grille)
    for i in range(size[0]):
        for j in range(size[1]):
            print(grille[i][j])


# 1er type : Le joueur choisi parmi une multitude de seed configurées auparavant
# On crée donc une seed vide qui sera liée avec le front-end pour que l'utilisateur choisisse sa seed


def initialisation_vide(size):
    """
    param initialisation_vide: ((int*int))
    """
    grille = np.zeros(tuple(size), dtype=Cellule)
    for i in range(size[0]):
        for j in range(size[1]):
            grille[i][j] = Cellule((i, j), "vide", 0, {
                                   "loup": [], "mouton": []}, 0)
    return grille


# 2ème type : Les plantes apparaissent aléatoirement (uniformément pour le moment) sur le plateau

def initialisation_rdm(size, p1, p2):
    """
    param initialisation_rdm: ((int*int), float, float, float, float))
    size(n,m) : taille de la grille
    p1 : probabilités d'être une plante  (0 < p1 < 1)
    p2 : probabilité d'être contaminé    (0 < p2 < 1)
    """
    grille = np.zeros(tuple(size), dtype=Cellule)
    for i in range(size[0]):
        for j in range(size[1]):
            x = rd.uniform(0, 1)
            if x < p1:
                grille[i][j] = Cellule((i, j), "plante", 0, {
                                       "loup": [], "mouton": []}, 0)
            elif p1 < x < p1+p2:
                grille[i][j] = Cellule((i, j), "contamine", 0, {
                                       "loup": [], "mouton": []}, 0)
            else:
                grille[i][j] = Cellule((i, j), "vide", 0, {
                                       "loup": [], "mouton": []}, 0)
    return grille


def random_spawn(grille, ploup, pmout):
    """
    param random_spawn: (Cellule array array, float, float)
    Prends en entrée une grille 
    Sur chaque case, on a une probabilité ploup de faire spawn 1 et 1 seul loup, et une probabilité pmout de faire spawn 1 seul mouton 
    """
    size = np.shape(grille)
    for i in range(size[0]):
        for j in range(size[1]):
            cell = grille[i][j]
            if rd.uniform(0, 1) < ploup:
                cell.ajoute_anim(Animal("loup", 0, rd.randint(0, 1), 0))
            if rd.uniform(0, 1) < pmout:
                cell.ajoute_anim(Animal("mouton", 0, rd.randint(0, 1), 0))


def random_spawn_poisson(grille, param_loup, param_mout):
    """ 
    Même principe qu'auparavant sauf que le nombre d'animaux par case suit une loi de poisson de paramètres param_loup et param_mout
    Cela représente mieux l'évolution d'une population
    """
    size = np.shape(grille)
    for i in range(size[0]):
        for j in range(size[1]):
            cell = grille[i][j]
            for _ in range(np.random.poisson(param_loup)):
                cell.ajoute_anim(Animal("loup", 0, rd.randint(0, 1), 0))
            for _ in range(np.random.poisson(param_mout)):
                cell.ajoute_anim(Animal("mouton", 0, rd.randint(0, 1), 0))

# 3ème type : Le joueur crée sa seed lui-même : Il choisit avec une interface quelles cellules commencent en tant que plante.
