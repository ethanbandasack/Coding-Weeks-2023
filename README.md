# Projet semaine 2 du groupe 12 : Coding Weeks jeu de la vie

## Description :

L'objet de ce projet est le développement d'une application de type "automate cellulaire" avec python.
Nous souhaitons que l'utilisateur puisse paramétrer sa simulation le plus librement possible.
Notre application est fournie avec une interface graphique épurée et accessible.

## Jeu, utilisation et interface graphique 

Notre application permet au joueur d'effectuer des simulations d'un écosystème tout en jouant sur les variables et paramètres de départ. 

Il peut choisir une grille de départ aléatoire en spécifiant la probabilité d'apparition des plantes, des champignons. Il peut même faire en sorte que le nombre d'animaux apparaisant suive une loi de poisson pour se rapprocher de la réalité.

L'utilisateur peut aussi configurer lui même sa grille ! Il choisit une taille, le placement et le nombre des plantes, champignons, animaux. Nous avons réussi l'un de nos objectifs : l'application permet une flexibilité au niveau du paramétrage, tout en restant intelligible.

Voici les paramètres sur lesquel l'utilisateur peut influer : 

- La taille de la grille de jeu (longueur et largeur)
- Probabilité d'apparation de la plante (Loi uniforme : pour chaque case, la probabilité d'appartion d'une plante est pplante)
- Probabilité d'apparation d'une plante contaminée par un champignon
- Probabilité qu'une plante infectée se fasse tuer
- Probabilité d'apparition des animaux (loi uniforme ou de poisson)
- Probabilité de reproduction (1 paramètre par animal, loup et mouton), loi uniforme et il faut que les conditions soient remplies
- Jours avant qu'une plante contaminée devienne immunisée (si elle ne meurt pas)
- Durée de l'immunité
- Nombre de plantes voisines avant la mort par surpopulation 
- Le nombre de FPS (frame par secondes = nombre d'actualisation de la grille par seconde)

Une fois la simulation lancée, l'utilisateur peut voir la grille évoluer. 
Il peut aussi suivre l'évolution des populations à l'aide de graphes qui s'actualisent en temps réel. 
Enfin, il peut quitter la simulation en appuyant sur la touche ECHAP.

#### Utilisation pratique

**Modules à installer au préalable :**
- numpy
- matplotlib
- random
- pygame
- pygame_widgets
- time (native)
- tkinter
- PIL (Pillow)
- importlib
- screeninfo

Lancer le fichier front-end/main.py.

La fenêtre affichée est la fenêtre d'accueil.

Un clic sur le bouton "Parametres" permet d'ouvrir un menu avec les paramètres concernant les plantes (sliders). Un deuxième clic sur le bouton permet d'accéder aux paramètres concernant les animaux (sliders et boutons).

Un clic sur le bouton "Simulation" permet d'accéder, dans une nouvelle fenêtre "Simulation", à une grille générée aléatoirement selon les paramètres définis à l'accueil. Voir deux paragraphes plus bas pour plus d'informations sur la fenêtre "Simulation".

Un clic sur le bouton "Jouer" permet d'accéder à une grille vierge (dimensions choisies dans les paramètres) dans une nouvelle fenêtre "Initialisation". UUne légende est disponible à droite de l'écran pour placer et retirer plantes et animaux sur la grille :
- Le clic gauche est utilisé pour placer les entités ou d'immuniser une plante (le nombre de tours est réinitialisé si la plante est déjà immunisée), tandis que le clic droit permet de retirer une entité ou de retirer une immunité sur une plante immunisée.
- La molette de la souris permet de changer d'entité sélectionnée parmi :
plante saine non immunisée, plante infectée, plante immunisée, mouton, loup.

Redimensionner la grille est possible avec les flèches directionnelles : les flèches verticales modifient la hauteur de la grille tandis que les flèches horizontales modifient sa largeur. La grille n'est pas réinitialisée à chaque redimensionnement.

La touche espace permet, une fois la grille choisie dans "Jouer", de lancer une nouvelle fenêtre "Simulation" qui fera évoluer la grille selon les règles spécifiée dans les paramètres. Initialement, les générations se succèdent rapidement selon le framerate défini au tout début du fichier front-end/fenetre_simulation.py.
- L'appui sur la touche S permet d'afficher les courbes indiquant les proportions des différentes entités sur la grille. Attention : matplotlib étant lent, la fréquence d'image sera beaucoup plus basse. Réappuyer sur la touche S retire l'affichage des courbes, rendant l'animation rapide à nouveau.
- L'appui sur la touche C ou un clic sur le bouton "Grille" permet de n'afficher que les deux courbes en grand, sans afficher la grille. Appuyer à nouveau sur C ou cliquer sur le bouton "Grille" permet de revenir au tableau de bord avec la grille et les courbes en petit.
- Un clic sur le bouton pause ou un appui sur la barre espace met la génération en pause. Un nouvel appui ou un nouveau clic relancera la simulation dans l'état où elle s'est arrêtée. En revanche, le clic sur le bouton "Modifier grille" permet d'accéder à nouveau à la fenêtre "Initialisation" et de modifier la grille dans l'état où elle s'est arrêtée. Voir 4 paragraphes plus haut pour plus d'informations sur la fenêtre "Initialisation".
- L'appui sur la touche A permet de relancer une simulation aléatoire depuis le début selon les paramètres définis à l'accueil.

## Membres du projet : 

**Membre A** : Quentin Fretault

**Membre B** : Ethan Bandasack 

**Membre C** : Alexandre Dieumegard 

**Membre D** : Auriane Delacroix

**Membre E** : Tarik Ouadjou 

**Membre F** : Quentin Courqueux

## Notre projet en détail : 

Notre automate représente un écosystème régi par les interactions biologiques entre les êtres vivants

Nous nous trouvons dans une prairie où se développent des plantes : elles subissent une attaque de mycéliums et sont mangées par des moutons qui eux-mêmes sont mangés par des loups, représentant ainsi de nombreuses interactions proie-prédateur. 

Nous avons une reproduction végétative des plantes : à chaque tour une probabilité p de reproduction sur une case adjacente aléatoire (la plante fille hérite des caractéristiques de la plante mère)
Si une plante possède plus de 4 plantes à son voisinage (1 case) elle meurt car il n'y a plus assez de ressources disponibles dans le sol

- A l'état initial, certaines plantes sont infectées par un champignon.

- Transport des spores par le vent : à chaque tour, pour chaque plante située dans la portée d'une plante infectée, on a une probabilité $p_{infect}$ d'être infectée à son tour (la portée est de 1 case).

- Si une plante saine est dans la portée de plusieurs plantes infectées, alors elle "cumule" les probabilités d'être contaminée.

- Contamination : durant un tour, la plante reçoit l'information de l'infection (stimulus) car le champignon diffuse des molécules lorsqu'il se développe. La plante reçoit l'information et développe alors un antidote : du point de vue de l'automate, rien ne se passe.
Ensuite, lors de chaque tour qui suit, le champignon a une probabilité $p_{tuer}$ de tuer la plante. 

- Résistance à court terme : si au bout de 2 tours la plante est toujours vivante, son antidote est prêt et le champignon meurt.
La plante reste donc infectée au maximum 3 tours.

- Résistance à long terme : la plante guérie est maintenant immunisée contre l'infection pendant $n_{immu}$ tours. 

### Seconde partie du projet : partie moutons et loups

- On ajoute à l'état initial un certain nombre de moutons et de loups disposé selon les seeds
- Les moutons et les loups peuvent se déplacer librement sur la grille, indépendamment de l'état des cellules
- A chaque tour les moutons et les loups ont une probabilité de mourir selon leur taux de mortalité
- Le taux de mortalité augmente avec l'âge des moutons et des loups, mais aussi du nombre d'individus à proximité
- Quand 2 moutons ou 2 loups sont côte à côte ils se reproduisent un nouvel individu apparait sur une des cases libres adjacentes
- A chaque tour les moutons et les loups se déplacent d'une case aléatoirement
- Un mouton peut aller sur une case plante et donc il la mange un loup peut aller sur une case mouton et le manger également
- Si au bout de $n_{mort,m}$ tours le mouton n'a pas mangé de plante, il meurt de faim
- Si au bout de $n_{mort,l}$ tours le loup n'a pas mangé de mouton, il meurt (avec $n_{mort,l}>n_{mort,m}$)
- Reproduction : si on a assez de temps, on pourra différencier moutons mâle et femelle ainsi que loups mâle et femelle

## Vocabulaire commun

- Grille : espace discrétisé représentant la prairie numériquement

- Cellule : équivalent de cellule dans le jeu de la vie de Conway, classe d'objet qui peut avoir comme état "vide", "plante" ou "contamine".

- Plante saine : lorsqu'elle n'est pas infectée par un champignon.

- Plante infectée : lorsqu'elle est infectée par un champignon.

- Plante immunisée : lorsqu'elle se débarrasse de champignon, redevient saine au bout d'un certain nombre de tours.

- Animaux : classe d'objet pouvant se déplacer sur la grille, possède un âge, un sexe et un nombre de tours depuis le dernier repas ; peut être pour l'instant un loup ou un mouton.

## Project status / Feuille de route 

Développement du MVP (Minimal Viable Product) : interface graphique minimale, peu de paramètres mais simulation fonctionnelle. OK

Mise en place des différentes fenêtres (accueil, simulation, initialisation manuelle). OK

Test du modèle simple (plantes uniquement) avec divers paramètres. OK

Développement du début de la seconde partie. OK

Implémentation des paramètres relatifs aux animaux. OK

Test du modèle complet avec divers paramètres. OK

Mise en place de l'interface utilisateur complète. OK

Implémentation de courbes. OK

Tentative de faire varier l'influence des voisins dans la surpopulation