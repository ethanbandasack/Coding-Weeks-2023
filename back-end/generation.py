import random as rd
import numpy as np
from init_grille import *


def voisins(grille, pos, n):
    """
    param voisins: (Cellule array array, (int*int), int)
    Renvoie la liste des plantes voisines de la case pos
    """
    liste_coordonnees = [(i, j) for i in range(-n, n+1)
                         for j in range(-n, n+1)]
    voisins = []
    while len(liste_coordonnees) >= 1:
        coordonnees_aleatoires = rd.choice(liste_coordonnees)
        x_repro = pos[0] + coordonnees_aleatoires[0]
        y_repro = pos[1] + coordonnees_aleatoires[1]
        if x_repro >= 0 and y_repro >= 0:
            try:
                grille[x_repro][y_repro]
                voisins.append((y_repro, x_repro))
            except:
                pass
        liste_coordonnees.remove(coordonnees_aleatoires)
    return voisins


def voisins_simples(grille, pos):
    """
    param voisins: (Cellule array array, (int*int))
    Renvoie la liste des plantes voisines de la case pos
    """
    liste_coordonnees = [(-1, -1), (-1, 0), (-1, 1),
                         (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    voisins = []
    while len(liste_coordonnees) >= 1:
        coordonnees_aleatoires = rd.choice(liste_coordonnees)
        x_repro = pos[0] + coordonnees_aleatoires[0]
        y_repro = pos[1] + coordonnees_aleatoires[1]
        if x_repro >= 0 and y_repro >= 0:
            try:
                grille[x_repro][y_repro]
                voisins.append((x_repro, y_repro))
            except:
                pass
        liste_coordonnees.remove(coordonnees_aleatoires)
    return voisins


def surpop(grille, pos, k2=4):
    """
    param surpop: (Cellule array array, (int*int), int)
    Renvoie Vrai si la plante à la position pos doit mourir de surpopulation, faux sinon
    Cette fonction est à appliquer uniquement aux plantes !
    paramètre k : nombres de plantes qui engendrent la suffocation
    """
    c = 0
    for v in voisins_simples(grille, pos):
        (x, y) = v
        if grille[x][y].status != "vide":
            c = c + 1
    if c >= k2:
        return True
    return False


def repro(grille, pos, prepro):
    """
    param repro: (Cellule array array, (int*int), float)
    prepro : float compris entre 0 et 1, probabilité de reproduction d'une plante
    Renvoie une case de la grille qui doit se transformer en plante
    ATTENTION : Pour le moment on ne met pas de condition sur la case qui doit être remplacée
    Un plante peut donc naître sur une plante déjà existence ou une plante contaminée  
    """
    if rd.uniform(0, 1) < prepro:
        v = voisins_simples(grille, pos)
        return rd.choice(v)
    else:
        return None, None


def contamination(grille, pos, pinfect):
    for v in voisins_simples(grille, pos):
        (x, y) = v
        if grille[x][y].status == "contamine" and rd.uniform(0, 1) < pinfect:
            return True
    return False

# les plantes infectées finissent par s'imuniser contre le champignon


def immunite(cellule, date, k=3):
    if cellule.age(date) == k:
        return True
    else:
        return False


def plante_mangee(cellule):
    if "mouton" not in cellule.anim:
        cellule.anim["mouton"] = []
    if len(cellule.anim["mouton"]) > 0:
        return True


def update_grille(grille, prepro, pinfect, ptuer, date, k1=4, Nimmun=3, k2=4):
    """
    param update_grille: (Cellule array array, float, float, float, int, int, int)
    Renvoie la grille à l'étape date+1 en prenant en compte : la reproduction, la surpopulation, la contamination, la mort par contamination, l'immunité
    prepro : probabilité de reproduction (floattant entre 0 et 1)
    pinfect : proba d'infection
    ptuer : proba de MORT par infection
    date : entier représentant à quel tour du jeu on se trouve
    k1 : nbr de tours avant immunité
    Nimmun : jours d'immunités
    k2 : nombre de plantes voisines avant surpopulation (0 < k < 9)
    """
    size = np.shape(grille)
    nouvelle_grille = np.copy(grille)
    for i in range(size[0]):
        for j in range(size[1]):
            cell = grille[i][j]
            if cell.status == "plante":
                # Reproduction
                (x, y) = repro(grille, (i, j), prepro)
                if (x, y) != (None, None):
                    nouvelle_grille[x][y] = Cellule(
                        (x, y), "plante", date, grille[x][y].anim, cell.immune)
                # Contamination
                if not cell.is_immune(date) and contamination(grille, (i, j), pinfect):
                    nouvelle_grille[i][j] = Cellule(
                        (i, j), "contamine", date, cell.anim, 0)

            if cell.status == "contamine":
                # Plantes contaminées qui se font TUER
                if rd.uniform(0, 1) < ptuer:
                    nouvelle_grille[i][j] = Cellule(
                        (i, j), "vide", date, cell.anim, 0)

                # Immunité si elles se font pas tuer
                if cell.age(date) >= k1:
                    nouvelle_grille[i][j] = Cellule(
                        (i, j), "plante", date, cell.anim, date + Nimmun)
            if cell.status != "vide":
                # Mort à cause de surpopulation
                if surpop(grille, (i, j), k2):
                    nouvelle_grille[i][j] = Cellule(
                        (i, j), "vide", date, cell.anim, 0)
                if plante_mangee(cell):
                    nouvelle_grille[i][j] = Cellule(
                        (i, j), "vide", date, cell.anim, 0)
    return nouvelle_grille
