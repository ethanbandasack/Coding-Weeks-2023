from def_class import *
from init_grille import *
import random as rd
from generation import *
import numpy as np
import matplotlib.pyplot as plt



"""
Fonction usuelle
Renvoie la liste des cases voisines de la case de position pos
"""
def voisins(grille, pos):
    """
    param repro_anim: (array de cellules, float) -> list
    Donne la liste des coordonnées des cellules voisines
    """
    liste_coordonnees = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
    voisins = []
    while len(liste_coordonnees) >= 1:                                                           
        coordonnees_aleatoires = rd.choice(liste_coordonnees)
        x_repro = pos[1] + coordonnees_aleatoires[0]
        y_repro = pos[0] + coordonnees_aleatoires[1] 
        if x_repro >= 0 and y_repro >= 0:                           
            try:
                grille[y_repro][x_repro]
                voisins.append((y_repro,x_repro))                                        
            except:
                pass                 
        liste_coordonnees.remove(coordonnees_aleatoires)
    return voisins



"""
Règles de la survie animale : 
    - les moutons et les loups peuvent vivre pendant un nombre de tours définis au maximum
    - un loup mange tous les moutons de sa case
    - un mouton mange la plante (imunisée ou non) qu'il y a sur sa case
    - les moutons et les loups meurent de faim à partir d'un nombre de tours défini si ils ne mangent pas
    - si il y a trop d'animaux sur une case, ils meurent aléatoirement de surpopulation jusqu'à ce que le nombre d'animaux soit suffisament petit
"""          
            

def score_surpopulation(cell):     # M est la matrice carré des voisins et modele est une matrice de même taille correspondant au modele choisit par l'utilisateur
    """
    param score_population: (Cellule) -> int
    Renvoie le nombre d'animaux sur la cellule
    """
    return cell.nb_mout() + cell.nb_loup()
   

def score_loup_mouton(critere_mouton, cell):     # Du point de vue d'un mouton, cette fonction vérifie si il y a un loup ou non dans la cellule
    if cell.nb_loup() > 0:
        return(critere_mouton)                      # Critere_mouton correspond à la valeur qui amène la mort lors de la comparaison
    return 0                                        # Si il n'y a pas de loup, le score est inchangé

        
def score_final_mouton(age, age_max, s_surpopulation_mouton, s_loup_mouton, critere_mouton, nb_jour_famine, duree):             # Elle détermine si un mouton doit être tué ou non à l'étape suivante
    if s_loup_mouton >= critere_mouton or age >= age_max or s_surpopulation_mouton >= critere_mouton or duree >= nb_jour_famine:   # On regarde si l'une des condition de mort est vérifiée (présence d'un loup, un age trop grand, une surpopulation ou la faim)
        return("mort")
    return("vivant")


def score_mouton_loup(duree, nb_jour_max):  # Du point de vue d'un loup, on regarde si il est mort de faim
    if duree >= nb_jour_max:
        return(nb_jour_max)
    else:
        return 0 

def score_final_loup(age, age_max, s_surpopulation_loup, s_mouton_loup, critere_loup, nb_jour_max):  # Elle détermine si un mouton doit être tué ou non à l'étape suivante
    if  s_mouton_loup >= nb_jour_max or age >= age_max or s_surpopulation_loup >= critere_loup:      # On regarde si l'une des condition de mort est vérifiée (faim, un age trop grand ou une surpopulation)
        return("mort")
    return("vivant")


def loup_mange(cellule, animal, date):        # Elle permet de dire que le loup a mangé
    if cellule.nb_mout() > 0:
        animal.lf = date


def mouton_mange(cellule, animal, date):      # Elle permet de dire que le mouton a mangé
    if cellule.status != "vide":
        animal.lf = date

def is_alive(cellule, animal, age_max_moutons, age_max_loups, nb_surpop, date, nb_jours_famine):  #Fonction qui renvoie True si l'animal survit, False si il meurt
    if animal.type == "mouton":             
        if score_final_mouton(animal.age(date), age_max_moutons, score_surpopulation(cellule), score_loup_mouton(nb_surpop, cellule), nb_surpop, nb_jours_famine, animal.feed(date)) == "mort":
            return False
    if animal.type == "loup":
        if score_final_loup(animal.age(date), age_max_loups, score_surpopulation(cellule), score_mouton_loup(animal.feed(date), nb_jours_famine), nb_surpop, nb_jours_famine) == "mort":
            return False
    return True
        


"""
Règles du déplacement des animaux :
Les moutons et les loups peuvent se déplacer à chaque tour avec une probabilité p_deplac
Si un animal se déplace, il ne peut le faire que sur l'une de ses cases voisines
Il peut y avoir plusieurs animaux par cases donc pas besoin de gérer des conflits de positions
"""
def deplacement(cellule, animal, p_deplac, grille):                     
    if rd.random()<= p_deplac:
        (x_depl, y_depl) = rd.choice(voisins(grille, cellule.pos))  # (x_depl, y_depl) sont les nouvelles coordonnées de l'animal
        return [cellule.pos, (x_depl, y_depl), animal]              # La liste renvoyée contient 3 éléments utilisés plus tard pour effectuer en pratique le déplacement sur la grille: [position_initiale, position_finale, animal concerné]
    return None                                          



"""
Règles de la reproduction animale : 
On considerera que 2 animaux peuvent se reproduire si :
- Ils sont du même  type
- Ils sont sur la même case
- Il y en a un mâle et une femelle
- Leur âge est >= 5
"""

def repro_anim(cell, preploup, prepmouton, date):
    """
    param repro_anim: (Cellule, float, float, int) -> Cellule
    Prend en entrée une cellule et une probabilité de reproduction (0 <= prepanim <= 1)
    Renvoie une cellule, modifiée si il y a eu reproduction, inchangée sinon
    """
    if "mouton" not in cell.anim:
        cell.anim["mouton"] = []
    if "loup" not in cell.anim:
        cell.anim["loup"] = []
    liste_mouton = cell.anim["mouton"]
    liste_loup = cell.anim["loup"] 
    male_mout = False
    femelle_mout = False
    male_loup = False
    femelle_loup = False
    for m in liste_mouton:
        if m.sexe == 0 and m.age(date) >= 5:
            male_mout = True
        if m.sexe == 1 and m.age(date) >= 5:
            femelle_mout = True
    for l in liste_loup:
        if l.sexe == 0 and l.age(date) >= 5:
            male_loup = True
        if l.sexe == 1 and 25 >= l.age(date) >= 5:
            femelle_loup = True
    if male_mout and femelle_mout and rd.uniform(0,1) < prepmouton:
        cell.ajoute_anim(Animal("mouton", date, rd.randint(0,1), date))
    if male_loup and femelle_loup and rd.uniform(0,1) < preploup:
        cell.ajoute_anim(Animal("loup", date, rd.randint(0,1), date))



"""
Fonctionnement de l'update de la grille:
    - on appelle pour chaque case la fonction update_cellule_animaux et on traîte les déplacements effectivement
    - la fonction update_cellule_animaux parcours l'ensemble des animaux d'une cellule et traîte leur survie, leurs déplacements puis leur reproduction
    
"""
def update_cellule_animaux(cellule, age_max_moutons, age_max_loups, nb_surpop, date, nb_jours_famine, grille, p_deplac, preploup, prepmouton):
    b = []                                      # b est la liste qui va contenir les listes de deplacement
    for cles in cellule.anim:
        mort = []                               # On va créer une liste mort qui contiendra l'ensemble des animaux à supprimer (on le fait après pour éviter de modifier la liste qu'on parcourt par la boucle for)
        for animal in cellule.anim[cles]:       
            if animal.type == "mouton":         # On vérifie si les animaux ont mangés ou non
                mouton_mange(cellule, animal, date)
            if animal.type == "loup":
                loup_mange(cellule, animal, date)
            
            est_vivant = is_alive(cellule, animal, age_max_moutons, age_max_loups, nb_surpop, date, nb_jours_famine)
            if est_vivant:                                                  # Si l'animal est_vivant, on lui autorise à se déplacer
                a = deplacement(cellule, animal, p_deplac, grille)          
                b.append(a)                                                 # On ajoute nos sous listes à b. On est obligé de traîter les déplacements en pratique après pour éviter qu'un animal soit déplacé plusieurs fois d'affilé
            else:
                mort.append(animal)                                         # Si l'animal est mort, on l'ajoute à la liste des morts
    
        for i in mort:
            cellule.delete_anim(i)                     # Une fois hors de la boucle, on peut se permettre de supprimer les animaux

            
    repro_anim(cellule, preploup, prepmouton, date)    # Maintenant, on regarde juste sur la case si il y a des reproductions d'animaux
    return b                                           # On renvoie notre liste b pour pouvoir effectuer les déplacements



def update_animaux(grille, date, age_max_moutons, age_max_loups, nb_surpop, nb_jours_famine, p_deplac, preploup, prepmouton):
    liste_deplacements = []                 # On créé une liste qui va contenir chaque liste b de chaque cellule (liste_déplacements contient donc, pour toute la grille, tous les animaux à déplacer, toutes leurs positions de départ ainsi que toutes leurs positions d'arrivée)
    for i in grille:                        # On appelle en boucle la fonction update_cellule_animaux
        for cellule in i:
            b = update_cellule_animaux(cellule, age_max_moutons, age_max_loups, nb_surpop, date, nb_jours_famine, grille, p_deplac, preploup, prepmouton)
            liste_deplacements.append(b)    

    for b in liste_deplacements:            # chaque b contient les déplacements de tous les animaux d'une cellule   
        for a in b:                         # chaque a contient le déplacement d'un animal: [coordonnées de départ, coordonnées d'arrivée, animal en question]
            if a is not None:               # on vérifie qu'il y a bien un déplacement
                grille[a[1][0]][a[1][1]].ajoute_anim(a[2])
                grille[a[0][0]][a[0][1]].delete_anim(a[2])

    date += 1
