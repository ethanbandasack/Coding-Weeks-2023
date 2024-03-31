from def_class import *
import numpy as np


def count(grille, date_actuelle):
    """
    param count: (Cellule Array Array, int) -> (int*int*int*int*int*int)
    Renvoie un triplet (vidse, plantes, contamines, immunisees, moutons, loups) qui compte les cases de la grille
    """
    size = np.shape(grille)
    vides = 0
    plantes = 0
    contamines = 0
    immunisees = 0
    moutons = 0
    loups = 0
    for i in range(size[0]):
        for j in range(size[1]):
            cell = grille[i][j]
            if cell.status == "vide":
                vides = vides + 1
            if cell.status == "plante":
                plantes = plantes + 1
            if cell.status == "contamine":
                contamines = contamines + 1
            if cell.is_immune(date_actuelle):
                immunisees = immunisees + 1
            moutons = moutons + cell.nb_mout()
            loups = loups + cell.nb_loup()
    return (vides, plantes, contamines, immunisees, moutons, loups)
