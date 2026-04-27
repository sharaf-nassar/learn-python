# 🚀 Cosmic Cafe — Practice Project 🍔

> **Your first complete Python project. Build an ordering system for the busiest restaurant in the galaxy — uses everything you've learned through Lesson 8.**

---

## The Story

You are the manager of "The Cosmic Cafe," the busiest restaurant in the galaxy! Customers want to order food, you want to give them combo deals, and the bill needs to come out right.

Time to build a smart ordering system from scratch.

---

## 🎯 What You'll Practice

- `print()` and banners (Lesson 1)
- **Variables** and `+=` updates (Lesson 2)
- **Input** and **f-strings** (Lesson 3)
- **Type conversion** with `int()` (Lesson 4)
- **If/elif/else** decisions (Lesson 6)
- **`and`/`or`/`not`**, nested ifs (Lesson 7)

---

## Difficulty: 🔥 (~4/10)

The easiest of the three practice projects — a great first project right after Lesson 8. No save files, no random numbers, no loops needed.

---

## How to Build It

Save your code as **`cafe.py`**. Build it **step-by-step** — complete each part before moving to the next!

---

### Part 1: Taking the Main Order (Easy)

**Your Task:**
1. Welcome the customer
2. Display a numbered menu
3. Ask for their choice using `int(input())`
4. Confirm their order with `if`/`elif`/`else`

```python
print("🚀 Welcome to the Cosmic Cafe! 🚀")
print()
print("=== MAIN MENU ===")
print("1) Meteor Burger - 10 credits")
print("2) Galaxy Pizza - 12 credits")
print("3) Black Hole Bagel - 8 credits")

main_choice = int(input("Choose a main (1/2/3): "))

if main_choice == 1:
    print("One Meteor Burger coming up!")
elif main_choice == 2:
    print("One Galaxy Pizza coming up!")
elif main_choice == 3:
    print("One Black Hole Bagel coming up!")
else:
    print("Sorry, that's not on the menu!")
```

---

### Part 2: Adding Prices and Sides (Medium)

**Your Task:**
1. Create `total_cost = 0`
2. Add the main dish price to `total_cost`
3. Ask for a side dish
4. Add the side price to `total_cost`
5. Print the subtotal

```python
total_cost = 0

# Add main dish price
if main_choice == 1:
    total_cost += 10    # Burger
elif main_choice == 2:
    total_cost += 12    # Pizza
elif main_choice == 3:
    total_cost += 8     # Bagel

print()
print("=== SIDES ===")
print("0) No side")
print("1) Asteroid Fries - 3 credits")
print("2) Saturn Rings - 4 credits")

side_choice = int(input("Choose a side (0/1/2): "))

if side_choice == 1:
    total_cost += 3
elif side_choice == 2:
    total_cost += 4

print(f"Subtotal: {total_cost} credits")
```

---

### Part 3: Combo Deals! (Hard)

Now add special deals using `and` and `or`:

**Deals:**
- Burger + Fries combo: Save 2 credits
- (Pizza OR Bagel) + any side: Save 1 credit

```python
# Burger + Fries combo
if main_choice == 1 and side_choice == 1:
    print("🎉 Burger + Fries combo! -2 credits")
    total_cost -= 2

# Pizza or Bagel with any side
if (main_choice == 2 or main_choice == 3) and (side_choice != 0):
    print("🎉 Meal deal! -1 credit")
    total_cost -= 1

print(f"After deals: {total_cost} credits")
```

**Note the parentheses!** They make the logic clear:
- `(main_choice == 2 or main_choice == 3)` — Pizza OR Bagel
- `(side_choice != 0)` — They ordered a side

---

### Part 4: Planetary Delivery (Challenge)

Add delivery fees with nested `if` statements:

```python
print()
print("=== DELIVERY ===")
print("1) Mars - 5 credits")
print("2) Venus - 7 credits")
print("3) Jupiter - varies")
print("0) Pickup (free)")

planet = int(input("Delivery destination (0/1/2/3): "))

if planet == 1:
    total_cost += 5
    print("Delivering to Mars!")
elif planet == 2:
    total_cost += 7
    print("Delivering to Venus!")
elif planet == 3:
    is_tuesday = int(input("Is today Tuesday? (1=yes, 2=no): "))
    if is_tuesday == 1:
        print("🎉 Free Jupiter delivery on Tuesdays!")
    else:
        total_cost += 10
        print("Jupiter delivery: 10 credits")
elif planet == 0:
    print("Pickup selected - no delivery fee!")

print()
print("=" * 30)
print(f"💫 TOTAL: {total_cost} credits 💫")
print("=" * 30)
```

---

### Test Your Cosmic Cafe

Try these orders and check your totals:

| Main | Side | Planet | Tuesday? | Expected Total |
| ---- | ---- | ------ | -------- | -------------- |
| 1 (Burger) | 1 (Fries) | 1 (Mars) | - | 16 |
| 2 (Pizza) | 2 (Rings) | 2 (Venus) | - | 22 |
| 3 (Bagel) | 0 (none) | 0 (Pickup) | - | 8 |
| 3 (Bagel) | 1 (Fries) | 3 (Jupiter) | 1 (yes) | 10 |
| 2 (Pizza) | 0 (none) | 3 (Jupiter) | 2 (no) | 22 |

---

## 🎮 Bonus Projects

If you finish the Cosmic Cafe, try these additional challenges!

### Project 2: Rock Paper Scissors Tournament

Build a best-of-5 game against the computer:
- Computer chooses randomly
- Track wins, losses, ties
- Play until someone wins 3 games
- Ask if they want to play again

### Project 3: Number Guessing Game (Enhanced)

- Let the player choose the difficulty (1-10, 1-50, or 1-100)
- Give hints like "very hot" or "cold" based on how close they are
- Track their best score across multiple games

### Project 4: Interactive Story Adventure

- Create a story with at least 3 decision points
- Each choice leads to different outcomes
- Use nested `if` statements for branching paths
- Add random elements for surprise endings!

---

## 🏆 Congratulations!

If you completed the Cosmic Cafe, you've mastered the fundamentals of Python:

✅ Variables and f-strings
✅ Input and type conversion
✅ Random numbers
✅ If/elif/else logic
✅ And/or/not operators
✅ While loops and break

**You're ready to tackle any beginner Python challenge!**

---

## What's Next?

You've got the basics down! Try one of these next:

- 💾 **[Lesson 9: Files](../../lessons/09-files.md)** — make your programs save data between runs
- 📋 **[Lesson 10: Lists](../../lessons/10-lists.md)** — store many things in one variable
- 🐉 **[Dragon's Tower](../02-dragons-tower/README.md)** — bigger adventure project that still only uses Lessons 1-8
- 🐣 **[Pixel Pet](../03-pixel-pet/README.md)** — virtual pet that survives across days (uses the Files lesson)

Keep coding and have fun! 🐍✨

