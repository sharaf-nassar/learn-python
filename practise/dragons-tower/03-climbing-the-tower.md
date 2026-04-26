# Step 3: Climbing the Tower 🗼

## The Story

The iron gate creaks open. Cold air rushes out. You step into the Dragon's Tower.

A spiral staircase winds up into shadow. Each floor has **two doors** — one leading left, one leading right. Behind some doors: gold and healing potions. Behind others: traps... or worse.

You hear a faint roar from far above. Krath knows you're here.

Climb wisely.

---

## 🎯 Your Mission

After the gate battle, the hero **climbs 3 floors** of the tower. On each floor:
1. The player picks a path: **left** or **right**
2. A random event happens: treasure, trap, or empty room
3. HP and gold update
4. If the hero dies, the game ends
5. After 3 floors, the step ends with a cliffhanger before the dragon

Save your file as **`03_climbing.py`**. Start by **copying everything from Step 2** — keep the gate fight!

---

## 🧠 Concepts You'll Practice

| Concept | Lesson |
|---------|--------|
| Everything from Steps 1 & 2 | — |
| Nested `if` statements | [Lesson 7](../../lessons/07-complex-logic.md) |
| Chained comparisons (`a < b < c`) | [Lesson 7](../../lessons/07-complex-logic.md) |
| `while` loops with a counter | [Lesson 8](../../lessons/08-while-loops.md) |

---

## Step-by-Step

### Part 1: What You Already Have ✅

Step 1 already set up `hero_gold` (10 base + background bonus + Lucky-trait bonus if rolled), `hero_luck`, and `hero_trait`. You'll use all three in this step — no need to redefine them!

Just make sure your character sheet shows them. If it doesn't, scroll back to Step 1 Part 7.

---

### Part 2: Only Climb If You Survived the Gate

Right after the gate battle's victory/defeat message, **only climb if the hero is still alive**. Wrap the climbing code in this:

```python
if hero_hp > 0:
    # Climbing the tower goes here
    ...
```

> 💡 **Why?** If Grukk killed your hero, climbing the tower makes no sense! This is exactly when `if` is useful.

---

### Part 3: The Climbing Loop

Use a `while` loop with a counter to climb 3 floors. **Type this skeleton inside the `if hero_hp > 0:` block:**

```python
floor = 1

while floor <= 3:
    print()
    print("=" * 40)
    print(f"🗼 FLOOR {floor}")
    print("=" * 40)
    print(f"❤️  HP: {hero_hp}    💰 Gold: {hero_gold}")
    print()

    print("Two doors stand before you.")
    print("  1) Take the LEFT door")
    print("  2) Take the RIGHT door")
    door = int(input("Which door? (1/2): "))
    print()

    # TODO: Roll a random event (we'll do this next!)

    floor += 1   # Climb to the next floor

# After the loop ends...
```

> ⚠️ **Don't forget `floor += 1`!** Without it, you're stuck on floor 1 forever.

---

### Part 4: Random Room Events

Inside the loop (where the TODO is), roll a random event. We'll use `random.randint(1, 6)` so each room is different.

The events:

| Roll | Event | Effect |
|------|-------|--------|
| 1, 2 | 💰 Treasure! | +5 gold |
| 3 | 🧪 Healing potion | +5 HP (max 30) |
| 4 | 🕳️ Spike trap | -4 HP |
| 5 | 👹 Slime ambush | -3 HP, but +2 gold for the slime's loot |
| 6 | 🪨 Empty room | Nothing happens |

Here's the **first branch** — you write the rest:

```python
event = random.randint(1, 6)

if event == 1 or event == 2:
    # 🍀 Lucky heroes find more gold! Base 5 + bonus based on luck.
    gold_found = 5 + random.randint(0, hero_luck // 2)
    print(f"💰 You find a chest of gold! +{gold_found} gold")
    hero_gold += gold_found

# TODO: elif event == 3:
#   "🧪 A healing potion! +5 HP"
#   hero_hp += 5
#   But don't go over 30! Use:  if hero_hp > 30: hero_hp = 30

# TODO: elif event == 4:
#   "🕳️ Spike trap! -4 HP"
#   hero_hp -= 4

# TODO: elif event == 5:
#   "👹 A slime ambushes you! -3 HP, +2 gold from its goo"
#   hero_hp -= 3
#   hero_gold += 2

# TODO: else:
#   "🪨 The room is empty. You catch your breath."
```

> 💡 **`event == 1 or event == 2`** is your `or` from Lesson 7 in action! It means "treasure on a roll of 1 OR 2."

---

### Part 5: The "Critical HP" Warning (Chained Comparison!)

Right after the random event, warn the player if they're getting low. This uses the **chained comparison** trick from Lesson 7:

```python
if 0 < hero_hp <= 5:
    print("⚠️  You are critically wounded! One more hit could be fatal!")
```

That reads like math: "0 is less than HP, AND HP is less than or equal to 5." Way cleaner than `hero_hp > 0 and hero_hp <= 5`!

---

### Part 6: Did the Hero Die in That Room?

After every random event, check if the hero survived. If not, end the climb early with `break`:

```python
if hero_hp <= 0:
    print()
    print(f"💀 The tower has claimed {hero_name}. Krath's roar echoes...")
    break
```

> 💡 **`break` exits the climbing loop immediately**, even if you haven't reached floor 3 yet.

---

### Part 7: Reach the Top — Cliffhanger Time!

After the `while floor <= 3:` loop ends, **but only if the hero is still alive**, give them a cliffhanger:

```python
if hero_hp > 0:
    print()
    print("=" * 40)
    print("🌑 You reach a heavy door at the top of the stairs.")
    print(f"🐉 A roar shakes the tower. Krath is just beyond...")
    print(f"❤️  HP: {hero_hp}    💰 Gold: {hero_gold}")
    print("=" * 40)
    print(f"{hero_name}, your final battle awaits in Step 4.")
```

---

## ✅ Test Your Work

Run your game several times. Try to:
- ✅ Beat Grukk and climb all 3 floors
- ✅ Beat Grukk but die on a floor (because of traps/slimes)
- ✅ Lose to Grukk and skip the climb

**Sample run (lucky climb):**

```
🎉 GATE GUARDIAN DEFEATED!
Luna, the gate is yours. The tower awaits...
========================================

========================================
🗼 FLOOR 1
========================================
❤️  HP: 22    💰 Gold: 10

Two doors stand before you.
  1) Take the LEFT door
  2) Take the RIGHT door
Which door? (1/2): 1

💰 You find a chest of gold! +5 gold

========================================
🗼 FLOOR 2
========================================
❤️  HP: 22    💰 Gold: 15

Two doors stand before you.
  1) Take the LEFT door
  2) Take the RIGHT door
Which door? (1/2): 2

🕳️ Spike trap! -4 HP

========================================
🗼 FLOOR 3
========================================
❤️  HP: 18    💰 Gold: 15

Two doors stand before you.
  1) Take the LEFT door
  2) Take the RIGHT door
Which door? (1/2): 1

🧪 A healing potion! +5 HP

========================================
🌑 You reach a heavy door at the top of the stairs.
🐉 A roar shakes the tower. Krath is just beyond...
❤️  HP: 23    💰 Gold: 15
========================================
Luna, your final battle awaits in Step 4.
```

---

## 🤔 Common Pitfalls

| Problem | Fix |
|---------|-----|
| Stuck on floor 1 forever | You forgot `floor += 1` at the bottom of the loop |
| Game keeps climbing after hero dies | Add the `if hero_hp <= 0: break` check after each event |
| Climbing happens even when Grukk wins | Wrap the climbing in `if hero_hp > 0:` |
| HP goes above 30 from potions | Add `if hero_hp > 30: hero_hp = 30` after healing |

---

## ✅ Ready for Step 4?

If you can climb the tower, take damage, find gold, and reach the top alive (sometimes!), you're ready for the final showdown.

👉 **Next: [Step 4 — The Dragon's Lair](04-the-dragons-lair.md)** 🐉🔥

The crown awaits. So does Krath.
