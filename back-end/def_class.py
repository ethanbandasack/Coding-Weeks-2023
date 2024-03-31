class Cellule(object):
    """"
    param Cellule: ((int*int), string, int, dict (string, Animal list)) case de la grille
    pos : position (x,y) de la cellule dans la grille
    status : type de la cellule (vide, plante ou contamine)
    lu : dernière date à laquelle la cellule a été modifiée
    anim : dictionnaire, les clés sont des string (nom de l'animal) et les valeurs sont une liste de l'objet Animal
    immune : entier représentant la date jusqu'à laquelle la cellule est imunisée.
    """

    def __init__(self, pos, status, lu, anim, immune):
        self.pos = pos
        self.status = status
        self.lu = lu
        self.anim = anim
        self.immune = immune

    """
    param age: (Cellule, int) renvoie l'age de l'objet de la cellule = nombre de tours depuis dernier changement
    Si le nom de la cellule est cell : cell.age(date_actuelle) 
    Utiliser print(nom_cellule) pour afficher les infos de la cellule
    """

    def age(self, date_actuelle):
        return date_actuelle-self.lu

    """
    cell.is_immune(date_actuelle) renvoie Vrai si la cellule est une plante immunisée, Faux sinon
    """

    def is_immune(self, date_actuelle):
        if self.immune > date_actuelle:
            return True
        else:
            return False

    def __str__(self):
        return str("(Position : {}, Cellule : {}, Date changement : {}, Animaux présents : {}, Immunité jusqu'au jour: {})".format(self.pos, self.status, self.lu, self.anim, self.immune))

    def ajoute_anim(self, new_anim):
        s = new_anim.type
        dico = self.anim
        if s in dico:
            dico[s].append(new_anim)
        else:
            dico[s] = [new_anim]

    def delete_anim(self, anim):
        s = anim.type
        dico = self.anim
        l = dico[s]
        if anim in l:

            l.remove(anim)
        else:
            return

    def nb_mout(self):
        if "mouton" in self.anim:
            d = self.anim
            return len(d["mouton"])
        return 0

    def nb_loup(self):
        if "loup" in self.anim:
            d = self.anim
            return len(d["loup"])
        return 0


class Animal(object):
    """
    param Animal: (string, int, int, int)
    type : string indiquant le type d'animal ex: "loup", "mouton"
    dn : int donnant la date de naissance de l'animal
    sexe : int 0 pour mâle, 1 pour femelle 
    lf (last feeding) : int indiquant la derniere date à laquelle l'animal a mangé
    """

    def __init__(self, type, dn, sexe, lf):
        self.type = type
        self.dn = dn
        self.sexe = sexe
        self.lf = lf

    def feed(self, date_actuelle):
        """
        Prend en entrée la date actuelle et renvoie le nombre de tours depuis lequel l'animal n'a pas mangé
        """
        return date_actuelle - self.lf

    def __str__(self):
        return str("(Type : {}, Age : {}, Sexe : {}, Last Feeding : {})".format(self.type, self.age, self.sexe, self.lf))

    def age(self, date_actuelle):
        return date_actuelle - self.dn