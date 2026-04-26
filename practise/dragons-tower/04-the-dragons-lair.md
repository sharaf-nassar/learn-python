# Step 4: The Dragon's Lair 🐉🔥

## The Story

You push the heavy door. It swings open with a deep groan.

The chamber at the top of the tower stretches wider than seemed possible. Bones crunch under your boots. Gold and weapons of fallen heroes litter the floor. And there, on a black throne — the crown.

Standing between you and it: **Krath**.

A dragon the size of a house, scales like obsidian, eyes like molten gold.

> *"Another little hero,"* he rumbles. *"How brave. How foolish."*

His wings unfurl. Smoke pours from his nostrils.

This is it.

---

## 🎯 Your Mission

Build the **complete game** — the full Dragon's Tower adventure!

You'll **expand** Step 3 to include:
1. **5 floors** instead of 3, each with a tougher monster fight
2. A choice between fighting or sneaking past some monsters (uses `and`/`or`!)
3. The **dragon boss** at the top with **two phases**:
   - Phase 1: Normal fight
   - Phase 2: When Krath's HP drops below 20, he becomes **enraged** and hits much harder
4. A grand victory ending — or a tragic one.

Save your file as **`04_dragons_tower.py`**. Start by **copying everything from Step 3**.

---

## 🧠 Concepts You'll Practice

This step uses **everything you've learned**. By the end, your game will use every concept from Lessons 1–9.

---

## Step-by-Step

### Part 1: A Battle Helper Pattern

You're going to fight a lot of monsters in this step. Instead of copying the whole battle loop over and over, you'll use a **pattern**: set up monster variables, then run the same battle loop.

> 💡 **Real game devs do this too!** They write the combat once and just change the monster.

For each fight you'll set:
- `monster_name`
- `monster_hp`
- `monster_attack`

Then run the battle loop. **Save your battle loop carefully** — you'll be using it 5 times!

---

### Part 2: The Monster Roster

Replace the random room events from Step 3 with **monster fights**. Use this table:

| Floor | Monster | HP | Attack |
|-------|---------|----|--------|
| 1 | 🟢 Slime | 10 | 3 |
| 2 | 👺 Skeleton | 14 | 4 |
| 3 | 🦇 Bat Swarm | 12 | 5 |
| 4 | 🛡️ Dark Knight | 22 | 7 |
| 5 | 🐉 **Krath the Dragon** | 35 | 9 (Phase 1) / 14 (Phase 2!) |

---

### Part 3: Sneak or Fight? (Floors 1–4)

For floors 1 to 4, give the player a choice **before** the battle:

```python
print(f"A {monster_name} blocks your path!")
print("  1) Fight!")
print("  2) Try to sneak past")
choice = int(input("What do you do? (1/2): "))
```

**Sneaking** uses Lesson 7's complex logic — and a clever **flag variable** called `sneaked` to remember whether the player got past the monster:

```python
sneaked = False   # Start by assuming the hero will fight (not sneak)

if choice == 2:
    # Rogues are great at sneaking. Mages are terrible. Warriors are okay.
    if hero_class == "Rogue":
        sneak_chance = 4   # 4-in-5 chance
    elif hero_class == "Warrior":
        sneak_chance = 2   # 2-in-5 chance
    else:
        sneak_chance = 1   # 1-in-5 chance (Mages and Peasants)

    # 🍀 Lucky heroes are sneakier — add up to +2 from luck
    sneak_chance += hero_luck // 4
    if sneak_chance > 5:
        sneak_chance = 5

    sneak_roll = random.randint(1, 5)
    if sneak_roll <= sneak_chance:
        print(f"🥷 You slip past the {monster_name} unnoticed!")
        sneaked = True   # 🎉 mark success — the battle below will be skipped
    else:
        print(f"💢 The {monster_name} spots you! No choice but to fight!")
        # `sneaked` stays False, so the battle will run normally
```

> 💡 **Why a flag variable?** It's a tidy way to remember something happened. We set `sneaked = True` here, and in the next part we'll wrap the battle in `if not sneaked:` (using `not` from Lesson 7). The battle only runs if the hero **didn't** sneak past!

> 💡 **You can NOT sneak past the dragon!** That's the whole point of the game — fight or die.

---

### Part 4: The 5-Floor Climb

Update your climbing loop to climb **5 floors**. Make sure `floor = 1` is set right before the loop (you had this in Step 3 — it must come along!):

```python
floor = 1   # ← carried over from Step 3 — must be set BEFORE the while loop!

while floor <= 5:
    print()
    print("=" * 40)
    print(f"🗼 FLOOR {floor}")
    print("=" * 40)
    print(f"❤️  HP: {hero_hp}    💰 Gold: {hero_gold}")
    print()

    # ---- Set up the monster for this floor ----
    # ⚠️ All FIVE branches must be filled in! If you forget floor 2, 3, or 4,
    #    your game will crash on those floors with a NameError.
    if floor == 1:
        monster_name = "Slime"
        monster_hp = 10
        monster_attack = 3
    # TODO: elif floor == 2 → Skeleton    (HP 14, Attack 4)
    # TODO: elif floor == 3 → Bat Swarm   (HP 12, Attack 5)
    # TODO: elif floor == 4 → Dark Knight (HP 22, Attack 7)
    elif floor == 5:
        monster_name = "Krath the Dragon"
        monster_hp = 35
        monster_attack = 9

    # ---- Sneak option (only for floors 1-4) ----
    sneaked = False   # Reset each floor — every fight is a fresh chance to sneak!
    if floor < 5:
        # TODO: paste the sneak code from Part 3 here.
        # On a successful sneak, that code sets `sneaked = True`.
        pass   # ← `pass` is a placeholder. Replace it with your sneak code!

    # ---- The battle (only if the hero didn't sneak past!) ----
    if not sneaked:
        # TODO: paste your battle loop here, using monster_name / monster_hp / monster_attack
        pass   # ← `pass` is a placeholder. Replace it with your battle code!

    # ---- Did the hero die? ----
    if hero_hp <= 0:
        break

    # ---- Floor reward (only after a real fight — sneakers keep moving!) ----
    if not sneaked:
        print(f"✨ You take a moment to recover. +3 HP, +2 gold")
        hero_hp += 3
        if hero_hp > 30:
            hero_hp = 30
        hero_gold += 2

    floor += 1
```

> ⚠️ **Three important things:**
> 1. The sneak option only appears on floors 1–4 — `if floor < 5:`
> 2. You **don't get the rest reward** if you die — the death check `break`s before the reward
> 3. You also **don't get the rest reward** if you sneaked past — sneakers keep moving!
>
> 💡 **What is `pass`?** It's a Python placeholder that does nothing. We use it so the empty `if` blocks don't break the program before you fill them in. Once you paste your real code, you can delete the `pass` line.

---

### Part 5: The Dragon's Two Phases (THE BIG ONE!) 🐉

The dragon fight is special. **At the start of each round of the dragon fight**, check his HP. If it dropped below 20, he enters **Phase 2** and his attack jumps to 14.

Inside your battle loop, just after showing the status, add:

```python
# Dragon's enraged phase!
if monster_name == "Krath the Dragon" and monster_hp < 20 and monster_attack < 14:
    print("🔥🔥🔥 KRATH ROARS WITH RAGE! HIS ATTACKS GROW DEADLIER! 🔥🔥🔥")
    monster_attack = 14
```

> 💡 **Read the condition out loud:** "If the monster IS Krath AND his HP is below 20 AND his attack hasn't been boosted yet, then enrage him." Three things, all joined by `and` — that's Lesson 7 in action!
>
> The third check (`monster_attack < 14`) makes sure the message only prints **once**, not every round after he goes below 20.

---

### Part 6: The Endings

After your `while floor <= 5:` loop, write the final endings. Use `if`/`elif`/`else` to pick the right one:

```python
print()
print("=" * 40)

if hero_hp > 0 and floor > 5:
    # Hero survived ALL 5 floors — they killed the dragon!
    print("🏆 VICTORY! 🏆")
    print(f"{hero_name} stands over Krath's fallen body...")
    print(f"You lift the crown high. Sunlight breaks through the tower!")
    print()
    print(f"❤️  Final HP:   {hero_hp}/30")
    print(f"💰 Final Gold: {hero_gold}")
    print()
    print(f"🎉 The kingdom is saved. {hero_name} the {hero_class} is a legend.")

elif hero_hp <= 0:
    print("💀 GAME OVER")
    print(f"{hero_name} the {hero_class} has fallen on floor {floor}.")
    print("The crown remains in Krath's claws... for now.")

# TODO: add an else clause for any other case (like running away successfully).
#       Use it to print a "you escaped" message.

print("=" * 40)
print()
print("Thanks for playing Dragon's Tower!")
```

> 💡 **Read the first condition:** `hero_hp > 0 and floor > 5` means *"hero is alive AND we made it past floor 5."* Both must be true to win!

---

## ✅ Test Your Work

This is the full game! Try to:
- ✅ Win the game with each class (Warrior, Mage, Rogue)
- ✅ Die on the dragon (he's hard!)
- ✅ Sneak past at least one monster
- ✅ Watch Krath's enrage message appear at the right time

**The dragon's enrage moment in a sample run:**

```
========================================
🗼 FLOOR 5
========================================
❤️  HP: 18    💰 Gold: 23

⚔️  You face Krath the Dragon!

❤️  Your HP: 18    💀 Krath the Dragon's HP: 22

What do you do?
  1) Attack
  2) Defend (take half damage next hit)
  3) Run away
Pick (1/2/3): 1

⚔️  You strike Krath the Dragon for 9 damage!
💥 Krath the Dragon slashes you for 6 damage!

❤️  Your HP: 12    💀 Krath the Dragon's HP: 13

🔥🔥🔥 KRATH ROARS WITH RAGE! HIS ATTACKS GROW DEADLIER! 🔥🔥🔥

What do you do?
  ...
```

---

## 🤔 Common Pitfalls

| Problem | Fix |
|---------|-----|
| Krath's enrage message prints every round | Add `monster_attack < 14` to the condition so it only fires once |
| Sneaking still triggers the fight | Use the `sneaked` flag from Part 3: set `sneaked = True` on success, then wrap the battle in `if not sneaked:` |
| Game says "VICTORY" even when hero died | Your condition needs `hero_hp > 0 AND floor > 5` (both!) |
| Hero gets full HP after every floor | The rest reward (`+3 HP`) is fine — just cap with `if hero_hp > 30: hero_hp = 30`. Note: sneakers don't get the reward, so it only fires after a real fight. |
| `NameError: name 'floor' is not defined` | You forgot `floor = 1` before the `while floor <= 5:` loop — it should be carried over from Step 3 |
| `monster_name` is undefined on floor 5 | Make sure you have an `elif floor == 5:` branch |

---

## 🏆 You Did It!

If your game works — hero creation, gate fight, 5-floor climb, sneak option, dragon with two phases, and a victory or death ending — **you've built a complete Python adventure game using every concept from Lessons 1 to 9.**

That is a *huge* accomplishment.

You used:
- ✅ `print()` and banners
- ✅ Variables and `+=`
- ✅ `input()` and f-strings
- ✅ `int()` casting
- ✅ `random.randint()` for damage, events, sneaking
- ✅ `if` / `elif` / `else` for choices
- ✅ `and`, `or`, `not`, nested ifs, chained comparisons
- ✅ `while` loops with `break`

---

🐉 *Krath has fallen. The crown is yours. The kingdom is saved.*

🎉 *Game complete!*
