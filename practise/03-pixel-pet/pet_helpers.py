"""
pet_helpers.py — helper functions for Pixel Pet 🐣

You don't need to read or understand this file's internals.
Just put it in the same folder as your `pet.py` file and call the
functions like this at the top of your code:

    from pet_helpers import random_species, show_pet_art

This file uses some Python features you haven't learned yet
(functions, dictionaries) — that's fine. You're using them,
not writing them.

You'll write the save/load logic yourself in `pet.py`, using
what you learned in Lesson 9 (Files).
"""

import random


# ---------------------------------------------------------------------------
# Pet generation
# ---------------------------------------------------------------------------

_SPECIES = ["slime", "dragon", "alien", "robot"]


def random_species():
    """Pick a random species. Returns one of: slime, dragon, alien, robot."""
    return random.choice(_SPECIES)


# ---------------------------------------------------------------------------
# ASCII art
# ---------------------------------------------------------------------------

def show_pet_art(species, stage):
    """Print the ASCII art for the given species and stage (1-4).
    stage 1 = egg, 2 = baby, 3 = teen, 4 = adult.
    """
    key = (species, stage)
    if key in _ART:
        print(_ART[key])
    else:
        print("[ ??? unknown pet ??? ]")


_ART = {
    # ---- Slime --------------------------------------------------
    ("slime", 1): r"""
   _____
  /  .  \
  \_____/    egg""",
    ("slime", 2): r"""
   _____
  ( o o )
  (~~~~~)   baby slime""",
    ("slime", 3): r"""
    _____
   ( o.o )
   (~~~~~)
  (~~~~~~~)  teen slime""",
    ("slime", 4): r"""
     _______
    ( ^_^   )
   (~~~~~~~~~)
  (~~~~~~~~~~~) adult slime""",

    # ---- Dragon -------------------------------------------------
    ("dragon", 1): r"""
   _____
  / X X \
  \_____/    egg""",
    ("dragon", 2): r"""
    /\_/\
   ( o.o )
    > ^ <     baby dragon""",
    ("dragon", 3): r"""
    /\_/\
  _( o.o )_
  / >^.^< \    teen dragon""",
    ("dragon", 4): r"""
       /\_/\
   ___( ^.^ )___
  ///  >^.^<  \\\
   ~/_/  \_\~     adult dragon""",

    # ---- Alien --------------------------------------------------
    ("alien", 1): r"""
   _____
  / *.* \
  \_____/    egg""",
    ("alien", 2): r"""
    . .
   ( o )
   (___)      baby alien""",
    ("alien", 3): r"""
    . .
   (o o)
    \-/
   (___)      teen alien""",
    ("alien", 4): r"""
     | |
    (o o)
    /\-/\
   (_____)
    | | |     adult alien""",

    # ---- Robot --------------------------------------------------
    ("robot", 1): r"""
   +-----+
   |  ?  |
   +-----+    egg""",
    ("robot", 2): r"""
    [o o]
    [---]     baby robot""",
    ("robot", 3): r"""
      |
    [o o]
    [---]
    /| |\     teen robot""",
    ("robot", 4): r"""
       |
     [o-o]
     [|||]
    /  |  \
    |__|__|   adult robot""",
}
