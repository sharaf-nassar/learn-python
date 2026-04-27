# Milestone 3: Evolve & Die 🧬💀

## The Story

The sun rises. Your pet stretches in its bed and looks at you with fresh eyes. Today is **day 2**.

But not every pet wakes up. Skip too many meals, leave it lonely, and one morning... it'll be gone. The save file deleted. A clean desk where the egg used to sit.

If you care for it well, though, you'll watch it **grow** — egg into baby, baby into teen, teen into a full adult. That's the goal.

---

## 🎯 Mission Goal

Make your pet survive across program runs. Each launch is one new day in its life — and the pet earns **achievements** as it grows, all saved alongside its stats.

You're extending your `pet.py` from Milestones 1 and 2.

---

## 🗺️ Where to Start

This milestone is a big one. Build it in **three layers**, getting each one working before moving to the next:

1. **Layer 1 — Persistence.** Add load + decay + death so the pet wakes up older, hungrier, and possibly dead.
2. **Layer 2 — Evolution.** Once load works, add the stage transitions (Egg → Baby → Teen → Adult).
3. **Layer 3 — Achievements.** Last layer. The list of badges your pet earns, saved alongside the stats in `pet_save.txt`.

Tackle them in order. Don't try to write all three at once — that's how you get stuck. Each layer adds onto the previous one.

---

## 🚦 The `pet_alive` Flag (read this first!)

You'll need to **end the program early** when the pet dies — but you don't know `return` (functions, Lesson 12) or `sys.exit()` yet. Easy fix: a **flag variable** called `pet_alive`. It lives in three spots:

1. **Near the top of your code** (after imports), set `pet_alive = True`
2. **In the death branch**, set `pet_alive = False`
3. **Wrap everything that should NOT run for a dead pet** inside `if pet_alive:`. That means: evolution check, age milestone, morning status, AND the entire action loop.

The decay and death check themselves run **before** `pet_alive` flips, so they don't need wrapping — they're the things that *decide* whether the pet survives.

It's just `if` and a variable — nothing new. Keep this in mind as you read the requirements below.

---

## 📋 Requirements

When the program starts, it must:

1. **Decide whether to load or hatch.** Check for the save file with `os.path.exists("pet_save.txt")` (don't forget `import os` at the top — that's [Lesson 9, Part 5](../../lessons/09-files.md)).
   - **If the save exists** → run the **load flow**:
     - Read the 8 stat values (see the Loading section)
     - Read the achievements list (see the Achievements section)
     - Continue with Requirements 2–6 below
   - **Otherwise** → run the **hatch flow**:
     - Run your Milestone 1 hatch sequence: welcome banner, ask name, pick species, set stats, show ASCII, show character sheet
     - Initialise `achievements = []` and append the first achievement: `f"New {species.capitalize()} egg!"`
     - **Show that first achievement** so the player sees it on day 1 (use the same display block from the Achievements section — Day 1 is special, this is the only "morning" the player gets when there's no save yet)
     - Skip Requirements 2–6 (they only apply on a load) and go straight to Requirement 7

2. **Apply daily decay** (load branch only):
   - `age += 1`
   - `hunger += 15`
   - `happiness -= 10`
   - `energy -= 5`
   - `cleanliness -= 10`
   - Then **clamp every stat to 0-100** (just like Milestone 2's actions)

3. **Check for death** (load branch only, after the decay):
   - If `hunger >= 100` OR `happiness <= 0` → the pet has died
   - Print a sad goodbye message including the pet's name (use the cause: "starved" if hunger, "ran away from a sad home" if happiness)
   - **Delete the save file** with `os.remove("pet_save.txt")` — the achievements die with it
   - Set `pet_alive = False` (see the flag callout above) so nothing else runs

4. **Check for evolution** (load branch only, if alive):
   - See the Evolution Rules below
   - If the pet evolves: print the 3-line celebration (Evolution Rules section), update `stage`, **and append a new achievement** (see the Achievements section)

5. **Check for the age milestone** (load branch only, if alive):
   - If `age >= 7` AND `"Survived a week!"` is **not in** the achievements list → append it

6. **Show a "good morning" status** (load branch only, if alive):
   - The pet's ASCII art (new stage if evolved!)
   - The current 4 stats
   - The full achievements list (use the display block from the Achievements section)

7. **Initialise the activity log and enter the action loop:**
   - `actions_today = []` right before the loop (this is the Milestone 2 list — fresh every session)
   - Run your Milestone 2 action loop, but only if the pet is alive: wrap it in `if pet_alive:`

8. **On Save & Quit (option 6):**
   - Print the day's activity summary (your Milestone 2 code)
   - Save the pet **and its achievements** to `pet_save.txt` — your save block from Milestone 1, **extended** with a count line and the achievement lines (see the Achievements section)
   - Exit cleanly

---

## 💾 Loading the Pet (Lesson 9 strikes again!)

Reading is the mirror image of writing. Open the file in `"r"` mode and call `f.readline()` 8 times — once for each value, in the **same order** you wrote them in Milestone 1:

```python
with open("pet_save.txt", "r") as f:
    name = f.readline().strip()
    species = f.readline().strip()
    stage = int(f.readline())
    age = int(f.readline())
    # TODO: read the other 4 stats (hunger, happiness, energy, cleanliness)
    #       — they're all numbers, so use int(f.readline()) for each
```

> 💡 **Why `.strip()` for text but not for numbers?** `.strip()` removes the trailing `\n` from a string. `int()` ignores whitespace automatically, so you don't need `.strip()` for numbers. (Both are explained in [Lesson 9, Part 4](../../lessons/09-files.md).)

> 💡 **The order MUST match the save!** If you wrote `name, species, stage, age, hunger, happiness, energy, cleanliness` in Milestone 1, you must read them back in that exact order. Mixing up `hunger` and `happiness` will load completely wrong stats.

> 💡 **Heads-up:** This loader will need a few more lines for achievements (the Lesson 10 piece) — see the next section.

---

## 🏆 Achievements (Lesson 9 + Lesson 10 = ❤️)

Your pet earns badges as it grows. They live in a **list**, and the list is **saved to disk** alongside the stats. This is where everything you've learned comes together.

### The achievements

A clean narrative arc tied to life stages — **egg → baby → teen → adult**:

| Trigger | Achievement |
|---------|-------------|
| Fresh start (new egg) | `"New Slime egg!"` (or Dragon, Alien, Robot) |
| Stage 1 → 2 (Egg → Baby) | `"Hatched into a baby!"` |
| Stage 2 → 3 (Baby → Teen) | `"Grew into a teen!"` |
| Stage 3 → 4 (Teen → Adult) | `"Reached adulthood!"` |
| `age >= 7` (first time only) | `"Survived a week!"` |

### When to add each one

**On fresh hatch** (the `else` branch — when no save file exists). Use `species.capitalize()` so `"slime"` becomes `"Slime"`:

```python
achievements = []
achievements.append(f"New {species.capitalize()} egg!")
```

> 💡 **Why "New ... egg!" not "Hatched ..."?** The pet starts at stage 1 = **Egg**. It hasn't hatched yet — that's the *next* achievement (egg → baby). Saying "Hatched" at egg stage would be a contradiction. ("New X egg!" also reads naturally for any species — including Alien, where "Adopted a Alien egg!" sounds wrong because of the missing "n".)

**On evolution** (inside each evolution branch). Print the 3-line celebration (the same format as the Evolution Rules section), then append the matching achievement using `not in` so it never gets added twice:

```python
if stage == 1 and age >= 1:
    stage = 2
    print()
    print(f"✨ ✨ ✨  {name} is evolving!  ✨ ✨ ✨")
    print(f"{name} is now a BABY {species}!")
    if "Hatched into a baby!" not in achievements:
        achievements.append("Hatched into a baby!")
```

(Same shape for stage 2→3 — print "TEEN" and append `"Grew into a teen!"` — and stage 3→4 — print "ADULT" and append `"Reached adulthood!"`.)

**On age milestone** (after the evolution checks, before the morning status):

```python
if age >= 7 and "Survived a week!" not in achievements:
    achievements.append("Survived a week!")
```

> 💡 **Why `not in` everywhere?** Evolution happens once per stage, so technically you don't need the guard for those. But the age check (`age >= 7`) stays True every day after age 7 — without `not in`, "Survived a week!" would be appended **every single day**, ballooning the list. Using `not in` everywhere is a safe, real-world pattern from [Lesson 10, Part 7](../../lessons/10-lists.md).

### Showing the achievements each morning

After load + decay + evolution + age-milestone, show the player what their pet has earned. Use a `while` loop with an index counter (just like the activity log!):

```python
if len(achievements) > 0:
    print()
    print(f"🏆 {name}'s achievements:")
    i = 0
    while i < len(achievements):
        print(f"  • {achievements[i]}")
        i += 1
```

> 💡 **`len(achievements) > 0` skips the heading on day 0** — but a freshly hatched pet already has the `"New [Species] egg!"` achievement, so this almost never shows nothing. Still good defensive practice.

### Saving and loading achievements (extending `pet_save.txt`)

The save file gains a **count line** plus N achievement lines, right after the 8 stat lines:

```
Pip                       ← line 1: name
slime                     ← line 2: species
2                         ← line 3: stage
3                         ← line 4: age
35                        ← line 5: hunger
70                        ← line 6: happiness
75                        ← line 7: energy
70                        ← line 8: cleanliness
2                         ← line 9: HOW MANY achievements (the count!)
New Slime egg!            ← line 10: first achievement
Hatched into a baby!      ← line 11: second achievement
```

**To save**, extend your existing save block:

```python
with open("pet_save.txt", "w") as f:
    # ... your 8 stat writes from Milestone 1 ...

    # Append the achievements section
    f.write(f"{len(achievements)}\n")
    i = 0
    while i < len(achievements):
        f.write(f"{achievements[i]}\n")
        i += 1
```

**To load**, extend your existing load block (inside the `with open("pet_save.txt", "r") as f:` block from the Loading section):

```python
    # ... your 8 stat reads ...

    # Read the achievements section
    achievement_count = int(f.readline())
    achievements = []
    i = 0
    while i < achievement_count:
        achievements.append(f.readline().strip())
        i += 1
```

> 💡 **"Header + variable section" is a real file format pattern.** Many real save files work like this: a fixed header (your 8 stats), a count, then that many records. You just learned a professional trick.

> ⚠️ **The count comes BEFORE the achievements**, never after. Without the count, the loader has no way to know how many `f.readline()` calls to make.

---

## 📐 Daily Decay (overnight)

Applied **only** when loading an existing pet (a freshly hatched pet doesn't decay on day 0).

| Stat | Change | Why |
|------|-------:|-----|
| age | `+1` | One more day older |
| hunger | `+15` | Got hungry overnight |
| happiness | `-10` | Misses you |
| energy | `-5` | Slept restlessly |
| cleanliness | `-10` | Got dusty |

Then clamp all stats to `0-100` (same rule as Milestone 2).

---

## 📐 Death Rules

After applying decay, check **right away**:

- **Hunger reached 100** → "starved"
- **Happiness reached 0** → "ran away from a sad home"

Either condition kills the pet. Print a goodbye message, delete the save, and end the program.

---

## 📐 Evolution Rules

After surviving the day, the pet might evolve. Compute **average care** as:

```
avg_care = (happiness + cleanliness) / 2
```

Then check stages **in order, from highest to lowest**:

| Current stage | Goes to | Required |
|--------------:|--------:|----------|
| 3 (Teen) | 4 (Adult) | `age >= 8` AND `avg_care >= 70` |
| 2 (Baby) | 3 (Teen) | `age >= 4` AND `avg_care >= 60` |
| 1 (Egg)  | 2 (Baby) | `age >= 1` |

A pet evolves at most **ONE stage per day**. Check the rules in **highest-stage-first** order so each pet moves up exactly one step when it qualifies — Egg only ever becomes Baby (never skips to Teen), Baby only ever becomes Teen, and so on.

> 💡 **Heads-up about `/`:** `(happiness + cleanliness) / 2` uses regular division, so `avg_care` will be a decimal like `65.0`. That's totally fine — comparisons like `>= 70` work the same way for decimals.

When the pet evolves, print a celebration like:

```
✨ ✨ ✨  Pip is evolving!  ✨ ✨ ✨
Pip is now a TEEN slime!
```

---

## 🎬 Sample Session (2nd run, right after hatch + save & quit)

This shows what happens on the **second** run, assuming the player hatched Pip and immediately saved & quit on the first run (no care actions yet). Stats trace cleanly from the Milestone 1 starting values.

```
========================================
        🐣  PIXEL PET  🐣
========================================
☀️  Good morning! Pip is now 1 day old.

Overnight, Pip got a bit hungrier and dustier.

✨ ✨ ✨  Pip is evolving!  ✨ ✨ ✨
Pip is now a BABY slime!

   _____
  ( o o )
  (~~~~~)   baby slime

Pip's stats:
  Hunger:      35/100   (was 20, +15 overnight)
  Happiness:   70/100   (was 80, -10)
  Energy:      75/100   (was 80, -5)
  Cleanliness: 70/100   (was 80, -10)

🏆 Pip's achievements:
  • New Slime egg!
  • Hatched into a baby!

What do you want to do?
  1) 🍔 Feed
  ...
```

Your version's wording can be different — only the math matters. (You can also display age however you like: `Pip is 1 day old`, `Day 1`, etc.)

**End of the same day** (after a few care actions, the player picks Save & Quit):

```
Pick (1-6): 6

📊 Today Pip did 3 thing(s):
  • Fed Pip
  • Played with Pip
  • Bathed Pip

💾 Pip is saved. See you tomorrow!
```

After that, your `pet_save.txt` looks like this (open it in VS Code to verify!):

```
Pip
slime
2
1
30
85
55
100
2
New Slime egg!
Hatched into a baby!
```

(8 stat lines, then the count `2`, then the 2 achievement lines. The count is what tells your loader how many `f.readline()` calls to make.)

And a sad death run:

```
========================================
        🐣  PIXEL PET  🐣
========================================
☀️  Good morning... wait.

The bed is empty. There's a small note that reads:
"Pip is gone. Hunger reached 100. The kingdom mourns. 💀"

Save deleted. Run the program again to start a new pet.
```

---

## ✅ Acceptance Criteria

- ✅ First run with no save → hatches a new pet (same as Milestone 1+2)
- ✅ Newly hatched pet has 1 achievement: `"New [Species] egg!"` (where `[Species]` is the capitalised species), AND it's shown to the player on day 1 right after the character sheet
- ✅ Second run finds `pet_save.txt` and loads it (stats AND achievements)
- ✅ Loaded pet shows `age = 1` after the first overnight, `2` after the next, etc.
- ✅ Stats decay correctly overnight and clamp to 0-100
- ✅ Pet evolves Egg → Baby on the second run (or whenever age first hits 1) and earns "Hatched into a baby!"
- ✅ Pet evolves Baby → Teen by day 4 with good care and earns "Grew into a teen!"
- ✅ Pet evolves Teen → Adult by day 8 with high care and earns "Reached adulthood!"
- ✅ At age 7, the achievement "Survived a week!" is earned
- ✅ Achievements **never duplicate** — relaunching after age 7 doesn't add "Survived a week!" again
- ✅ The morning status shows the full achievements list when there are any
- ✅ Open `pet_save.txt` after Save & Quit — first 8 lines are stats, line 9 is the count, then the achievement lines
- ✅ Neglecting the pet for several runs eventually triggers death (hunger 100 or happiness 0)
- ✅ When the pet dies, `pet_save.txt` is deleted and the program ends without crashing
- ✅ After death, running the program again starts a fresh hatch with achievements reset to just `"New [Species] egg!"` (the previous pet's achievements are gone with the deleted save file)

---

## 🧪 Testing Tips

You don't have to wait 8 real days! Just keep launching the program over and over to age the pet quickly.

To test **death**, hatch a pet, save & quit immediately, then re-launch many times in a row without doing any care actions. Decay should eventually kill it.

To test **evolution**, hatch and care really well each day (lots of feed/play/clean/sleep) and watch the stage label change.

To start fresh anytime, manually delete `pet_save.txt` from the folder.

---

<details>
<summary>💡 Hints (open if you're stuck)</summary>

- The very first thing in your code (after `import` lines) should be `if os.path.exists("pet_save.txt"):` — that's the [Lesson 9 Part 5](../../lessons/09-files.md) check. Inside it, open the file in `"r"` mode and read the 8 values with `f.readline()`, **then** the achievement count and the achievement lines. The `else` branch is your Milestone 1 hatch flow.
- **Don't forget `import os` at the top** — same as `import random`. Without it, `os.path.exists` and `os.remove` will crash with `NameError`.
- Daily decay is a fixed sequence of `+=` and `-=` lines, then 8 clamp checks (4 stats × 2 ends). It's repetitive but fine — you can copy-paste similar lines.
- Death check uses `or`: `if hunger >= 100 or happiness <= 0:`. Don't forget to `os.remove("pet_save.txt")` AND set `pet_alive = False` (see the `pet_alive` flag callout near the top of this milestone).
- Evolution: think of it as three `elif` checks in **highest-stage-first** order so a pet only jumps one stage per day. A standalone `if` chain works too if you're careful.
- **Add the achievement INSIDE each evolution branch**, not after the chain — otherwise the achievement fires for the wrong stage transition.
- The `pet_alive` flag is the cleanest way to "end early" with what you know — wrap the whole post-decay flow (death check, evolution, milestone, morning, action loop) inside `if pet_alive:`. (Some grown-up Python code uses `import sys; sys.exit()` for this, but you don't need it yet.)
- The stage label translation (1 → "Egg", 2 → "Baby", etc.) is the same one from Milestone 1. **Now that you know lists, here's a cleaner one-liner you can swap in:**
  ```python
  stage_labels = ["Egg", "Baby", "Teen", "Adult"]
  stage_label = stage_labels[stage - 1]   # stage 1 → index 0
  ```
  This replaces the whole `if`/`elif`/`else` chain with **two lines**. Lookup tables (using a list with the index as the "key") are a real-world Python pattern you'll see all over the place.
- **The achievement count line is the bridge between stats and the list.** When saving, write `f"{len(achievements)}\n"` AFTER the 8 stat writes and BEFORE the achievement writes. When loading, `int(f.readline())` AFTER the 8 stat reads and BEFORE the achievement-reading loop.
- **All four list iterations in this milestone use the same shape** — `i = 0`, `while i < SOMETHING:`, do work, `i += 1`. SOMETHING is either `len(list)` or `achievement_count`. Forgetting `i += 1` is the #1 cause of infinite loops in this milestone.
- `species.capitalize()` makes `"slime"` → `"Slime"`. Use it for the first achievement string: `f"New {species.capitalize()} egg!"`.

</details>

---

## 🏆 You Built a Tamagotchi!

If your pet survives between runs, decays overnight, evolves, earns achievements, and can die from neglect — congratulations! You've built a real virtual pet using **every concept from Lessons 1 to 10**:

- ✅ Variables, f-strings, input, casting
- ✅ Random numbers (via the helper)
- ✅ `if`/`elif`/`else`, `and`/`or`/`not`, nested ifs, chained comparisons
- ✅ `while True:` + `break` (the action loop)
- ✅ **Files — `open()`, `with`, `f.write()`, `f.readline()`, `\n`, `int()` casting on read** (Lesson 9, Parts 2-4)
- ✅ **`os.path.exists()` and `os.remove()`** for save management (Lesson 9, Part 5)
- ✅ **Lists — `[]`, `.append()`, `len()`, index access, `not in`** (Lesson 10) — both the in-session activity log and the persisted achievements
- ✅ **Combining lists + files** — saving and loading a variable-length list with a count header (Lessons 9 + 10 together!)
- ✅ Iterating with `while` + index counter (until `for` loops in Lesson 11 make this much cleaner)
- ✅ Calling helper functions

**That's a full game with persistence — the same way real apps work.**

---

## ✅ Ready for Milestone 4?

If your pet survives between runs, decays, evolves, earns achievements, and dies cleanly when neglected — **you're ready for the final milestone**.

👉 **Next: [Milestone 4 — The Graveyard](04-graveyard.md)** 🪦 (give your fallen pets a permanent memorial that survives between every pet you adopt)

---

## What's Next? (after Milestone 4)

You're ready for bigger things. Some ideas:

- 🔁 **`for` loops** — iterate over a list without the `i = 0` / `while` / `i += 1` dance. Coming in Lesson 11!
- 🐾 **Multi-pet roster** — care for multiple pets at once (a whole pet collection, each with their own achievements!). Needs lists-of-lists or parallel lists.
- 🏅 **More achievements** — try adding "Maxed all stats!" (when all four hit 100), "Two weeks!" (age 14), "A month!" (age 30), or species-specific ones like "First Slime to reach Adult!"
- 🧩 **Functions** — bundle code into reusable blocks (the clamp logic and the activity-log loop would benefit a lot)
- 📅 **Real time** — use `datetime` so a "day" is an actual real-world day

Or build your own game! Snake, Hangman, a quiz show — the choice is yours. 🚀
