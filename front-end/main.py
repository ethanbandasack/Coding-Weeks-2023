from fenetre_accueil import fenetre_accueil

if __name__ == "__main__":
    fenetre_accueil()

"""La fenêtre affichée est la fenêtre d'accueil.


Un clic sur le bouton "Parametres" permet d'ouvrir
un menu avec les paramètres concernant les plantes (sliders).

Un deuxième clic sur le bouton permet d'accéder aux paramètres
concernant les animaux (sliders et boutons).



Un clic sur le bouton "Simulation" permet d'accéder,
dans une nouvelle fenêtre "Simulation",
à une grille générée aléatoirement selon les paramètres définis à l'accueil.

Voir deux paragraphes plus bas pour plus d'informations sur la fenêtre "Simulation".



Un clic sur le bouton "Jouer" permet d'accéder à une grille vierge
(dimensions choisies dans les paramètres) dans une nouvelle fenêtre "Initialisation".

Une légende est disponible à droite de l'écran pour placer et retirer
plantes et animaux sur la grille. Le clic gauche est utilisé pour placer
les entités ou d'immuniser une plante (le nombre de tours est réinitialisé si la plante
est déjà immunisée), tandis que le clic droit permet de retirer une entité ou
de retirer une immunité sur une plante immunisée.

La molette de la souris permet de changer d'entité sélectionnée parmi :
plante saine non immunisée, plante infectée, plante immunisée, mouton, loup.

Redimensionner la grille est possible
avec les flèches directionnelles : les flèches verticales modifient la hauteur
de la grille tandis que les flèches horizontales modifient sa largeur.
La grille n'est pas réinitialisée à chaque redimensionnement.



La touche espace permet, une fois la grille choisie dans "Jouer",
de lancer une nouvelle fenêtre "Simulation" qui fera évoluer la grille
selon les règles spécifiée dans les paramètres.

Initialement, les générations se succèdent rapidement selon le framerate défini
au tout début du fichier front-end/fenetre_simulation.py.

- L'appui sur la touche S permet d'afficher les courbes indiquant les proportions
des différentes entités sur la grille.
Attention : matplotlib étant lent, la fréquence d'image sera beaucoup plus basse
Réappuyer sur la touche S retire l'affichage des courbes, rendant l'animation rapide à nouveau.

- L'appui sur la touche C ou un clic sur le bouton "Grille" permet de n'afficher
que les deux courbes en grand, sans afficher la grille.
Appuyer à nouveau sur C ou cliquer sur le bouton "Grille" permet de revenir
au tableau de bord avec la grille et les courbes en petit.

- Un clic sur le bouton pause ou un appui sur la barre espace met la génération en pause.
Un nouvel appui ou un nouveau clic relancera la simulation dans l'état où elle s'est arrêtée.
En revanche, le clic sur le bouton "Modifier grille" permet d'accéder à nouveau
à la fenêtre "Initialisation" et de modifier la grille dans l'état où elle s'est arrêtée.

Voir 4 paragraphes plus haut pour plus d'informations sur la fenêtre "Initialisation".

- L'appui sur la touche A permet de relancer une simulation aléatoire
depuis le début selon les paramètres définis à l'accueil."""
