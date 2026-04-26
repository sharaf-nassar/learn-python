# Milestone 3: Evolve & Die 🧬💀

## The Story

The sun rises. Your pet stretches in its bed and looks at you with fresh eyes. Today is **day 2**.

But not every pet wakes up. Skip too many meals, leave it lonely, and one morning... it'll be gone. The save file deleted. A clean desk where the egg used to sit.

If you care for it well, though, you'll watch it **grow** — egg into baby, baby into teen, teen into a full adult. That's the goal.

---

## 🎯 Mission Goal

Make your pet survive across program runs. Each launch is one new day in its life.

You're extending your `pet.py` from Milestones 1 and 2.

---

## 📋 Requirements

When the program starts, it must:

1. **Decide whether to load or hatch:**
   - If `save_exists()` is `True` → load the existing pet with `load_pet()`
   - Otherwise → hatch a new pet (the Milestone 1 flow)
2. **Apply daily decay** to the loaded pet:
   - `age += 1`
   - `hunger += 15`
   - `happiness -= 10`
   - `energy -= 5`
   - `cleanliness -= 10`
   - Then **clamp every stat to 0-100** (just like Milestone 2's actions)
3. **Check for death** (after the decay):
   - If `hunger >= 100` OR `happiness <= 0` → the pet has died
   - Print a sad goodbye message including the pet's name
   - Call `delete_save()`
   - End the program (do NOT enter the action loop)

> 💡 **How to "end the program" using only what you know:**
> Use a flag variable. At the top of your code, set `pet_alive = True`. In the death branch, set `pet_alive = False`. Then wrap your action loop in `if pet_alive:` so it only runs for living pets. Simple and uses just `if` and a variable!
4. **Check for evolution** (if the pet is alive):
   - See the rules below
   - If the pet evolves, print an evolution message and update `stage`
5. **Show a "good morning" status update** with the pet's ASCII (new stage if evolved!) and current stats.
6. Then enter the action loop from Milestone 2.

When the player Saves & Quits, save the pet as before.

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

What do you want to do?
  1) 🍔 Feed
  ...
```

Your version's wording can be different — only the math matters. (You can also display age however you like: `Pip is 1 day old`, `Day 1`, etc.)

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
- ✅ Second run finds `pet_save.txt` and loads it
- ✅ Loaded pet shows `age = 1` after the first overnight, `2` after the next, etc.
- ✅ Stats decay correctly overnight and clamp to 0-100
- ✅ Pet evolves Egg → Baby on the second run (or whenever age first hits 1)
- ✅ Pet evolves Baby → Teen if you care for it well by day 4
- ✅ Pet evolves Teen → Adult by day 8 with high care
- ✅ Neglecting the pet for several runs eventually triggers death (hunger 100 or happiness 0)
- ✅ When the pet dies, `pet_save.txt` is deleted and the program ends without crashing
- ✅ After death, running the program again starts a fresh hatch

---

## 🧪 Testing Tips

You don't have to wait 8 real days! Just keep launching the program over and over to age the pet quickly.

To test **death**, hatch a pet, save & quit immediately, then re-launch many times in a row without doing any care actions. Decay should eventually kill it.

To test **evolution**, hatch and care really well each day (lots of feed/play/clean/sleep) and watch the stage label change.

To start fresh anytime, manually delete `pet_save.txt` from the folder.

---

<details>
<summary>💡 Hints (open if you're stuck)</summary>

- The very first thing in your code should be the `if save_exists():` check. Inside it, use tuple unpacking to load all 8 values. The `else` branch is your Milestone 1 hatch flow.
- Daily decay is a fixed sequence of `+=` and `-=` lines, then 8 clamp checks (4 stats × 2 ends). It's repetitive but fine — you can copy-paste similar lines.
- Death check uses `or`: `if hunger >= 100 or happiness <= 0:`. Don't forget to `delete_save()` AND exit (you can use `return` if you've put your code in a function, or just stop entering the action loop and let the program fall off the bottom).
- Evolution: think of it as three `elif` checks in **highest-stage-first** order so a pet only jumps one stage per day. A standalone `if` chain works too if you're careful.
- For "exit the program after death", you can use `import sys; sys.exit()`. Or just structure your code so that the action loop only runs `if pet_alive:`.
- The stage label translation (1 → "Egg", 2 → "Baby", etc.) is the same one from Milestone 1.

</details>

---

## 🏆 You Built a Tamagotchi!

If your pet survives between runs, decays overnight, evolves, and can die from neglect — congratulations! You've built a real virtual pet using **every concept from Lessons 1 to 10**:

- ✅ Variables, f-strings, input, casting
- ✅ Random numbers (via the helper)
- ✅ `if`/`elif`/`else`, `and`/`or`/`not`, nested ifs, chained comparisons
- ✅ `while True:` + `break` (the action loop)
- ✅ Files (save & load between runs)
- ✅ Tuple unpacking
- ✅ Calling helper functions

**That's a full game with persistence — the same way real apps work.**

---

## What's Next?

You're ready for bigger things. Some ideas:

- 🐍 **Lists** — store multiple pets in one file (a whole pet collection!)
- 🔁 **`for` loops** — iterate over data
- 🧩 **Functions** — bundle code into reusable blocks (you'd love this for the clamp logic)
- 📅 **Real time** — use `datetime` so a "day" is an actual real-world day

Or build your own game! Snake, Hangman, a quiz show — the choice is yours. 🚀
