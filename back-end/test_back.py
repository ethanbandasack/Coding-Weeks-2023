from def_class import *
from init_grille import *
from statistiques import *
from generation import *
from animaux import *

cell = Cellule((0, 0), "vide", 0, {}, 0)
cell2 = Cellule((0, 0), "vide", 0, {}, 11)
mouton1 = Animal("mouton", 0, 0, 0)
mouton2 = Animal("mouton", 10, 1, 0)
loup1 = Animal("loup", 7, 0, 2)


def test_classe():
    assert cell.age(10) == 10, "fail test age"
    assert cell.is_immune(10) == False, "fail test immune"
    assert cell2.is_immune(10) == True, "fail test immune"


def test_animaux():
    cell.ajoute_anim(mouton1)
    cell.ajoute_anim(mouton2)
    cell.ajoute_anim(loup1)
    assert cell.nb_mout() == 2, "fail test nb_mout"
    assert cell.nb_loup() == 1, "fail test nb_loup"
    cell.delete_anim(mouton1)
    assert cell.nb_mout() == 1, "fail test delete_anim"


def test_anim2():
    assert loup1.age(10) == 3
    assert mouton1.feed(10) == 10


def test_initialisation_rdm():
    grille = initialisation_rdm((10, 10), 0.2, 0.1)
    assert (np.shape(grille) == (10, 10)
            ), "fail test taille initialisation_rdm"


"""
Les tests pour init_vide sont complétement buggés. 
Le test d'égalité fail tout le temps, je pense que cela est dû à un problème de pointeurs et de valeur en mémoire,
ou alors avec numpy. 

def test_init_vide():
    grille = initialisation_vide((2,2))
    grille_2 = np.array([[Cellule((0,0), "vide", 0, {}, 0), Cellule((0,1), "vide", 0, {}, 0)], [Cellule((1,0), "vide", 0, {}, 0), Cellule((1,1), "vide", 0, {}, 0)]])
    assert(grille == grille_2.all()), "fail test init_seed"
    affiche_grille(grille)

test_init_vide()
"""

grille = [[Cellule((0, 0), "plante", 0, {"mouton": [Animal("mouton", 0, 0, 0)], "loup": [Animal("loup", 0, 0, 0)]}, 10), Cellule((0, 1), "contamine", 0, {}, 0), Cellule((0, 2), "plante", 0, {"mouton": [Animal("mouton", 0, 0, 0)], "loup": [Animal("loup", 0, 0, 0)]}, 0)],
          [Cellule((1, 0), "vide", 0, {}, 0), Cellule(
              (1, 1), "contamine", 0, {}, 0), Cellule((1, 2), "vide", 0, {}, 0)],
          [Cellule((2, 0), "vide", 0, {}, 0), Cellule((2, 1), "plante", 0, {"mouton": [Animal("mouton", 0, 0, 0), Animal("mouton", 0, 0, 0)]}, 10), Cellule((2, 2), "plante", 0, {}, 0)]]


def test_statistiques():
    assert count(grille, 7) == (3, 4, 2, 2, 4, 2), "fail test count"


def test_voisins():
    assert voisins_simples(grille, (1, 1)) == [(
        2, 2), (2, 1), (2, 0), (1, 2), (1, 0), (0, 2), (0, 1), (0, 0)], "fail test voisins"
    assert voisins_simples(grille, (0, 0)) == [(
        1, 1), (1, 0), (0, 1)], "fail test voisins"


def test_surpop():
    assert surpop(grille, (1, 1), 4) == True
    assert surpop(grille, (1, 1), 6) == False


"""
On ne peut pas faire de test sur la majorité des fonctions qui suivent puisqu'elle ne sont pas déterminstes
On pourrait (un peu plus difficilement faire des tests probabilistes en s'accordant une marge d'erreur)

Je vais pour le moment faire des tests basiques avec des probabilités "sûres" (0 ou 1)
"""


def test_reproduction_anim1():
    cell = Cellule((0, 0), "vide", 0, {"mouton": [
                   mouton1, mouton2], "loup": [loup1]}, 0)
    repro_anim(cell, 1, 1, 20)
    assert cell.nb_mout() == 3
    assert cell.nb_loup() == 1


def test_reproduction_anim2():
    cell = Cellule((0, 0), "vide", 0, {"mouton": [mouton1, mouton2], "loup": [
                   loup1, Animal("loup", 7, 1, 2)]}, 0)
    repro_anim(cell, 1, 0, 5)   # test si l'age minimal fonctionne
    assert cell.nb_loup() == 2
    assert cell.nb_mout() == 2
    repro_anim(cell, 1, 0, 20)
    assert cell.nb_loup() == 3
