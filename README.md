# Week 2 Project by Group 12: Coding Weeks Game of Life

## Description:

The objective of this project is to develop a "cellular automaton" type application using Python. We aim for the user to be able to parameterize their simulation as freely as possible. Our application comes with a clean and accessible graphical interface.

## Game, Usage, and Graphical Interface

Our application allows the player to perform simulations of an ecosystem while adjusting initial variables and parameters.

The user can choose a random starting grid by specifying the probability of plant and mushroom appearance. They can even make the number of animals appearing follow a Poisson distribution to better reflect reality.

The user can also configure their own grid! They choose the size, placement, and number of plants, mushrooms, and animals. We have achieved one of our goals: the application allows flexibility in parameterization while remaining intelligible.

Here are the parameters the user can influence:

- Grid size (length and width)
- Probability of plant appearance (Uniform distribution: for each cell, the probability of a plant appearing is p_plant)
- Probability of a plant being contaminated by a mushroom
- Probability that an infected plant will be killed
- Probability of animal appearance (uniform or Poisson distribution)
- Reproduction probability (1 parameter per animal, wolf and sheep), uniform distribution, and conditions must be met
- Days before a contaminated plant becomes immune (if it doesn't die)
- Duration of immunity
- Number of neighboring plants before death by overpopulation
- FPS (frames per second = number of grid updates per second)

Once the simulation is launched, the user can see the grid evolve. They can also track population changes using real-time updating graphs. Finally, they can exit the simulation by pressing the ESC key.

### Practical Usage

**Modules to install beforehand:**
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

Run the file `front-end/main.py`.

The displayed window is the welcome window.

Clicking the "Parameters" button opens a menu with plant-related parameters (sliders). A second click on the button accesses animal-related parameters (sliders and buttons).

Clicking the "Simulation" button opens a new "Simulation" window with a randomly generated grid based on the parameters set in the welcome window. See two paragraphs below for more information on the "Simulation" window.

Clicking the "Play" button opens a blank grid (dimensions chosen in the parameters) in a new "Initialization" window. A legend is available on the right side of the screen to place and remove plants and animals on the grid:
- The left click is used to place entities or immunize a plant (the number of turns is reset if the plant is already immunized), while the right click removes an entity or removes immunity from an immunized plant.
- The mouse wheel changes the selected entity among: healthy non-immunized plant, infected plant, immunized plant, sheep, wolf.

Resizing the grid is possible with the arrow keys: vertical arrows modify the grid height, while horizontal arrows modify its width. The grid is not reset with each resizing.

The space bar, once the grid is chosen in "Play," launches a new "Simulation" window that evolves the grid according to the rules specified in the parameters. Initially, generations succeed rapidly according to the framerate defined at the beginning of the `front-end/fenetre_simulation.py` file.
- Pressing the S key displays curves indicating the proportions of different entities on the grid. Note: Since matplotlib is slow, the frame rate will be much lower. Pressing the S key again removes the curve display, making the animation fast again.
- Pressing the C key or clicking the "Grid" button displays only the two large curves without showing the grid. Pressing C again or clicking the "Grid" button returns to the dashboard with the grid and small curves.
- Clicking the pause button or pressing the space bar pauses the generation. A new press or click will resume the simulation in the state where it stopped. However, clicking the "Modify Grid" button reopens the "Initialization" window to modify the grid in the state where it stopped. See four paragraphs above for more information on the "Initialization" window.
- Pressing the A key restarts a random simulation from the beginning according to the parameters set in the welcome window.

## Project Members:

**Member A:** Quentin Fretault

**Member B:** Ethan Bandasack

**Member C:** Alexandre Dieumegard

**Member D:** Auriane Delacroix

**Member E:** Tarik Ouadjou

**Member F:** Quentin Courqueux

## Our Project in Detail:

Our automaton represents an ecosystem governed by biological interactions between living beings.

We are in a meadow where plants develop: they are attacked by mycelium and eaten by sheep, which in turn are eaten by wolves, thus representing numerous predator-prey interactions.

We have vegetative reproduction of plants: each turn, there is a probability p of reproduction on a random adjacent cell (the daughter plant inherits the characteristics of the mother plant). If a plant has more than 4 neighboring plants (1 cell away), it dies because there are not enough resources available in the soil.

- Initially, some plants are infected by a mushroom.

- Spore transport by wind: each turn, for each plant within the range of an infected plant, there is a probability $p_{infect}$ of being infected in turn (the range is 1 cell).

- If a healthy plant is within the range of multiple infected plants, it "accumulates" the probabilities of being contaminated.

- Contamination: during a turn, the plant receives the infection information (stimulus) because the mushroom diffuses molecules as it develops. The plant receives the information and then develops an antidote: from the automaton's perspective, nothing happens. Then, in each subsequent turn, the mushroom has a probability $p_{tuer}$ of killing the plant.

- Short-term resistance: if after 2 turns the plant is still alive, its antidote is ready, and the mushroom dies. Therefore, the plant remains infected for a maximum of 3 turns.

- Long-term resistance: the cured plant is now immune to infection for $n_{immu}$ turns.

### Second Part of the Project: Sheep and Wolves

- Initially, a certain number of sheep and wolves are added, arranged according to the seeds.
- Sheep and wolves can move freely on the grid, independently of the cell states.
- Each turn, sheep and wolves have a probability of dying according to their mortality rate.
- The mortality rate increases with the age of the sheep and wolves, as well as the number of nearby individuals.
- When 2 sheep or 2 wolves are side by side, they reproduce, and a new individual appears on one of the adjacent free cells.
- Each turn, sheep and wolves move randomly by one cell.
- A sheep can move to a plant cell and eat it; a wolf can move to a sheep cell and eat it.
- If after $n_{mort,m}$ turns the sheep has not eaten a plant, it dies of starvation.
- If after $n_{mort,l}$ turns the wolf has not eaten a sheep, it dies (with $n_{mort,l} > n_{mort,m}$).
- Reproduction: if we have enough time, we will differentiate between male and female sheep and wolves.

## Common Vocabulary

- **Grid:** discretized space representing the meadow numerically.

- **Cell:** equivalent to a cell in Conway's Game of Life, an object class that can have states "empty," "plant," or "contaminated."

- **Healthy Plant:** when not infected by a mushroom.

- **Infected Plant:** when infected by a mushroom.

- **Immunized Plant:** when it gets rid of the mushroom, becomes healthy again after a certain number of turns.

- **Animals:** object class that can move on the grid, has an age, gender, and number of turns since the last meal; can currently be a wolf or a sheep.

## Project Status / Roadmap

- Development of the MVP (Minimal Viable Product): minimal graphical interface, few parameters but functional simulation. **OK**

- Setting up different windows (welcome, simulation, manual initialization). **OK**

- Testing the simple model (plants only) with various parameters. **OK**

- Development of the beginning of the second part. **OK**

- Implementation of animal-related parameters. **OK**

- Testing the complete model with various parameters. **OK**

- Setting up the complete user interface. **OK**

- Implementation of curves. **OK**
