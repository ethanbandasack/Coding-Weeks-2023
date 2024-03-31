# Liste décrivant les tâches à faire et leur répartition.

## Section 1 : Idées et fonctionnalités à mettre en place 

##### MVP
- Avant toute chose, il faut se mettre d'accord sur la représentation des données (pour pouvoir paralléliser les tâches de back-end et de front-end).
- Dans un premier temps, la plupart des paramètres sont décidés à l'avance (e.g. nombre maximal de plantes voisines pour qu'une plante reste en vie) et les probabilités suivent des lois uniformes. L'interface graphique sera minimal afin de pouvoir lancer la simulation.

##### Amélioration incrémentale

- La règle de la surpopulation (et d'autres) pourra être gérée par une probabilité autre (e.g. loi de Poisson).
- L'interface graphique sera améliorée en parallèle, une fois que le MVP sera viable : graphismes moins austères, interface utilisateur pour choisir les pararmètres de la simulation (slider bars), possibilité de cliquer sur la grille directement pour ajouter des plantes (saines ou infectées).
- Affichage du compte des différents états (graphe).

### Partie moutons et loups

S'il reste du temps, nous développerons un modèle proie-prédateur spatialisé : des moutons et des loups se baladeront aléatoirement sur la grille.

##### Première étape

Graphismes minimaux, déplacements des animaux selon une loi uniforme indépendamment des positions des autres entités. Lors d'une collision entre moutons ou entre loups, il y a une probabilité (ici fixe) de générer un nouvel individu (reproduction). Lors de la collision d'un mouton et d'un loup, le loup mange le mouton : le mouton meurt.

##### Amélioration incrémentale

- Lors d'une collision de moutons ou de loups, la probabilité de reproduction dépend du taux de fécondité, qui dépend lui de l'effectif de l'espèce dans la grille.

- Différentiation entre mâles et femelles pour la reproduction animale.

- Mise en place du système complexe : nous allons relier les deux parties du modèle par la mise en place de l'interaction entre les moutons et la végétation.

- En parallèle, amélioration de l'interface graphique de la même manière que pour la première étape (possibilité de mettre la simulation en pause et de modifier la grille, possibilité de choisir les règles de surpopulation en fonction des différents voisins).


## Section 2 : Jalons et répartition des tâches 

Sprint 0 : mise en place du projet

- Jalon 0 : discussion autour du sujet et des besoins
- Jalon 1 : définition du type des différents objets (équipe complète)

Sprint 1 : préparation du MVP

- Jalon 2 : mise en place des classes d'objet (Quentin F) et présentation à l'équipe
- Jalon 3 : implémentation des règles de reproduction et d'infection des plantes (Alexandre)
- Jalon 4 : préparation des fonctionnalités avancées comme les règles de reproduction et de survie des animaux (Auriane et Quentin C)
- Jalon 5 : initialisation de l'interface, choix du paquet utilisé, premiers jets (Ethan et Tarik)

Sprint 2 : MVP

- Jalon 6 : mise en commun vers un MVP viable

Sprint 3 : améliorations

- Jalon 7 : amélioration de l'interface graphique utilisateur (Ethan et Tarik)
- Jalon 8 : implémentation des fonctionnalités avancées vers un produit plus évolué fonctionnel

Sprint 4 : MVP de la seconde partie

- Jalon 9 : implémentation des nouveaux objets, les animaux, et de leurs interactions (Alexandre et Quentin F)
- Jalon 10 : intégration graphique (Ethan, Auriane)
- Jalon 11 : tests du modèle complexe (Quentin F, Alexandre)

Sprint 5 : finalisation du produit

- Jalon 12 : amélioration de l'interface utilisateur (Tarik, Ethan, Quentin C, Auriane)
- Jalon 13 : correction et optimisation du code (équipe entière)


## Section 3 : Updates 

Jour 0 : jalon 0 ok

Jour 1 : jalons 1 à 7 ok

Jour 2 : jalons 8 à 10 ok

Note front : problème de redimensionnement lors du lancement de la simulation (résolu)

Jalon 3 : jalons 11 et 12 ok

Note back : problème dans la reproduction des animaux en présence de plantes (résolu)

Jalon 4 : jalon 13

Note : problème dans l'implémentation de la dernière fonction concernant la prise en compte des voisins, abandon de la fonctionnalité compte tenu du temps restant et du problème de complexité que cela engendrait ; retour des anciennes fonctionnalités en cours