# Milestone 2: Care for Your Pet 🍼

## The Story

The egg wobbles, cracks... and out tumbles your pet. It looks at you with big, hungry eyes.

It needs you. Feed it. Play with it. Bathe it. Tuck it in to sleep.

---

## 🎯 Mission Goal

Add an **action loop** to your program. After hatching the pet, the player should keep choosing actions until they save and quit. Each action affects the pet's stats. When they quit, save the pet.

Keep your `pet.py` from Milestone 1 — you're extending it.

---

## 📋 Requirements

After the hatch flow from Milestone 1, your program must:

1. Enter an **action loop** that keeps running until the player chooses **Save & Quit**.
2. Each turn of the loop:
   - Show the pet's ASCII art and current stat sheet
   - Show the action menu
   - Read the player's choice
   - Apply the action (see the rules below)
   - **Clamp** every stat between 0 and 100
3. On Save & Quit, call `save_pet(...)` with the latest values and exit cleanly.

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
- ✅ Save & Quit writes the latest stats to `pet_save.txt` and ends the program
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
- For the "show the stat sheet" sub-routine: when option 5 is picked, you can do nothing extra and let the next loop iteration print the sheet for you. Or print it explicitly. Both work.
- If your loop runs forever, you forgot `break` in the Save & Quit branch — `Ctrl + C` to stop.

</details>

---

## ✅ Ready for Milestone 3?

If you can feed, play, clean, sleep, and save & quit — and the stats stay tidy in 0-100 — **you're ready** for the boss milestone: making your pet survive between runs.

👉 **Next: [Milestone 3 — Evolve & Die](03-evolve-and-die.md)** (the longest mission — load, age, decay, evolve, and the rules of life)
