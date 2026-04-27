# Step 2: The Gate Guardian 👹

## The Story

You travel for days. The Dragon's Tower rises above the clouds, twisted and black. At its base, an iron gate blocks your way.

A snarl. A green shape steps from the shadows.

> *"None shall pass! I am Grukk, gate guardian of Krath!"*

The goblin raises a rusty axe.

It's time for your first battle.

---

## 🎯 Your Mission

Add a **battle system** to your game. The player will:
1. Face a goblin (Grukk) with HP and attack power
2. Choose what to do each turn: **Attack**, **Defend**, or **Run**
3. Take or deal random damage
4. Win the battle (goblin's HP hits 0) or lose (their HP hits 0)

Save your file as **`02_first_battle.py`**. Start by **copying everything from Step 1** — your hero is ready to fight!

---

## 🧠 Concepts You'll Practice

| Concept | Lesson |
|---------|--------|
| Everything from Step 1 | — |
| `import random` and `random.randint()` | [Lesson 5](../../lessons/05-random-numbers.md) |
| `and` / `or` / `not` | [Lesson 7](../../lessons/07-complex-logic.md) |
| `while` loops and `break` | [Lesson 8](../../lessons/08-while-loops.md) |

---

## Step-by-Step

### Part 1: Import Random

At the **very top** of your file (before everything else), add:

```python
import random
```

You'll need this for damage rolls.

---

### Part 2: Set Up the Goblin

After the character sheet from Step 1, introduce Grukk:

```python
print()
print("⚔️  You arrive at the Dragon's Tower...")
print("A goblin steps out from the shadows!")
print()
print(">> Grukk the Gate Guardian appears! <<")
print()

goblin_hp = 15
goblin_attack = 5
```

> 💡 **Why these numbers?** A goblin with HP 15 and attack 5 is just challenging enough for a fresh hero. You can tune these later.

---

### Part 3: The Battle Loop (with Critical Hits!)

This is the heart of the battle! We'll use `while True:` and `break` to keep fighting until someone wins.

> 💡 **Your hero's luck stat finally matters!** When you attack, we'll roll a die — if you roll your luck score or lower, you score a **critical hit** for double damage. A hero with `hero_luck = 9` crits 9 times out of 10. A hero with `hero_luck = 2` crits only 2 times out of 10. A hero with the maximum `hero_luck = 10` crits **every single hit** — godly luck! Re-rolling for a high luck stat in Step 1 has real payoff.

Here's the skeleton — copy it, then **fill in the TODO parts**:

```python
while True:
    # Show the battle status
    print(f"❤️  Your HP: {hero_hp}    💀 Grukk's HP: {goblin_hp}")
    print()
    print("What do you do?")
    print("  1) Attack")
    print("  2) Defend (take half damage next hit)")
    print("  3) Run away")
    action = int(input("Pick (1/2/3): "))
    print()

    # ---- ATTACK ----
    if action == 1:
        # Hero hits the goblin
        damage = random.randint(hero_attack - 2, hero_attack + 2)

        # 💥 Critical hit chance based on luck!
        # Roll 1 to 10 — if it's <= hero_luck, it's a crit (double damage)
        crit_roll = random.randint(1, 10)
        if crit_roll <= hero_luck:
            damage *= 2
            print(f"💥 CRITICAL HIT! Lucky strike!")

        goblin_hp -= damage
        print(f"⚔️  You strike Grukk for {damage} damage!")

        # TODO: Did Grukk die? If goblin_hp <= 0, print a victory message and break.

        # If Grukk is still alive, he hits back
        goblin_damage = random.randint(1, goblin_attack)
        hero_hp -= goblin_damage
        print(f"💥 Grukk slashes you for {goblin_damage} damage!")

    # ---- DEFEND ----
    # TODO: elif action == 2:
    #   Grukk attacks but you block half. Use:
    #     goblin_damage = random.randint(1, goblin_attack)
    #     blocked = goblin_damage // 2
    #     hero_hp -= blocked
    #   Then print something like "🛡️  You block! Took only {blocked} damage."

    # ---- RUN ----
    # TODO: elif action == 3:
    #   50/50 chance to escape. Roll: escape_roll = random.randint(1, 2)
    #   If escape_roll == 1: print "💨 You escape!" and break.
    #   Else: print "❌ Grukk blocks your escape!" and let him hit you.

    # ---- INVALID CHOICE ----
    # TODO: else:
    #   print "🤔 You hesitate... Grukk takes the chance!"
    #   Let Grukk hit you anyway.

    # ---- DID THE HERO DIE? ----
    if hero_hp <= 0:
        print()
        print(f"💀 You have fallen, {hero_name}. The kingdom mourns...")
        break

    print()  # Blank line between rounds — easier to read
```

> ⚠️ **The most common mistake:** forgetting to update `goblin_hp` or `hero_hp` inside the loop. If neither HP changes, your loop runs forever! Press `Ctrl + C` if that happens.

---

### Part 4: Victory or Defeat?

After the loop ends, the program needs to know **why** it ended. Did the hero win, or did they fall?

We can check `hero_hp` to find out! Add this **after** the `while` loop (un-indented):

```python
print()
print("=" * 40)
if hero_hp > 0 and goblin_hp <= 0:
    print("🎉 GATE GUARDIAN DEFEATED!")
    print(f"{hero_name}, the gate is yours. The tower awaits...")
elif hero_hp > 0:
    print("💨 You live to fight another day.")
else:
    print("💀 GAME OVER")
print("=" * 40)
```

> 💡 **Notice the `and`!** `hero_hp > 0 and goblin_hp <= 0` means "hero is still alive **AND** goblin is dead" — that's a victory.

---

## ✅ Test Your Work

Run your file a few times. Try each action:
- **Always attacking:** Sometimes you should win, sometimes lose. That's the random damage at work!
- **Defending only:** You'll take less damage but never deal any. You should die slowly.
- **Running:** Sometimes works, sometimes doesn't.
- **Type `9`:** Make sure the `else` saves you (Grukk should still hit you).

**Sample winning run:**

```
⚔️  You arrive at the Dragon's Tower...
A goblin steps out from the shadows!

>> Grukk the Gate Guardian appears! <<

❤️  Your HP: 30    💀 Grukk's HP: 15

What do you do?
  1) Attack
  2) Defend (take half damage next hit)
  3) Run away
Pick (1/2/3): 1

⚔️  You strike Grukk for 9 damage!
💥 Grukk slashes you for 4 damage!

❤️  Your HP: 26    💀 Grukk's HP: 6

What do you do?
...

⚔️  You strike Grukk for 7 damage!

========================================
🎉 GATE GUARDIAN DEFEATED!
Luna, the gate is yours. The tower awaits...
========================================
```

---

## 🤔 Common Pitfalls

| Problem | Fix |
|---------|-----|
| Loop never ends | You forgot `break` after victory or defeat |
| `NameError: hero_hp` | Make sure Step 1's character creation is at the top of this file |
| Damage is always the same | Check that you're inside the loop and using `random.randint()` |
| Hero can run away then keep playing | Run should `break` out of the loop |

---

## ✅ Ready for Step 3?

If you can defeat Grukk (or die trying!) and the game ends cleanly, you're ready to enter the tower.

👉 **Next: [Step 3 — Climbing the Tower](03-climbing-the-tower.md)** 🗼
