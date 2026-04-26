# 🐣 Pixel Pet — Practice Project 💾

> **Build a virtual pet you keep alive across days. The pet is saved to a file, so it remembers you between runs — just like a real Tamagotchi.**

---

## The Story

You've adopted a tiny digital creature. It's hatched from a mysterious egg, and it depends on you to feed it, play with it, clean it, and let it sleep. If you take great care of it, it will **evolve through 4 stages** — egg → baby → teen → adult.

If you neglect it... well, you don't want to find out.

Each time you start the program, **another day passes** in your pet's life. Stats decay overnight. Visit your pet often!

---

## How This Project Works

This is a **practice** project — there are no step-by-step "Part 1, Part 2" walkthroughs. Each milestone gives you a **mission spec**: requirements, rules, sample sessions, and acceptance criteria. You write the Python yourself.

You'll need three things:

1. **The helper file** — `pet_helpers.py` (already provided in this folder). Don't edit it. Just put it next to your code and import its functions.
2. **Your code** — write it in `pet.py` in this folder.
3. **The save file** — `pet_save.txt` will be created automatically when you save your pet.

> 💡 **Why a helper file?** Some of what this project needs (managing files, picking ASCII art) goes a tiny bit beyond what you've learned in the lessons. The helper file does that part for you. You just call its functions like you've been calling `random.randint()` all along.

---

## Helper Functions You'll Use

At the top of your `pet.py`, add this:

```python
from pet_helpers import (
    save_exists, load_pet, save_pet, delete_save,
    random_species, show_pet_art,
)
```

Now you can use these:

| Function | What it does |
|----------|--------------|
| `save_exists()` | Returns `True` if there's a saved pet, `False` if not |
| `load_pet()` | Reads the save file and returns 8 values (see below) |
| `save_pet(name, species, stage, age, hunger, happiness, energy, cleanliness)` | Saves all 8 values to the file |
| `delete_save()` | Deletes the save file (use when pet dies) |
| `random_species()` | Returns a random species: `"slime"`, `"dragon"`, `"alien"`, or `"robot"` |
| `show_pet_art(species, stage)` | Prints the ASCII art for the given species and life stage (1-4) |

### Loading values with tuple unpacking

`load_pet()` returns **eight values** at once. Use tuple unpacking (from Lesson 10) to put them into separate variables in one line:

```python
name, species, stage, age, hunger, happiness, energy, cleanliness = load_pet()
```

The order is **fixed** — always: `name, species, stage, age, hunger, happiness, energy, cleanliness`.

---

## What You'll Practice

Every concept from Lessons 1–9, plus Lesson 10:

- ✅ Variables, f-strings, input, casting
- ✅ Random numbers (via the helper)
- ✅ `if`/`elif`/`else`, `and`/`or`/`not`, nested ifs, chained comparisons
- ✅ `while True:` + `break` (the action loop)
- ✅ Files (via `save_pet`/`load_pet`/`save_exists`)
- ✅ Tuple unpacking
- ✅ Function calls

---

## Milestones

You'll build the game in **3 milestones**. Each milestone produces a working program — at the end of milestone 1 you have a complete "hatch a pet" demo, at the end of milestone 2 you can play with the pet during a session, and at the end of milestone 3 your pet survives between runs.

| Milestone | What you build | File |
|-----------|----------------|------|
| 1 | Hatch a brand new pet, see its ASCII, save it | [01-hatch.md](01-hatch.md) |
| 2 | Care actions: feed / play / clean / sleep / quit | [02-care.md](02-care.md) |
| 3 | Multi-day persistence: load, age, decay, evolve, die | [03-evolve-and-die.md](03-evolve-and-die.md) |

---

## Stuck?

This project intentionally has **less hand-holding** than Dragon's Tower. Each milestone gives you the rules, not the code. If you get stuck:

1. Re-read the milestone — you might've missed a requirement
2. Re-read [Lesson 10](../../lessons/10-files.md) for file functions
3. Open the `<details>` "Hints" section at the bottom of the milestone
4. Test piece by piece — print stuff to check what your variables hold

---

## Difficulty: 🔥🔥🔥🔥 (~7.5/10)

Tougher than Dragon's Tower because you design the structure yourself. There are no skeletons telling you which `if` to write.

---

## Ready?

Your pet is waiting in its egg. 🥚

👉 **Start with [Milestone 1: Hatch Your Pet](01-hatch.md)**
