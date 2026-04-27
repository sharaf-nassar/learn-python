# Lesson 8: While Loops — Repeating Code 🔄

## Goal

Make your programs repeat actions! Learn how to use `while` loops to run code over and over until a condition changes.

## What You'll Learn

- How `while` loops work (repeat while a condition is True)
- The `!=` (not equal) operator
- Using `break` to exit a loop early
- Why loops need variables and conditions
- Avoiding infinite loops (the #1 beginner mistake!)

---

## Part 1: Meet the `while` Loop

A `while` loop is like a persistent friend who keeps asking "Are we there yet?" until the answer changes. It repeats a block of code as long as a condition stays True.

```python
count = 1

while count <= 5:
    print(count)
    count = count + 1

print("Blast off!")
```

**Output:**
```
1
2
3
4
5
Blast off!
```

**How it works:**
1. Check: Is `count <= 5` True? (Yes, count is 1)
2. Run the indented code (print and increment)
3. Go back to step 1
4. Repeat until `count <= 5` is False

---

## Part 2: CRITICAL — Indentation in Loops ⚠️

Just like `if` statements, **indentation is required** for loops!

```python
while count <= 5:
    print(count)       # INDENTED - part of the loop
    count += 1         # INDENTED - part of the loop
print("Done!")         # NOT indented - runs AFTER the loop ends
```

Everything indented under `while` repeats. Un-indented code runs once, after the loop finishes.

**Common mistake:**
```python
while count <= 5:
print(count)           # ❌ IndentationError! Must be indented
```

---

## Part 3: The `!=` Operator — "Not Equal To"

The `!=` operator checks if two things are NOT the same:

```python
print("cat" != "dog")     # True (they're different)
print("hello" != "hello") # False (they're the same)
print(5 != 3)             # True (different numbers)
```

This is perfect for loops that run "until something matches":

```python
answer = ""

while answer != "yes":
    answer = input("Do you want to continue? (yes/no) ")

print("Great, let's go!")
```

---

## Part 4: The Secret Password Game 🔐

Let's build a classic password guessing game:

```python
secret_password = "shark"

print("🔐 Welcome to the Secret Club! 🔐")
print("You need the password to enter...")

guess = input("What is the secret password? ")

while guess != secret_password:
    print("❌ Nope, that's not it. Try again!")
    guess = input("What is the secret password? ")

print()
print("🎉 You got it! Welcome to the club!")
```

**Why do we ask for the guess TWICE?**
- Once BEFORE the loop (to get started)
- Once INSIDE the loop (to get a new guess after they're wrong)

---

## Part 5: `break` — The Emergency Exit 🛑

The `break` statement lets you escape from a loop immediately, even if the condition is still True.

```python
secret_password = "shark"

print("🔐 Welcome to the Secret Club! 🔐")

while True:                                    # Loop forever (until break)
    guess = input("What is the password? ")
    
    if guess == secret_password:
        break                                  # Exit the loop NOW!
    
    print("❌ Wrong! Try again.")

print("🎉 You got it! Welcome!")
```

**Why use `break`?**
- Only ask for input in ONE place (cleaner code)
- Can exit based on multiple conditions
- The logic flows more naturally

---

## Part 6: Adding a "Quit" Option

Use `break` to let users give up:

```python
secret = "shark"

print("🔐 Guess the password! (or type 'quit' to give up)")

while True:
    guess = input("> ")
    
    if guess == "quit":
        print("Goodbye!")
        break
    
    if guess == secret:
        print("🎉 Correct!")
        break
    
    print("❌ Wrong, try again!")
```

---

## Part 7: Counting Attempts

Variables can track how many times the loop runs:

```python
secret = "shark"
attempts = 0

while True:
    guess = input("Password: ")
    attempts += 1                   # Add 1 to attempts each time
    
    if guess == secret:
        print(f"🎉 Correct! It took you {attempts} tries.")
        break
    
    print("❌ Wrong!")
```

---

## Part 8: DANGER — Infinite Loops! ⚠️

An infinite loop runs forever because the condition never becomes False:

```python
# ❌ INFINITE LOOP - DON'T RUN THIS!
count = 1
while count <= 5:
    print(count)
    # Oops! We forgot to update count!
    # count will always be 1, so count <= 5 is always True
```

**How to escape if you accidentally create one:**
- Press `Ctrl + C` in the terminal to stop the program

**How to avoid:**
- Make sure something changes inside the loop
- The condition must eventually become False
- Use `break` with a clear exit condition

---

## Quick Reference

```python
# Basic while loop
while condition:
    # code to repeat
    # something must change so condition becomes False!

# Using break
while True:
    # code
    if should_stop:
        break

# Common operators
!=    # not equal to
==    # equal to
<=    # less than or equal to
```

---

## Common Pitfalls (and Fixes!)

- **Infinite loop:** Make sure something changes inside the loop!
- **Forgot to update the variable:** `count += 1` is often forgotten
- **Wrong indentation:** Everything that repeats must be indented
- **Off-by-one errors:** Test with edge cases (what if they guess right first try?)

---

## 🏠 Homework Task: Number Guessing Game

Create a game where the computer picks a random number and the user guesses:

**Requirements:**
1. Generate a random number between 1 and 20
2. Ask the user to guess
3. Tell them "too high" or "too low"
4. Keep looping until they guess correctly
5. Count and display how many attempts it took

**Starter code:**
```python
import random

secret = random.randint(1, 20)
attempts = 0

print("I'm thinking of a number between 1 and 20...")

while True:
    guess = int(input("Your guess: "))
    attempts += 1
    
    # TODO: Check if guess is correct (break if so)
    # TODO: Tell them if too high or too low
    
print(f"🎉 You got it in {attempts} tries!")
```

**Bonus:** Add a "give up" option that reveals the number.

---

## ✅ Ready for Lesson 9?

If you can write `while` loops that repeat until a condition is met, you're ready!

**Next up: Lesson 9 — Files** (saving and loading data between program runs).

> 💡 **Take a victory lap first!** You've now learned all the core building blocks. Try the **[Cosmic Cafe](../practise/01-cosmic-cafe/README.md)** practice project — it uses everything from Lessons 1–8 and is your first chance to build a complete program from scratch.

