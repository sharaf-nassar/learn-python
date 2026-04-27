# Milestone 1: Hatch Your Pet 🥚

## The Story

A small, smooth egg sits on your desk. You don't know what's inside — could be anything. You name it, peek through the shell, and tuck it in for the night.

---

## 🎯 Mission Goal

Build a program that creates a **brand new pet**, prints its character sheet with an egg-stage ASCII drawing, and **saves it to disk**. Running the program twice should hatch two different pets (random species each time).

You'll add care actions in Milestone 2, and persistence in Milestone 3. For now: just hatch.

Save your code as **`pet.py`** in the same folder as `pet_helpers.py`.

---

## 📋 Requirements

Your program must:

1. Print a welcome banner.
2. Ask the player for the pet's name. **Reject blank names** — keep asking until they type something.
3. Pick a **random species** using `random_species()`.
4. Set the pet's starting stats:
   - `stage = 1` (egg)
   - `age = 0`
   - `hunger = 20`
   - `happiness = 80`
   - `energy = 80`
   - `cleanliness = 80`
5. Print a banner introducing the pet.
6. Show the egg ASCII using `show_pet_art(species, stage)`.
7. Print a stat sheet (name, species, stage label, age, all 4 stats).
8. **Save** the pet to disk by writing all 8 values to `pet_save.txt`, one per line. **You write this yourself** — see the file save section below.
9. Print a friendly goodbye.

---

## 🛠️ Tools at Your Disposal

From `pet_helpers`:
- `random_species()` → returns a string like `"slime"`
- `show_pet_art(species, stage)` → prints the ASCII art

From the lessons:
- `print()`, variables, `input()`, f-strings, `int()`, `if`/`elif`/`else`, `while True:` + `break`
- **From [Lesson 9](../../lessons/09-files.md): `open()`, `with`, `f.write()`, `\n`** — you'll use these to save the pet

---

## 📐 Stage Labels

The pet's `stage` is a number, but humans like words. When you print the stat sheet, translate it:

| stage | label |
|------:|-------|
| 1 | Egg |
| 2 | Baby |
| 3 | Teen |
| 4 | Adult |

You only need stage 1 in this milestone, but write the translation anyway — Milestone 3 will use the rest.

---

## 💾 Saving the Pet (Lesson 9 in action!)

Save all 8 values to `pet_save.txt`, **one per line**, in this fixed order:

```
name
species
stage
age
hunger
happiness
energy
cleanliness
```

Use the `with open(...)` + `f.write(...)` pattern from [Lesson 9, Part 4](../../lessons/09-files.md). The shape is exactly the same as the lesson's example — just with 8 values instead of 3:

```python
with open("pet_save.txt", "w") as f:
    f.write(f"{name}\n")
    f.write(f"{species}\n")
    # TODO: write the other 6 values, each followed by \n
```

> ⚠️ **Don't forget the `\n`!** Without it, all 8 values run together on one line and you won't be able to read them back in Milestone 3.
>
> 💡 **The order matters!** Milestone 3's loading code will read in this exact order. If you swap, say, `hunger` and `happiness` here, the pet will load with weird stats next time.

---

## 🎬 Sample Session

Here's roughly what the player should see (your version can be styled differently):

```
========================================
        🐣  PIXEL PET  🐣
========================================
A tiny egg sits on your desk...

What will you name your new pet? Pip
Welcome to the world, Pip!

Rolling species... 🎲 Slime!

   _____
  /  .  \
  \_____/    egg

========================================
       Pip's Character Sheet
========================================
Name:        Pip
Species:     Slime
Stage:       Egg
Age:         0 days
Hunger:      20/100
Happiness:   80/100
Energy:      80/100
Cleanliness: 80/100
========================================

💾 Pip has been saved. See you tomorrow, Pip!
```

---

## ✅ Acceptance Criteria

Your program is done when:

- ✅ Running it asks for a name
- ✅ Pressing Enter on an empty name does NOT crash — it asks again
- ✅ Running it twice in a row gives two pets of (probably) different species
- ✅ The egg ASCII art appears
- ✅ The character sheet shows all 8 stats clearly
- ✅ A file called `pet_save.txt` appears in the folder when you finish
- ✅ Open `pet_save.txt` in VS Code — you should see 8 lines (name, species, 1, 0, 20, 80, 80, 80)

---

<details>
<summary>💡 Hints (open if you're stuck)</summary>

- The "reject blank names" pattern is the same `while True:` + `break` you used in Step 1 of Dragon's Tower.
- The species comes back as a lowercase string like `"slime"`. To show it nicely on the sheet (`Slime`), use `species.capitalize()`. (`.capitalize()` makes the first letter uppercase and lowercases the rest.)
- You can use `.capitalize()` on the name too. If the player types `"pip"` in lowercase, `name.capitalize()` gives you `"Pip"` — handy for the character sheet header `f"{name.capitalize()}'s Character Sheet"`.
- For the stage label, an `if`/`elif`/`else` chain on the `stage` number works perfectly.
- For the save block, you'll have **8** `f.write(...)` lines — one per stat. Make sure each one ends with `\n`!
- Use `"w"` mode (write) — it creates the file or overwrites if it exists. That's exactly what we want.
- Test your save by deleting `pet_save.txt` and running again — a fresh file should appear with 8 lines.
- After running, open `pet_save.txt` in VS Code. You should see something like:
  ```
  Pip
  slime
  1
  0
  20
  80
  80
  80
  ```

</details>

---

## ✅ Ready for Milestone 2?

If you can hatch a random pet, see its egg ASCII, and a `pet_save.txt` file shows up afterward — **you're ready**.

👉 **Next: [Milestone 2 — Care for Your Pet](02-care.md)** (the action menu, where the pet actually lives)
