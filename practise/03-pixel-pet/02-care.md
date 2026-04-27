# Milestone 2: Care for Your Pet 🍼

## The Story

The egg wobbles, cracks... and out tumbles your pet. It looks at you with big, hungry eyes.

It needs you. Feed it. Play with it. Bathe it. Tuck it in to sleep.

---

## 🎯 Mission Goal

Add an **action loop** to your program. After hatching the pet, the player should keep choosing actions until they save and quit. Each action affects the pet's stats and gets logged to a daily **activity list**. When they quit, show the day's summary, then save the pet.

Keep your `pet.py` from Milestone 1 — you're extending it.

---

## 📋 Requirements

After the hatch flow from Milestone 1, your program must:

1. Create an empty **activity log list**: `actions_today = []` (right before the action loop starts).
2. Enter an **action loop** that keeps running until the player chooses **Save & Quit**.
3. Each turn of the loop, in order:
   1. **Show the action menu** and read the player's choice
   2. **Handle the choice:**
      - **Feed / Play / Clean / Sleep** (1–4): apply the stat changes, clamp every stat to 0–100, **append** a friendly description to `actions_today`, print a short action message
      - **Stats** (5): just `pass` — no changes (the end-of-turn display below will show the sheet)
      - **Save & Quit** (6): handle as Requirement 4 below, then `break`
      - **Anything else** (e.g. `9`): print `"🤔 I don't know that one!"` and let the loop continue
   3. **Show the pet's ASCII art and current stat sheet** so the player always sees the latest state before the next menu. *(Save & Quit skips this step because of the `break`.)*
4. On Save & Quit:
   - **Print the day's summary** by walking through `actions_today` (see the Activity Log section below)
   - **Save the pet** to `pet_save.txt` — if your Milestone 1 save block is sitting standalone after the hatch (running on every program exit), **move it inside the Save & Quit branch** so it only fires when the player chooses option 6
   - Exit cleanly

> 💡 **Why ASCII + stats at the END of each turn, not the beginning?** The kid's "current state" view comes from EITHER (a) the Milestone 1 character sheet right after hatching, OR (b) the Milestone 3 morning status when reloading. Both happen *before* the action loop starts, so the player has already seen the state when they pick their first action. Then every iteration ends with a refreshed display. This way, no display ever runs twice in a row.

> ⚠️ **About moving your Milestone 1 save block:** In Milestone 1 the save was the *last thing* in your program — it ran every time the program ended. That made sense when the only path was hatch → save → exit. Now you have an action loop, so the save belongs INSIDE the Save & Quit branch. Cut it from where it lives now and paste it into the `if action == 6:` block.

---

## 📐 Action Rules

Use these stat changes — you'll tune them later if you like:

| # | Action | Effects |
|---|--------|---------|
| 1 | 🍔 Feed | hunger −25, happiness +5 |
| 2 | 🎮 Play | happiness +15, energy −20, hunger +10 |
| 3 | 🛁 Clean | cleanliness +30, happiness +5 |
| 4 | 😴 Sleep | energy +30, hunger +5 |
| 5 | 📊 Stats | (no changes — just show the sheet again) |
| 6 | 💾 Save & Quit | save and exit |

Anything else (like `9`) → print a friendly "I don't know that one!" message and re-show the menu.

---

## 📐 Stat Clamping

After every action, **every stat must stay between 0 and 100**. If `hunger` would go below 0, set it to 0. If it would go above 100, set it to 100. Same for the other stats.

> 💡 **Why?** Imagine sleeping when energy is already 95. `+30` would shoot it to 125, which doesn't make sense. The clamp rule keeps things tidy.

---

## 🗒️ Activity Log (Lists at work!)

Track each meaningful action in a list. Right before your action loop starts:

```python
actions_today = []   # Empty list — we'll fill it as the player acts
```

After each successful action — and **only** for Feed/Play/Clean/Sleep — append a friendly description:

```python
# After the Feed action, for example:
actions_today.append(f"Fed {name}")
```

Stay consistent — pick **one** style and use it for all four actions. Suggested: past-tense action by you on the pet, like:

- `f"Fed {name}"`
- `f"Played with {name}"`
- `f"Bathed {name}"`
- `f"Put {name} to bed"`

(Mixing formats like `f"Fed {name}"` with `f"{name} slept"` works but reads a bit jumbled in the daily summary — better to match.)

> ⚠️ **Don't track Stats (option 5) or invalid choices.** Stats is just peeking — the player didn't *do* anything. Invalid choices like `9` shouldn't count either.

When the player picks **Save & Quit**, print the day's summary **before** saving the pet. Walk through the list with a `while` loop and an index counter:

```python
print(f"📊 Today {name} did {len(actions_today)} thing(s):")

i = 0
while i < len(actions_today):
    print(f"  • {actions_today[i]}")
    i += 1
```

> 💡 **Why a `while` loop with an index?** You haven't learned `for` loops yet — those are coming in **Lesson 11**! For now, walking through a list means using a counter `i` and `while i < len(...)`. The counter starts at 0 (computers count from 0!) and goes up by 1 each turn. Lesson 11 will show you a much shorter way to do the exact same thing — and you'll understand *why* it's nicer.

> 💡 **What if `actions_today` is empty?** That's fine! `len(actions_today)` is `0`, the `while` loop doesn't run even once, and you'll just see "Today {name} did 0 thing(s):" with no bullets. No special case needed — that's the magic of `len()`-based loops.

This whole section uses **everything from [Lesson 10](../../lessons/10-lists.md)**: empty list `[]`, `.append()`, `len()`, and reading items by index.

---

## 🎬 Sample Session (after hatching)

```
What do you want to do?
  1) 🍔 Feed
  2) 🎮 Play
  3) 🛁 Clean
  4) 😴 Sleep
  5) 📊 Stats
  6) 💾 Save & Quit
Pick (1-6): 1

🍔 You feed Pip. Pip slurps it up happily!

   _____
  ( o o )
  (~~~~~)   baby slime

Pip's stats:
  Hunger:      0/100
  Happiness:   85/100
  Energy:      80/100
  Cleanliness: 80/100

What do you want to do?
  ...
Pick (1-6): 2

🎮 You play with Pip!
   ... (stats update)

Pick (1-6): 6

📊 Today Pip did 2 thing(s):
  • Fed Pip
  • Played with Pip

💾 Pip is tucked in for the night. Goodnight!
```

(The species/stage shown here is just an example — yours might be a baby alien, an egg robot, etc., depending on how you set it up. We'll keep it stuck on stage 1/2 for now and add evolution in Milestone 3.)

> 🐣 **Heads-up:** You can keep stage at the value the pet hatched with for now. Don't worry about evolution yet — that's Milestone 3.

---

## ✅ Acceptance Criteria

Your program is done when:

- ✅ The action menu appears repeatedly until the player picks Save & Quit
- ✅ Each action changes the right stats by the right amounts
- ✅ Stats never go below 0 or above 100, no matter how many times you click an action
- ✅ Picking an invalid number (like `9`) doesn't crash — it just shows the menu again
- ✅ Stats screen (option 5) shows the ASCII + all 4 stats with no changes
- ✅ The activity log appends one entry per Feed/Play/Clean/Sleep — but **not** for Stats or invalid choices
- ✅ Save & Quit prints "Today {name} did N thing(s):" with one bullet per action
- ✅ If you Save & Quit with zero actions, the summary still works — it just shows "0 thing(s):" with no bullets
- ✅ Save & Quit writes the latest 8 stats to `pet_save.txt` (using your `with open(...)` block from Milestone 1) and ends the program
- ✅ Open `pet_save.txt` after quitting — the 8 values match what you saw on screen

---

## 🧪 Testing Tips

- Click **Feed** 5 times in a row → hunger should hit 0 and stay there, not go negative.
- Click **Sleep** until energy is full (100) → it should not go above 100.
- After quitting, open `pet_save.txt` and verify the numbers match what you saw on screen.

---

<details>
<summary>💡 Hints (open if you're stuck)</summary>

- The action loop is `while True:` with a `break` inside the Save & Quit branch.
- Stat clamping is two `if` checks per stat: `if hunger > 100: hunger = 100` and `if hunger < 0: hunger = 0`.
- You'll repeat this clamp every turn — that's OK, it's just a few lines.
- For option 5 (Stats), just write `pass`. The end-of-turn ASCII + stats display does the rest.
- If your loop runs forever, you forgot `break` in the Save & Quit branch — `Ctrl + C` to stop.
- The activity log lives **only in memory** — when you quit, it disappears. (We'll persist a different list across runs in Milestone 3.)
- The summary loop needs `i = 0` BEFORE the `while`, and `i += 1` INSIDE it. Forgetting `i += 1` makes it loop forever!
- Place `actions_today.append(...)` **inside** each action's `if`/`elif` block — so it only fires when the action actually runs. Don't place it after the if-chain or it'll run for invalid choices too.
- The menu uses `int(input(...))`, which expects a **number** (1–6). If the player presses Enter on its own or types letters, the program will crash with `ValueError`. That's normal at this stage — try/except is a Lesson 12+ topic. Just type a digit.

</details>

---

## ✅ Ready for Milestone 3?

If you can feed, play, clean, sleep, and save & quit — and the stats stay tidy in 0-100 — **you're ready** for the boss milestone: making your pet survive between runs.

👉 **Next: [Milestone 3 — Evolve & Die](03-evolve-and-die.md)** (the longest mission — load, age, decay, evolve, and the rules of life)
