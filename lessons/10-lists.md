# Lesson 10: Lists — Many Things in One Box 📦

## Goal

Store many values in a **single** variable so your programs can manage collections — your hero's inventory, a list of high scores, pizza toppings, names of friends, anything!

## What You'll Learn

- What a list is (a single variable that holds many items)
- How to create lists with `[ ]`
- How to read items by **index** (computers count from 0!)
- How to change items
- How to grow a list with `.append()`
- How to check the size with `len()`
- How to check if something is in a list with `in`
- A few extra list tricks: `.remove()`, `.pop()`, `.sort()`

---

## Part 1: Why Lists?

So far, every variable holds **one** thing. That gets messy fast.

Imagine tracking three monsters in a game:

```python
monster_1 = "Goblin"
monster_2 = "Slime"
monster_3 = "Skeleton"
```

Now five monsters? Ten? You'd need a separate variable for each — and a different `if` to pick the right one. Yuck.

A **list** puts many things into ONE variable:

```python
monsters = ["Goblin", "Slime", "Skeleton"]
```

That's three monsters in one neatly-labeled box. Much better!

---

## Part 2: Making a List

Make a list by putting items inside **square brackets** `[ ]`, separated by commas:

```python
inventory = ["sword", "potion", "key"]
high_scores = [9000, 8500, 8000, 7500]
empty_bag = []        # an empty list — we'll fill it later
```

A list can hold **strings**, **numbers**, or even a mix of types:

```python
mixed = ["Luna", 11, "Seattle"]
```

> 💪 **Try It! — Three Lists**
>
> Open your editor and type these three lists. Run the file:
>
> ```python
> snacks = ["pizza", "cookies", "fries"]      # your top 3 snacks
> seasons = ["spring", "summer", "autumn", "winter"]
> mixed = ["Luna", 11, "purple"]              # name, age, favourite colour
>
> print(snacks)
> print(seasons)
> print(mixed)
> ```
>
> Now change `snacks` to **your** top 3 snacks. Run again. The most common typo with lists is forgetting a comma between items — Python will tell you `SyntaxError` if you do.

---

## Part 3: Reading Items — Index Access

To read an item, use **square brackets with a number** — the **index**.

> ⚠️ **Computers count from 0!** The first item is at index `0`, not `1`.

```python
inventory = ["sword", "potion", "key"]

print(inventory[0])    # sword   (the first item)
print(inventory[1])    # potion
print(inventory[2])    # key
```

**Handy shortcut: `-1` means the LAST item.** No need to count!

```python
print(inventory[-1])   # key      (the last item)
print(inventory[-2])   # potion   (second from the end)
```

> 🤔 **Predict First, Then Run**
>
> Write your guesses on paper, **then** type the code and run it.
>
> ```python
> fruits = ["apple", "banana", "cherry", "date"]
> print(fruits[0])      # ?
> print(fruits[2])      # ?
> print(fruits[-1])     # ?
> print(fruits[-3])     # ?
> ```
>
> <details>
> <summary>Show answers</summary>
>
> - `apple` — index `0` is the first item
> - `cherry` — index `2` is the third item (counting `0`, `1`, `2`)
> - `date` — index `-1` is the last item
> - `banana` — index `-3` is third from the end (`date` is `-1`, `cherry` is `-2`, `banana` is `-3`)
> </details>

> 💪 **Try It! — Same Item, Two Ways**
>
> Make a list of the **5 weekdays** (Monday through Friday). Print **Wednesday** twice — once using a **positive** index, once using a **negative** index. Both prints should show `Wednesday`.
>
> <details>
> <summary>Show solution</summary>
>
> ```python
> weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
> print(weekdays[2])     # positive: 3rd item (counting from 0)
> print(weekdays[-3])    # negative: 3rd from the end
> ```
> </details>

---

## Part 4: Changing Items

Replace an item by assigning to its index:

```python
inventory = ["sword", "potion", "key"]

inventory[1] = "shield"

print(inventory)   # ['sword', 'shield', 'key']
```

The "potion" is gone — replaced by "shield" at position 1.

> 💪 **Try It! — Roster Update**
>
> Your team has three members. One of them is leaving — replace them with a new member.
>
> ```python
> team = ["Alice", "Bob", "Charlie"]
> # TODO: Bob (index 1) is leaving. Replace him with "Diana".
> print(team)
> ```
>
> Expected output: `['Alice', 'Diana', 'Charlie']`
>
> <details>
> <summary>Show solution</summary>
>
> ```python
> team[1] = "Diana"
> ```
> </details>

---

## Part 5: Growing the List with `.append()`

`.append()` adds a new item to the **end** of the list:

```python
inventory = ["sword", "potion", "key"]
inventory.append("torch")
print(inventory)   # ['sword', 'potion', 'key', 'torch']
```

It works on empty lists too — perfect for collecting things over time:

```python
treasures = []

treasures.append("ruby")
treasures.append("emerald")
treasures.append("diamond")

print(treasures)   # ['ruby', 'emerald', 'diamond']
```

> 💪 **Mini-challenge: Treasure Collector**
>
> You're exploring a dungeon. Build a program that asks you for **3 treasures** and adds each one to your bag. Use a `while` loop with a counter (from [Lesson 8](08-while-loops.md)) so you don't have to write `input()` three times by hand.
>
> ```python
> bag = []
> count = 0
>
> # TODO: while count < 3:
> #   ask "What did you find? "
> #   append the answer to bag
> #   count += 1
>
> print(f"You collected: {bag}")
> ```
>
> Sample run:
> ```
> What did you find? sword
> What did you find? potion
> What did you find? ruby
> You collected: ['sword', 'potion', 'ruby']
> ```
>
> **Bonus:** Change `< 3` to `< 5` and collect 5 treasures instead. (One number changes — the rest of the loop just works!)
>
> <details>
> <summary>Show solution</summary>
>
> ```python
> bag = []
> count = 0
>
> while count < 3:
>     treasure = input("What did you find? ")
>     bag.append(treasure)
>     count += 1
>
> print(f"You collected: {bag}")
> ```
>
> 💡 **Why this matters:** This is the first time `.append()` and a `while` loop work together to *build* a list from scratch. You'll do this pattern over and over — high scores, shopping lists, action logs in the Pixel Pet, anything that grows over time.
> </details>

---

## Part 6: How Big? `len()`

The `len()` function tells you how many items are in the list:

```python
inventory = ["sword", "potion", "key", "torch"]
print(len(inventory))    # 4
```

Super handy for "is the bag empty?" or "is it full?":

```python
if len(inventory) == 0:
    print("Your bag is empty!")
elif len(inventory) >= 10:
    print("Your bag is full!")
```

> 🤔 **Predict First, Then Run**
>
> What does each `print()` show?
>
> ```python
> items = ["sword", "shield"]
> print(len(items))            # ?
>
> items.append("torch")
> print(len(items))            # ?
>
> items.append("rope")
> items.append("map")
> print(len(items))            # ?
> ```
>
> <details>
> <summary>Show answers</summary>
>
> - `2` — two items to start
> - `3` — appended `"torch"`, so three items
> - `5` — appended `"rope"` and `"map"`, so five items
>
> **Key idea:** `len()` always reflects the *current* size — it changes every time the list grows or shrinks.
> </details>

> 💪 **Try It! — Bag Status**
>
> Build a "how full is the bag?" reporter. Print one of three messages:
>
> - `"Bag is empty!"` if `len(bag) == 0`
> - `"Bag is full!"` if `len(bag) >= 10`
> - `"Bag has room"` otherwise
>
> ```python
> bag = ["sword", "shield", "potion", "torch"]
> # TODO: write the if/elif/else
> ```
>
> Then change `bag` to `[]` and re-run. Then change it to a list of 10+ items and re-run. You should see all three messages depending on the contents.
>
> <details>
> <summary>Show solution</summary>
>
> ```python
> if len(bag) == 0:
>     print("Bag is empty!")
> elif len(bag) >= 10:
>     print("Bag is full!")
> else:
>     print("Bag has room")
> ```
> </details>

---

## Part 7: Is It in the List? `in`

The `in` operator checks if a value is in the list. It gives you back `True` or `False`:

```python
inventory = ["sword", "potion", "key"]

if "key" in inventory:
    print("🔑 You have the key!")

if "torch" not in inventory:
    print("Better grab a torch — it's dark down there!")
```

This is huge — way cleaner than checking every variable one by one.

> 💪 **Mini-challenge: Door Code**
>
> You're standing at the door of a secret club. The guest list is hard-coded. Ask the user for their name. If they're on the list, welcome them. If not, turn them away.
>
> ```python
> guest_list = ["Alice", "Bob", "Charlie", "Diana"]
> name = input("What's your name? ")
>
> # TODO: if name is in guest_list → "🎉 Welcome to the club, {name}!"
> #       otherwise              → "❌ Sorry {name}, your name isn't on the list."
> ```
>
> Test with **"Alice"** (should welcome) AND **"Eve"** (should turn away).
>
> <details>
> <summary>Show solution</summary>
>
> ```python
> if name in guest_list:
>     print(f"🎉 Welcome to the club, {name}!")
> else:
>     print(f"❌ Sorry {name}, your name isn't on the list.")
> ```
>
> **Bonus thought:** What if someone types `"alice"` (lowercase)? The check is **case-sensitive** — `"alice"` is NOT the same as `"Alice"`. Try it and see! You can fix it with `name.capitalize()` before the check.
> </details>

---

## Part 8: A Few More List Tricks

Some extra methods worth knowing. You'll use `.sort()` in today's homework — the others are good to know exist.

```python
items = ["sword", "potion", "key"]

items.remove("potion")     # remove a specific item by VALUE
items.pop()                # remove and return the LAST item

scores = [8500, 9000, 7500]
scores.sort()              # smallest first → [7500, 8500, 9000]
scores.sort(reverse=True)  # biggest first → [9000, 8500, 7500]
```

> 🤔 **Predict First, Then Run**
>
> Trace the list step by step. What does the final `print` show?
>
> ```python
> scores = [50, 90, 30, 70]
> scores.sort(reverse=True)
> scores.append(100)
> scores.pop()
> scores.remove(50)
> print(scores)              # ?
> ```
>
> <details>
> <summary>Show answer</summary>
>
> Final: `[90, 70, 30]`
>
> Step by step:
> - Start: `[50, 90, 30, 70]`
> - `.sort(reverse=True)` (biggest first) → `[90, 70, 50, 30]`
> - `.append(100)` (add to end) → `[90, 70, 50, 30, 100]`
> - `.pop()` (remove last) → `[90, 70, 50, 30]`
> - `.remove(50)` (remove that value) → `[90, 70, 30]`
>
> **Tip:** When a problem chains list methods like this, write the list out on paper after **each** line. Way easier than tracing it all in your head.
> </details>

---

## Part 9: Putting It Together — Hero's Bag

```python
hero_bag = ["sword", "shield"]

print(f"You have {len(hero_bag)} items.")

# Pick something up
hero_bag.append("torch")
print(f"You picked up a torch! Now you have {len(hero_bag)} items.")

# Use a key — only if you have one
if "key" in hero_bag:
    print("🔑 You unlock the door!")
    hero_bag.remove("key")
else:
    print("🔒 The door is locked. You need a key.")

print(f"Bag: {hero_bag}")
```

**Output:**
```
You have 2 items.
You picked up a torch! Now you have 3 items.
🔒 The door is locked. You need a key.
Bag: ['sword', 'shield', 'torch']
```

(There's no "key" in the bag, so the `else` branch runs. Try changing the starting bag to `["sword", "shield", "key"]` and see what happens!)

---

## Quick Reference

```python
items = []                    # empty list
items = ["a", "b", "c"]       # list with values

items[0]                      # first item
items[-1]                     # last item
items[1] = "new"              # change item

items.append("x")             # add to end
items.remove("a")             # remove by value
items.pop()                   # remove last item

len(items)                    # how many?
"a" in items                  # True or False
items.sort()                  # in order
```

---

## Common Pitfalls (and Fixes!)

| Problem | Fix |
|---------|-----|
| `IndexError: list index out of range` | The index is too big. A 3-item list has indexes 0, 1, 2 — not 3! |
| Forgot computers count from 0 | The FIRST item is `items[0]`, not `items[1]` |
| `.append()` doesn't seem to do anything | It changes the list in place — print the list AFTER to see the change |
| `.remove("X")` crashes | "X" isn't in the list. Check first with `if "X" in items:` |
| Got the wrong item | Did you mean the index or the value? `items[0]` is the FIRST item; `items.remove("sword")` removes "sword" by VALUE |

---

## 🏠 Homework Task: Top Scores Tracker

Build a high-score tracker that keeps the **top 5** scores.

**Your program should:**
1. Start with an empty list called `scores`
2. In a `while True:` loop, ask the player to enter a score, or type `quit` to stop
3. If they entered a number, append it to the list
4. If they typed `quit`, break out of the loop
5. After they quit:
   - Sort the scores from highest to lowest
   - Show the top scores in a numbered list — **up to 5** (if they entered fewer than 5, just show however many there are; don't crash!)
   - Show how many scores were entered total

**Watch out!** `int()` will crash on `"quit"`. Check if the input is `"quit"` BEFORE converting it to a number.

**Hint for "up to 5":** A `while` loop with a counter variable that stops at `5` OR at `len(scores)` (whichever comes first) is exactly the job. The `and` operator from Lesson 7 lets you combine both conditions.

**Bonus:**
- If they type `clear` instead of a number, empty the list (`scores = []`) and confirm
- If they type `last`, show the last score they entered (`scores[-1]`)

**Sample run:**
```
Enter a score (or 'quit'): 8500
Enter a score (or 'quit'): 9200
Enter a score (or 'quit'): 7000
Enter a score (or 'quit'): quit

🏆 Top scores:
  1. 9200
  2. 8500
  3. 7000

Total scores entered: 3
```

---

