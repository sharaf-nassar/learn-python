# Step 1: Build Your Hero ⚔️

## The Story

The king's messenger pounds on your door at dawn.

> *"The dragon Krath has stolen the crown! Heroes have failed. The kingdom needs YOU. Climb the Dragon's Tower. Slay the beast. Bring the crown home."*

You grab your weapon and head out. But first... who ARE you, hero?

---

## 🎯 Your Mission

Build a **rich character creation screen**. The player will:
1. See a welcome banner
2. Type their hero's name (no blank names allowed!)
3. Choose a **class** (Warrior, Mage, or Rogue)
4. Choose a **background** (Royal Born, Wanderer, or Outcast)
5. **Roll** a random luck score and special trait — with a chance to **re-roll** if they don't like it!
6. See a complete character sheet with all stats

Save your file as **`01_hero.py`**.

---

## 🧠 Concepts You'll Practice

This step alone uses **most** of what you learned!

| Concept | Lesson |
|---------|--------|
| `print()` and banners | [Lesson 1](../../lessons/01-printing.md) |
| Variables and `+=` | [Lesson 2](../../lessons/02-variables.md) |
| `input()` and f-strings | [Lesson 3](../../lessons/03-input-and-fstrings.md) |
| `int()` casting | [Lesson 4](../../lessons/04-types-and-casting.md) |
| `import random` and `random.randint()` | [Lesson 5](../../lessons/05-random-numbers.md) |
| `if` / `elif` / `else` | [Lesson 6](../../lessons/06-if-else-logic.md) |
| `and` / `or`, nested ifs, chained comparisons | [Lesson 7](../../lessons/07-complex-logic.md) |
| `while True:` + `break`, `.lower()` | [Lesson 8](../../lessons/08-while-loops.md) |

---

## Step-by-Step

### Part 1: Imports and the Welcome Banner

You'll be using random numbers later, so add `import random` at the **very top** of your file. Then print the banner:

```python
import random

print("=" * 40)
print("      🐉  DRAGON'S TOWER  🗡️")
print("=" * 40)
print("Krath the dragon has stolen the crown.")
print("Only a brave hero can climb the tower")
print("and bring it home...")
print()
```

---

### Part 2: Get a Valid Hero Name (No Blanks!)

If the player just presses Enter without typing, `hero_name` would be blank — your character sheet would look broken. Use a **`while True:` loop** to keep asking until they give a real name:

```python
while True:
    hero_name = input("⚔️  What is your hero's name? ")
    if hero_name == "":
        print("❌ A nameless hero is no hero! Try again.")
    else:
        break

print(f"Welcome, brave {hero_name}!")
print()
```

> 💡 **This is your first real validation loop!** Real apps do this all the time — keep asking the user until their input is good enough.

---

### Part 3: Choose a Class

Print the class menu:

| Choice | Class | HP | Attack | Style |
|--------|-------|----|--------|-------|
| 1 | Warrior | 30 | 8 | Tough and brave |
| 2 | Mage | 20 | 12 | Fragile but powerful |
| 3 | Rogue | 25 | 10 | Balanced and sneaky |

```
Choose your class:
  1) Warrior — tough and brave    (HP: 30, Attack: 8)
  2) Mage    — fragile but mighty (HP: 20, Attack: 12)
  3) Rogue   — balanced and sneaky (HP: 25, Attack: 10)
```

Then ask for a choice (remember `int()`!):

```python
class_choice = int(input("Pick your class (1/2/3): "))
```

Now use `if` / `elif` / `else` to set `hero_class`, `hero_hp`, and `hero_attack`:

```python
if class_choice == 1:
    hero_class = "Warrior"
    hero_hp = 30
    hero_attack = 8
# TODO: elif class_choice == 2 (Mage: HP 20, Attack 12)
# TODO: elif class_choice == 3 (Rogue: HP 25, Attack 10)
# TODO: else — set them to a "Peasant" with HP 15, Attack 5 (safety net)
```

---

### Part 4: Choose a Background

Every hero has a story. Show a **second menu** for where they came from:

| Choice | Background | HP bonus | Attack bonus | Gold bonus |
|--------|-----------|---------:|-------------:|-----------:|
| 1 | Royal Born | -2 (soft hands) | 0 | +5 |
| 2 | Wanderer | 0 | +1 | +5 |
| 3 | Outcast | +3 (toughened) | 0 | -3 (started with nothing) |

Print the menu yourself, then ask:

```python
print()
print("Choose your background:")
print("  1) Royal Born — pampered, but well-funded")
print("  2) Wanderer   — a sharper blade, with savings")
print("  3) Outcast    — tougher, but penniless")
bg_choice = int(input("Pick your background (1/2/3): "))
```

**Your turn — write the if/elif/else.** Set: `background`, `hp_bonus`, `attack_bonus`, `gold_bonus`.

```python
if bg_choice == 1:
    background = "Royal Born"
    hp_bonus = -2
    attack_bonus = 0
    gold_bonus = 5
# TODO: elif bg_choice == 2 (Wanderer)
# TODO: elif bg_choice == 3 (Outcast)
# TODO: else — "Commoner": all bonuses = 0
```

Now **apply the bonuses** to the stats from Part 3:

```python
hero_hp += hp_bonus
hero_attack += attack_bonus
hero_gold = 10 + gold_bonus
```

> 💡 **Notice `+=`!** You're adding the bonus to the class stats. A Warrior Outcast = 30 + 3 = **33 HP**. A Mage Royal Born = 20 - 2 = **18 HP** (yikes!). Every combo plays differently.

---

### Part 5: Roll Random Luck and a Trait — With a Re-Roll Option!

Now for the fun part — random rolls! Wrap them in a `while True:` loop so the player can re-roll until they're happy.

```python
while True:
    # 🎲 Roll luck (1 to 10)
    hero_luck = random.randint(1, 10)

    # 🎁 Roll for a trait (1 in 5 chance for each)
    trait_roll = random.randint(1, 5)
    if trait_roll == 1:
        hero_trait = "✨ Brave"
    # TODO: elif trait_roll == 2 → hero_trait = "🎯 Sharp Eye"
    # TODO: elif trait_roll == 3 → hero_trait = "🍀 Lucky"
    # TODO: elif trait_roll == 4 → hero_trait = "🛡️ Tough"
    # TODO: else → hero_trait = "😐 Ordinary"

    # 🍀 The "Lucky" trait gives +5 gold immediately!
    # TODO: if hero_trait == "🍀 Lucky": hero_gold += 5

    # Show what was rolled
    print()
    print(f"🎲 Luck score:  {hero_luck}/10")
    print(f"🎁 Trait:       {hero_trait}")
    print()

    # Ask if happy
    happy = input("Happy with this roll? (yes/no): ").lower()
    if happy == "yes":
        break
    print("🎲 Rolling again...")

    # ⚠️ Important: undo the Lucky bonus before re-rolling, or gold piles up forever!
    # TODO: if hero_trait == "🍀 Lucky": hero_gold -= 5
```

> 💡 **Read the loop carefully:** It rolls, asks "happy?", and only `break`s out when the player says "yes". If they say no, it loops back and rolls fresh values. This is exactly how character creation works in real RPGs!
>
> ⚠️ **Watch out:** if Lucky adds +5 gold and the player re-rolls, you need to *un-add* it or gold keeps stacking. The `TODO` at the bottom handles that.

---

### Part 6: Critical-Stat Warning

Right after the roll loop, give the player a heads-up if their luck is extreme. This uses the **chained comparison** trick from Lesson 7:

```python
if 1 <= hero_luck <= 3:
    print(f"⚠️  Your hero has terrible luck. The journey will be hard...")
elif 8 <= hero_luck <= 10:
    print(f"🌟 Your hero is BLESSED with great fortune!")
```

That `1 <= hero_luck <= 3` reads like math: *"1 is less than or equal to luck, AND luck is less than or equal to 3."* Way cleaner than `hero_luck >= 1 and hero_luck <= 3`!

---

### Part 7: The Complete Character Sheet

Now print everything you've built. Use f-strings to line it all up.

```python
print()
print("=" * 40)
print("       YOUR CHARACTER SHEET")
print("=" * 40)
print(f"Name:       {hero_name}")
print(f"Class:      {hero_class}")
print(f"Background: {background}")
# TODO: print HP, Attack, Gold, Luck, and Trait the same way
print("=" * 40)
print(f"{hero_name} the {background} {hero_class}, your quest begins...")
```

---

## ✅ Test Your Work

Run your program **several times** to test all the paths:

- ✅ Press Enter without typing a name → should reject and ask again
- ✅ Try each class
- ✅ Try each background
- ✅ Re-roll luck a few times until you get something extreme (1 or 10)
- ✅ Try a Mage Royal Born — only 18 HP! That'll be a tough run.
- ✅ Try class `9` and background `9` — your `else` safety nets should catch it

**Sample run (Wanderer Rogue with great luck):**

```
========================================
      🐉  DRAGON'S TOWER  🗡️
========================================
...

⚔️  What is your hero's name?
❌ A nameless hero is no hero! Try again.
⚔️  What is your hero's name? Luna
Welcome, brave Luna!

Choose your class:
  1) Warrior — tough and brave    (HP: 30, Attack: 8)
  2) Mage    — fragile but mighty (HP: 20, Attack: 12)
  3) Rogue   — balanced and sneaky (HP: 25, Attack: 10)
Pick your class (1/2/3): 3

Choose your background:
  1) Royal Born — pampered, but well-funded
  2) Wanderer   — a sharper blade, with savings
  3) Outcast    — tougher, but penniless
Pick your background (1/2/3): 2

🎲 Luck score:  4/10
🎁 Trait:       😐 Ordinary

Happy with this roll? (yes/no): no
🎲 Rolling again...

🎲 Luck score:  9/10
🎁 Trait:       🍀 Lucky

Happy with this roll? (yes/no): yes
🌟 Your hero is BLESSED with great fortune!

========================================
       YOUR CHARACTER SHEET
========================================
Name:       Luna
Class:      Rogue
Background: Wanderer
HP:         25
Attack:     11
Gold:       20
Luck:       9/10
Trait:      🍀 Lucky
========================================
Luna the Wanderer Rogue, your quest begins...
```

> 💰 *Note: Luna started with 10 gold + 5 (Wanderer) + 5 (Lucky trait) = 20 gold.*

---

## 🤔 Common Pitfalls

| Problem | Fix |
|---------|-----|
| `TypeError: ... str ... int` | You forgot `int()` around `input()` |
| Re-rolling gives more and more gold each time | The Lucky trait adds gold; if the player re-rolls, undo it before the next loop. |
| Loop never ends | Make sure `break` only fires when the player typed "yes" — and that you're using `.lower()` so "Yes" works too. |
| `NameError: hero_class` | Did you forget the `else` branch on the class menu? Test with `9`. |
| Luck warning fires for luck = 0 | Use `1 <= hero_luck <= 3`, not `hero_luck <= 3`. |

---

## ✅ Ready for Step 2?

If you can build a hero — name validated, class + background picked, luck and trait rolled and re-rollable — and the character sheet shows all 7 stats correctly, **you're ready**.

👉 **Next: [Step 2 — The Gate Guardian](02-the-gate-guardian.md)** (your luck is about to matter — critical hits incoming!)
