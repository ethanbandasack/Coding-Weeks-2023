# Simulation Types

This document aims to list the parameters of typical simulations. These simulations are intended to demonstrate the functioning of the numerous rules and tools of our application.

## Simulation with Plants Only

For the moment, we are using a 10x10 grid for all the following simulations.

### Reproduction without Mushrooms or Overpopulation (https://youtu.be/kXpQcrvfNBc)

- Only plants are placed initially, no mushrooms.
- Reproduction probability: 0.5 > 0.
- Overpopulation death: 9 => no death by overpopulation.

### Effect of Overpopulation (https://youtu.be/ib9Fmade2Zw)

- Only plants are placed initially, no mushrooms.
- Reproduction probability: 0.5 > 0.
- Overpopulation death: 4 => death by overpopulation.

### Effect of Contamination (https://youtu.be/07GRIvuv3Tw)

We want to observe a "stable" predator-prey model.

- Plants placed with mushrooms.
- Kill probability: 0.3.
- Infection probability: 0.8.
- Reproduction probability: 0.35.
- No immunity.
- Overpopulation death: 6.

We observe stability. We notice that the cells at the edges rarely die (only by infection because they cannot die from overpopulation, not enough neighbors).

### Effect of Immunity (https://youtu.be/6nbiHfFJnlc)

We want to observe the immunity parameters.

I keep the same parameters while activating immunity.

- Days before immunity: 5.
- Days of immunity: 5.

We observe that the plants manage to eliminate the mushrooms.

### Scenario of Mushroom Domination (https://youtu.be/DNYaljQ7eGw)

If the plants take too long to develop immunity, they will be eradicated.

- Kill probability: 0.3.
- Infection probability: 0.8.
- Reproduction probability: 0.5.
- Days before immunity: 100.
- Days of immunity: 5.
- No death by overpopulation.

### Scenario of Repopulation (https://youtu.be/s1d4Va8ndwY)

Aesthetic scenario: the mushrooms cannot kill the plants before immunity: everything repopulates.

- Kill probability: 0.02 (very low).

## Simulation with Animals Only

### Explosion of the Sheep Population without Predators (https://youtu.be/S2sDYEvGgO8)

No predators, the sheep live happily and have many offspring! However, food resources become increasingly scarce, and overpopulation suffocates them, so the number of sheep cannot diverge.

### Wolves Eat Starving Sheep (https://youtu.be/q2vRDBqhrS0)

We show the functioning of wolf survival by eating sheep. The wolves die only of old age in the end because there are too few to reproduce.

- Maximum age of sheep: 100.
- Maximum age of wolves: 100.
- Number before overpopulation: 50.
- Famine: 75.
- Movement probability: 0.5.
- Wolf reproduction probability: 0.3.
- Sheep reproduction probability: 0.3.

### Predator-Prey Model (https://youtu.be/IySNyOm4cUY)

We consider a scenario without contaminated plants but with plants to feed the sheep. In this simulation, it is difficult to predict which population will survive, as wolves can die of old age or starvation if there are not enough sheep. In the proposed video, we observe a certain balance until the death of all the wolves. The sheep live peacefully but are too few to reform a herd.

### All Parameters Activated (https://youtu.be/7pwCT4WDW98)

Here, it is really difficult to understand what is happening, as there are many interactions between the different objects.
