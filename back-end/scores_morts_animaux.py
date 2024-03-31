from random import *
from def_class import *


# Dico = {type_animal : [class, ...]...}


# score = critere seulement si un loup est present et le mange et 0 sinon
def score_loup_mouton(critere_mouton, animaux_presents):
    # animaux_presents est considéré comme une liste des animaux présents sur la case
    if "loup" in animaux_presents:
        # on le tue directement car le score critère sera forcément dépassé
        return (critere_mouton)
    return 0


def score_surpopulation(cellule):
    score = 0
    for i in cellule.anim:
        score = score + len(cellule.anim[i])
    return score


# définit la capacité du loup à vivre selon le nombre de jours sans avoir mangé
def score_mouton_loup(duree, nb_jour_max):
    if duree >= nb_jour_max:
        # résultat propotionnel à la durée sans manger (durée) et de valeur critere apres le nomnre de jours max donc le loup meurt
        return (nb_jour_max)


# somme de tous les scores pour le mouton
def score_final_mouton(age, age_max, s_surpopulation_mouton, s_loup_mouton, critere_mouton):
    if s_loup_mouton >= critere_mouton or age > age_max or s_surpopulation_mouton >= critere_mouton:
        return ("mort")
    return ("vivant")


# somme de tous les scores pour le loup
def score_final_loup(age, age_max, s_surpopulation_loup, s_mouton_loup, critere_loup, nb_jour_max):
    if s_mouton_loup > nb_jour_max or age > age_max or s_surpopulation_loup >= critere_loup:
        return ("mort")
    return ("vivant")


def reproduction(espece, animaux, p):
    """

    animaux : dictionnaire regroupant les différentes espèces présentes sur la case en question
    espèces : clés de animaux correspondant aux différentes espèces présentes sur la case
    animaux[espece] : liste de longueur 2 avec pour premier coef le nombre de mâles et second coef le nombre de femelles (ou l'inverse peu importe les 2 fonctionnent)
    p : probabilité qu'un couple se reproduise


    """

    nb_reproductions = 0
    # on prend tous les couples possibles
    for k in range(min(animaux[espece][0], animaux[espece][1])):
        x = random()
        if x < p:
            nb_reproductions += 1
    return (nb_reproductions)   # nombre de reproductions sur la case


def creation_matrice(nb_voisins):
    """
    Tarik se charge de poser la question "combien de voisins au minimum doivent influer?
    La réponse ici correspond à nb_voisins, il faut ensuite demander à l'utilisateur de remplir un tableau donnant l'influence des voisins et cette fonction donne la taille nécessaire du tableau

    """
    racine = (nb_voisins)**0.5
    if racine == int(racine):
        return (racine)
    return (int(racine)+1)
