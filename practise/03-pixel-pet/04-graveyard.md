# Milestone 4: The Graveyard 🪦

## The Story

Pets come and pets go. But you don't have to forget them.

Every time a pet dies, their name gets added to a **graveyard file** that lives forever — separate from the save file that gets deleted. The next time you adopt a fresh pet, the egg sits beside a small monument listing every fallen pet who came before.

Your pet game now has **memory** that outlives any single pet.

---

## 🎯 Mission Goal

Add a **persistent graveyard** that remembers every pet you've ever lost. Each new pet you adopt sees the names of those who came before.

You're extending your `pet.py` from Milestone 3.

---

## 🆕 What's New: Two Files, Two Roles

This milestone introduces a key real-world idea: a program can have **multiple save files**, each with a different job.

| File | Role | Lifetime |
|------|------|----------|
| `pet_save.txt` | The **state** of your CURRENT pet | Deleted when pet dies |
| `pet_graveyard.txt` | A **log** of every pet that has died | Grows forever |

This split is everywhere in real software:
- A game might have a "save game" file AND a "high scores" file
- A messaging app keeps your "current chats" AND a "delivered messages" log
- Your phone keeps your contacts AND a call history

---

## 📋 Requirements

1. **Right after `import` lines** (very top of your code), try to load the graveyard:
   - If `pet_graveyard.txt` exists → read it (count + N entries) into a list called `graveyard`
   - Otherwise → `graveyard = []`

2. **On a fresh hatch** (the `else` branch of the load-or-hatch check, after the character sheet and first achievement display):
   - If `len(graveyard) == 0` → print `"🎉 Your first pet! No graveyard yet."`
   - Otherwise → print `"🪦 In memory of (N fallen pets):"` followed by each entry as a bullet

3. **On pet death** (inside the death branch of Requirement 3 in Milestone 3):
   - Figure out the **cause** of death (`"starved"` if hunger ≥ 100, `"ran away"` if happiness ≤ 0)
   - Build a death entry string: `f"{name} the {species.capitalize()} — {cause} on day {age}"`
   - Append it to the `graveyard` list
   - **Write the updated graveyard back to `pet_graveyard.txt`** (using the count-prefix pattern from achievements — the same shape, different file)
   - THEN do the existing M3 death steps: `os.remove("pet_save.txt")`, `pet_alive = False`

4. **On a returning pet** (load flow, not fresh hatch): **don't** show the graveyard. The graveyard appears only at fresh hatches — that's its emotional moment.

---

## 💾 The Graveyard File Format

Same count-prefix pattern as achievements, but in a **separate file**:

```
3                                              ← line 1: count
Pip the Slime — starved on day 4               ← line 2: first fallen pet
Luna the Dragon — ran away on day 2            ← line 3: second fallen pet
Rex the Robot — starved on day 1               ← line 4: third fallen pet
```

> 💡 **Why a count line?** Same reason as achievements — your loader needs to know how many `f.readline()` calls to make. The count is the bridge between "fixed header" (here just the count) and "variable section" (the entries).

> 💡 **First-pet edge case:** If you've never lost a pet, `pet_graveyard.txt` doesn't exist yet. That's totally fine — `os.path.exists()` will return `False`, your `else` branch sets `graveyard = []`, and the empty-graveyard message handles the rest.

---

## 💀 Loading the Graveyard

This goes at the **very top** of your code (after `import`, before the `if os.path.exists("pet_save.txt")` check). Same pattern as loading achievements, just a different filename:

```python
graveyard = []
if os.path.exists("pet_graveyard.txt"):
    with open("pet_graveyard.txt", "r") as f:
        grave_count = int(f.readline())
        i = 0
        while i < grave_count:
            graveyard.append(f.readline().strip())
            i += 1
```

> 💡 **Notice this is THE SAME shape as achievement loading.** Once you spot a pattern in code, your job is just to apply it — don't reinvent the wheel.

---

## 🪦 Showing the Graveyard

After the character sheet and first-achievement display in your hatch flow, drop in this block:

```python
print()
if len(graveyard) == 0:
    print("🎉 Your first pet! No graveyard yet.")
else:
    print(f"🪦 In memory of ({len(graveyard)} fallen pets):")
    i = 0
    while i < len(graveyard):
        print(f"  • {graveyard[i]}")
        i += 1
```

> ⚠️ **Only on fresh hatch — not on load!** Place this inside the `else` branch of your load-or-hatch check, NOT in the load branch. A returning pet doesn't need to see ghosts every morning.

---

## ⚱️ Recording a Death

In the death branch (where you currently set `pet_alive = False` and delete the save), add the graveyard write **before** the existing code:

```python
if hunger >= 100 or happiness <= 0:
    # 1. Figure out the cause
    if hunger >= 100:
        cause = "starved"
    else:
        cause = "ran away"

    # 2. Build the entry and append to the graveyard list
    entry = f"{name} the {species.capitalize()} — {cause} on day {age}"
    graveyard.append(entry)

    # 3. Write the updated graveyard back to disk
    with open("pet_graveyard.txt", "w") as f:
        f.write(f"{len(graveyard)}\n")
        i = 0
        while i < len(graveyard):
            f.write(f"{graveyard[i]}\n")
            i += 1

    # 4. Now your existing M3 death code:
    print()
    print(f"☀️  Good morning... wait.")
    print()
    print(f"💀 {name} {cause} overnight. The kingdom mourns.")
    os.remove("pet_save.txt")
    pet_alive = False
```

> 💡 **The `cause` variable does double duty** — it goes in both the goodbye message AND the graveyard entry. Compute it once, use it twice. That's good programming hygiene.

---

## 🎬 Sample Session

**Run 1 — first pet ever:**

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
... (stats)
========================================

🏆 Pip's achievements:
  • New Slime egg!

🎉 Your first pet! No graveyard yet.

What do you want to do?
  ...
```

**Run later — Pip dies, then a new pet hatches:**

```
========================================
        🐣  PIXEL PET  🐣
========================================
A tiny egg sits on your desk...

What will you name your new pet? Luna
Welcome to the world, Luna!

Rolling species... 🎲 Dragon!

[... character sheet ...]

🏆 Luna's achievements:
  • New Dragon egg!

🪦 In memory of (1 fallen pets):
  • Pip the Slime — starved on day 4

What do you want to do?
  ...
```

**Run after a few more deaths:**

```
🪦 In memory of (3 fallen pets):
  • Pip the Slime — starved on day 4
  • Luna the Dragon — ran away on day 2
  • Rex the Robot — starved on day 1
```

---

## ✅ Acceptance Criteria

- ✅ First-ever run (no `pet_graveyard.txt`): "🎉 Your first pet! No graveyard yet." appears after the character sheet
- ✅ When a pet dies, `pet_graveyard.txt` is created (or updated) with the new entry
- ✅ The graveyard file format: line 1 is the count (a number), then exactly that many entry lines
- ✅ When the next pet hatches fresh (after a death), the graveyard is shown listing the previous pet
- ✅ The graveyard NEVER gets deleted — even when `pet_save.txt` is deleted on death, the graveyard persists across as many pet deaths as you want
- ✅ Multiple deaths over time accumulate (the graveyard list keeps growing — never resets)
- ✅ A **returning** pet (load flow, not fresh hatch) does NOT show the graveyard
- ✅ Open `pet_graveyard.txt` in VS Code after a death — the count and entries should match what was on screen

---

## 🧪 Testing Tips

You don't have to wait for real pet deaths to test:

1. **Force a quick death:** hatch a pet, save & quit, then manually edit `pet_save.txt` to set the hunger value (line 5) to `90`. On the next launch, decay adds `+15` → hunger hits `100+` → death. The graveyard gets its first entry.

2. **Build up the graveyard:** repeat step 1 with a few different pet names. Watch `pet_graveyard.txt` grow.

3. **Reset for testing:** delete BOTH `pet_save.txt` AND `pet_graveyard.txt` to simulate a brand-new install.

4. **Verify file persistence:** after a death, check that `pet_save.txt` is gone but `pet_graveyard.txt` is still there. That's the whole point of the two-file split.

---

<details>
<summary>💡 Hints (open if you're stuck)</summary>

- **Where the graveyard lives in your code:** at the very top, right after `import os` and `import random`, before the `if os.path.exists("pet_save.txt"):` check. The graveyard is a "global" thing, not tied to one pet.

- **The hatch flow has a NEW final step:** after showing the first achievement, show the graveyard. The order is: character sheet → first achievement → graveyard → action loop.

- **The death branch has a NEW first step:** before deleting the save and setting `pet_alive = False`, write the graveyard. Otherwise the dying pet's name won't make it into the file.

- **Two `while` loops, same shape:** one to read the graveyard, one to write it. Both use `i = 0`, `while i < SOMETHING`, do work, `i += 1`. By now you've written this pattern a *lot* — Lesson 11's `for` loop will replace all of them with one cleaner version.

- **Don't forget `\n`** in the writes! Each entry needs to be on its own line. This is the same lesson as the achievement file — every `f.write(f"{...}\n")`.

- **The `cause` variable** is reused in both the goodbye message and the graveyard entry. Compute it once at the top of the death branch.

- **If you see weird characters in the bullets** (like `Pip\\n`), you forgot `.strip()` after `f.readline()`. The newline character is invisible but it's there.

</details>

---

## 🏆 You Built a Memorial!

Your pet game now has **lasting memory** across every pet you've ever cared for. The graveyard is a real **log file** — a pattern used everywhere from server logs to game histories to financial transactions.

You used:
- ✅ Two save files at once — different roles, different lifetimes
- ✅ The count-prefix list pattern, applied a **second** time (achievements + graveyard) — proving the pattern composes
- ✅ Conditional reading (`if os.path.exists(...)` before `open(...)`)
- ✅ List `.append()` on death, list iteration for display
- ✅ A computed variable (`cause`) used in two places

**That's a complete persistence-aware game with both state files AND log files — the way real apps work.**

---

## 🚀 Stretch Ideas

If you want to extend the graveyard further:

- 🥇 **Longest-lived pet** — scan the graveyard for the highest "day N" number and print it as a "personal best"
- 🐲 **Filter by species** — only show fallen Dragons, or only Slimes (uses `in` and string checking)
- 📊 **Cause stats** — count how many pets starved vs. ran away (great practice with `if` inside a list-walking loop)
- ⚰️ **Last words** — when a pet dies, ask the player to type a memorial line that gets saved with the entry
- 🧹 **Graveyard cleanup option** — add a menu choice to clear the graveyard (asks for confirmation, then `os.remove("pet_graveyard.txt")`)

🪦 *Rest in pixels, friends.*
