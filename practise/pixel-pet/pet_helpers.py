"""
pet_helpers.py — helper functions for Pixel Pet 🐣

You don't need to read or understand this file's internals.
Just put it in the same folder as your `pet.py` file and call the
functions like this at the top of your code:

    from pet_helpers import (
        save_exists, load_pet, save_pet, delete_save,
        random_species, show_pet_art,
    )

This file uses some Python features you haven't learned yet
(functions, lists, dictionaries) — that's fine. You're using
them, not writing them.
"""

import os
import random


SAVE_FILE = "pet_save.txt"


# ---------------------------------------------------------------------------
# Save / load helpers
# ---------------------------------------------------------------------------

def save_exists():
    """Return True if there is a saved pet on disk, False otherwise."""
    return os.path.exists(SAVE_FILE)


def load_pet():
    """Read the saved pet and return 8 values in this order:

        name, species, stage, age, hunger, happiness, energy, cleanliness

    Use tuple unpacking on the result:

        name, species, stage, age, hunger, happiness, energy, cleanliness = load_pet()
    """
    with open(SAVE_FILE, "r") as f:
        name = f.readline().strip()
        species = f.readline().strip()
        stage = int(f.readline())
        age = int(f.readline())
        hunger = int(f.readline())
        happiness = int(f.readline())
        energy = int(f.readline())
        cleanliness = int(f.readline())
    return name, species, stage, age, hunger, happiness, energy, cleanliness


def save_pet(name, species, stage, age, hunger, happiness, energy, cleanliness):
    """Write the pet's current state to disk. Pass all 8 values in order."""
    with open(SAVE_FILE, "w") as f:
        f.write(f"{name}\n")
        f.write(f"{species}\n")
        f.write(f"{stage}\n")
        f.write(f"{age}\n")
        f.write(f"{hunger}\n")
        f.write(f"{happiness}\n")
        f.write(f"{energy}\n")
        f.write(f"{cleanliness}\n")


def delete_save():
    """Erase the save file (use this when the pet dies)."""
    if save_exists():
        os.remove(SAVE_FILE)


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
