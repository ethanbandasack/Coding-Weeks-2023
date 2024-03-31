# Simulations Types

Ce document a pour objectif de recenser les paramètres des simulations types. 
Ces simulations ont pour but de montrer le fonctionnement des nombreuses règles et outils de notre application.

## Simulation avec des plantes uniquement 

On se place pour le moment dans une grille 10x10 pour toutes les prochaines simulations

#### Reproduction sans champignons ni surpopulation (https://youtu.be/kXpQcrvfNBc) 

- On ne place que des plantes initialement, aucun champignon

- Probabilité de reproduction : 0.5 > 0 

- Mort de surpopulation : 9 => pas de mort par surpopulation 

#### Effet de la surpopulation (https://youtu.be/ib9Fmade2Zw)

- On ne place que des plantes initialement, aucun champignon

- Probabilité de reproduction : 0.5 > 0 

- Mort de surpopulation : 4 => Mort par surpopulation 

#### Effet de contamination (https://youtu.be/07GRIvuv3Tw)

On veut observer un modèle proie-prédateur "stable"

- Placement des plantes avec champignons
- Probabilité tuer : 0.3
- Probabilité d'infection : 0.8
- Probabilité de reproduction 0.35
- Pas d'immunité 
- Mort de surpopulation : 6

On a bien une stabilité. On remarque que les cellules au bord meurent rarement (uniquement par infection car elle ne peuvent pas mourir de surpopulation, pas assez de voisins)

#### Effet de l'immunité (https://youtu.be/6nbiHfFJnlc)

On veut observer les paramètres d'immunités. 

Je conserve les mêmes paramètres, tout en activant l'immunité 

- Jours avant d'immunité : 5 
- Jours d'immunité : 5

On constate que les plantes arrivent à éliminer les champignons

#### Scénario de domination des champignons (https://youtu.be/DNYaljQ7eGw)

Si les plantes mettent trop de temps avant de développer une immunité, elle vont se faire éradiquer 

- Probabilité tuer : 0.3
- Probabilité d'infection : 0.8
- Probabilité de reproduction : 0.5
- Jours avant immunité : 100
- Jours d'immunité : 5
- Pas de mort par surpopulation

#### Scénario de repopulation (https://youtu.be/s1d4Va8ndwY)

Scénario esthétique : les champignons n'arrivent pas à tuer les plantes avant l'immunité : tout se repeuple 

- Probailité de tuer : 0.02 (très faible)

## Simulation avec des animaux uniquement 

#### Explosion de la population de moutons sans prédateur (https://youtu.be/S2sDYEvGgO8)

Pas de prédateurs, les moutons vivent heureux et ont beacoup d'enfants !
Seulement, les ressources en nourritures se font de plus en plus rares et la surpopulation les étouffent, ainsi le nombre de mouton ne peut pas diverger

#### Les loups mangent les moutons affamés (https://youtu.be/q2vRDBqhrS0)

On montre le fonctionnement de la survie des loups qui mangent les moutons.
Les loups meurent juste d'âge à la fin car ils sont trop peu pour se reproduire 

- Age max mouton : 100
- Age max loup : 100
- Nombre avant surpop : 50
- Famine : 75
- Proba déplacement : 0.5
- Proba repro loup : 0.3
- Proba repro mout : 0.3

#### Modèle proie-prédateur (https://youtu.be/IySNyOm4cUY)

On se place dans un cadre sans plantes contaminées, mais on prend des plantes pour pouvoir nourrir les moutons 
Dans cette simulation il est compliqué de prévoir quelle population va rester en vie, puisque les loups peuvent mourir d'âge ou de faim s'il n'y a plus assez de moutons.
Dans la vidéo proposée on constate un certain équilibre, jusqu'à la mort de tous les loups. Les moutons vivent paisiblement mais sont trop peu pour reformer un troupeau.

#### Tous les paramètres sont activés (https://youtu.be/7pwCT4WDW98)

Ici il est vraiment difficile de comprendre ce qu'il se passe, il y a énormément d'intéractions entre les différents objets.





