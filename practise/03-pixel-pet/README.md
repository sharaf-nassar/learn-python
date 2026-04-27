# 🐣 Pixel Pet — Practice Project 💾

> **Build a virtual pet you keep alive across days. The pet is saved to a file, so it remembers you between runs — just like a real Tamagotchi.**

---

## The Story

You've adopted a tiny digital creature — still inside its mysterious egg. It depends on you to feed it, play with it, clean it, and let it sleep. If you take great care of it, the egg will hatch and your pet will **grow through 4 stages** — egg → baby → teen → adult.

If you neglect it... well, you don't want to find out.

Each time you start the program, **another day passes** in your pet's life. Stats decay overnight. Visit your pet often!

---

## How This Project Works

This is a **practice** project — there are no step-by-step "Part 1, Part 2" walkthroughs. Each milestone gives you a **mission spec**: requirements, rules, sample sessions, and acceptance criteria. You write the Python yourself.

You'll need three things:

1. **The helper file** — `pet_helpers.py` (already provided in this folder). Don't edit it. Just put it next to your code and import its functions.
2. **Your code** — write it in `pet.py` in this folder. **You'll write the save and load logic yourself** — that's the whole point of Lesson 9!
3. **The save file** — `pet_save.txt` will be created automatically by *your* code when you save your pet.

> 💡 **Why a helper file?** ASCII art and species-picking are tedious to write by hand, so the helper does those. **The file save/load is yours to write** — you just learned exactly how in [Lesson 9](../../lessons/09-files.md).

---

## Helper Functions You'll Use

At the top of your `pet.py`, add this:

```python
from pet_helpers import random_species, show_pet_art
```

Now you can use these:

| Function | What it does |
|----------|--------------|
| `random_species()` | Returns a random species: `"slime"`, `"dragon"`, `"alien"`, or `"robot"` |
| `show_pet_art(species, stage)` | Prints the ASCII art for the given species and life stage (1-4) |

That's it — just two helpers. **Everything else is your code.**

### Saving and loading the pet — that's YOUR job

This project uses **two files**, each with a different role:

- **`pet_save.txt`** — the state of your CURRENT pet (8 stats + achievements list). Gets deleted when the pet dies.
- **`pet_graveyard.txt`** — a log of every pet that has ever died. Grows forever.

You'll write all the file and list code yourself, drawing on Lessons 9 (Files) and 10 (Lists):

- **Save** (Milestone 1 onwards) — `with open("pet_save.txt", "w") as f:` and 8 `f.write(...)` calls (extended in Milestone 3 with the achievements section)
- **Activity log** (Milestone 2) — track what the player did today in an in-memory list
- **Achievements** (Milestone 3) — track milestones in a list saved alongside the stats
- **Check & load** (Milestone 3) — `os.path.exists(...)`, 8 `f.readline()` calls, plus a count + N more reads for achievements
- **Delete** (Milestone 3, when the pet dies) — `os.remove("pet_save.txt")`
- **Graveyard** (Milestone 4) — append to `pet_graveyard.txt` on every death so fallen pets are remembered forever

Don't worry — each milestone walks you through what to write.

---

## What You'll Practice

Every concept from Lessons 1–10 — and **Lessons 9 (Files) and 10 (Lists) are the stars**:

- ✅ Variables, f-strings, input, casting
- ✅ Random numbers (via the helper)
- ✅ `if`/`elif`/`else`, `and`/`or`/`not`, nested ifs, chained comparisons
- ✅ `while True:` + `break` (the action loop)
- ✅ **Writing files** (`open` + `with` + `f.write` + `\n`) — you write this!
- ✅ **Reading files** (`f.readline()` + `.strip()` + `int()`) — you write this!
- ✅ **Checking and deleting files** (`os.path.exists`, `os.remove`) — you write this!
- ✅ **Lists** (`[]`, `.append()`, `len()`, index access, `not in`) — three different list usages: an in-session activity log, a persisted achievements collection, AND a graveyard log!
- ✅ **Lists as lookup tables** — replacing if/elif chains with index access (`stage_labels[stage - 1]`)
- ✅ **Combining lists + files** — saving and loading a variable-length list with a count header (Lessons 9 + 10 together!)
- ✅ **Multiple files at once** — a state file (`pet_save.txt`) AND a log file (`pet_graveyard.txt`), each with its own role
- ✅ Iterating with `while` + an index counter (`i = 0`, `while i < len(...):`, `i += 1`) — until `for` loops arrive in Lesson 11 to make it much shorter
- ✅ Function calls

---

## Milestones

You'll build the game in **4 milestones**. Each milestone produces a working program — at the end of milestone 1 you have a complete "hatch a pet" demo, at the end of milestone 2 you can play with the pet during a session, at the end of milestone 3 your pet survives between runs, and at the end of milestone 4 every pet you've ever lost lives on in a graveyard.

| Milestone | What you build | Lessons used | File |
|-----------|----------------|--------------|------|
| 1 | Hatch a brand new pet, see its ASCII, save it to disk | 1–8 + Lesson 9 (write) | [01-hatch.md](01-hatch.md) |
| 2 | Care actions + daily activity log (in-memory list) | + Lesson 10 (lists, `.append()`, `len()`, index access) | [02-care.md](02-care.md) |
| 3 | Load, age, decay, evolve, **earn achievements**, die | + Lesson 9 (read + delete) + Lesson 10 (`not in`) + lists-in-files | [03-evolve-and-die.md](03-evolve-and-die.md) |
| 4 | Pet **graveyard** — a memorial log that survives every pet | + a second save file + the count-prefix pattern reused | [04-graveyard.md](04-graveyard.md) |

---

## Stuck?

This project intentionally has **less hand-holding** than Dragon's Tower. Each milestone gives you the rules, not the code. If you get stuck:

1. Re-read the milestone — you might've missed a requirement
2. Re-read [Lesson 9 (Files)](../../lessons/09-files.md) for file functions
3. Re-read [Lesson 10 (Lists)](../../lessons/10-lists.md) for `[]`, `.append()`, `len()`, index access, and `not in`
4. Open the `<details>` "Hints" section at the bottom of the milestone
5. Test piece by piece — print stuff to check what your variables hold

---

## Difficulty: 🔥🔥🔥🔥🔥 (~8/10)

Tougher than Dragon's Tower because you design the structure yourself **and** combine two of the most powerful concepts in programming (files and lists). There are no skeletons telling you which `if` to write.

---

## Ready?

Your pet is waiting in its egg. 🥚

👉 **Start with [Milestone 1: Hatch Your Pet](01-hatch.md)**
