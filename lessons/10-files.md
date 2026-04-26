# Lesson 10: Saving Your Work — Files 💾

## Goal

Make your programs **remember things** between runs! By the end of this lesson, you'll know how to save data to a file and load it back the next time. This is how real games keep your high score, your save game, and your progress.

## What You'll Learn

- Why files are useful (saving data between runs)
- How to **write** text to a file with `open()` and `with`
- How to **read** text back from a file
- How to save **multiple values** on separate lines
- How to **check if a file exists** before reading it
- **Tuple unpacking** — putting several values into separate variables in one line

---

## Part 1: Why Save Data?

Every program you've built so far **forgets everything** when you close it.

Run the Cosmic Cafe twice — it starts fresh both times. Run Dragon's Tower twice — your hero from yesterday is gone.

Real games and apps **save your progress** to a file on your computer. The next time you open the app, it **loads** what was saved.

- Minecraft remembers your world
- Mario remembers your high score
- Your phone remembers your contacts

A file is just a text document on your computer. Python can write text into it and read text out of it — like a person writing in a notebook and reading it back later.

---

## Part 2: Writing to a File

To save text to a file, use Python's `open()` function with `"w"` mode (for **write**):

```python
with open("hello.txt", "w") as f:
    f.write("Hello, world!")
```

**Read it line by line:**

1. `open("hello.txt", "w")` — opens (or creates) a file called `hello.txt` in write mode
2. `with ... as f:` — gives the file a nickname `f` (for "file") so you can use it
3. `f.write("Hello, world!")` — writes the text into the file
4. When the `with` block ends, Python automatically closes the file safely

**Try it!** Run that code, then open `hello.txt` in VS Code — you'll see your text inside.

> ⚠️ **Important:** `"w"` mode **erases** the file first if it already exists. It's a fresh write every time! If you want to add to an existing file instead, use `"a"` (append) mode.

---

## Part 3: Reading from a File

To read text from a file, use `"r"` mode (for **read**):

```python
with open("hello.txt", "r") as f:
    text = f.read()

print(text)   # Shows: Hello, world!
```

`f.read()` reads everything in the file and gives it back to you as a string.

**The pattern is always the same:** `open` the file, `with` block, do your read or write inside, and Python handles closing.

---

## Part 4: Saving Multiple Values

Most of the time you want to save more than one thing — like a player's **name** AND their **score** AND their **level**.

The trick: put **each value on its own line** by adding `\n` (the newline character) after each one.

**Saving three values:**

```python
player_name = "Luna"
high_score = 9000
level = 3

with open("save.txt", "w") as f:
    f.write(f"{player_name}\n")
    f.write(f"{high_score}\n")
    f.write(f"{level}\n")
```

That creates a file that looks like:

```
Luna
9000
3
```

**Reading them back, one line at a time:**

```python
with open("save.txt", "r") as f:
    saved_name = f.readline().strip()    # First line
    saved_score = int(f.readline())       # Second line
    saved_level = int(f.readline())       # Third line

print(f"Welcome back, {saved_name}!")
print(f"Score: {saved_score}, Level: {saved_level}")
```

`f.readline()` reads **one line** and moves to the next one. Three calls = three lines.

> 💡 **`.strip()`** removes whitespace (including the `\n` at the end) from a string. Use it for text values.
>
> 💡 **`int()`** handles the `\n` automatically — no `.strip()` needed when you're converting to a number.
>
> 💡 **Files only store text!** Even numbers are saved as text. That's why `int()` is needed when reading them back.

---

## Part 5: Checking if a File Exists

What happens if your program tries to read a save file that doesn't exist yet? **It crashes!** 💥

```
FileNotFoundError: [Errno 2] No such file or directory: 'save.txt'
```

To avoid this, check first using the `os` library:

```python
import os

if os.path.exists("save.txt"):
    print("Save file found! Loading...")
    # ... read the file
else:
    print("No save yet. Starting fresh.")
    # ... use default values
```

`os.path.exists("save.txt")` returns `True` if the file exists, `False` if not.

**Don't forget `import os` at the top of your file** — just like `import random`!

---

## Part 6: Tuple Unpacking

Sometimes you want to put several values into separate variables in **one line**. Python has a clever shortcut called **tuple unpacking**:

```python
# Instead of three lines:
a = 10
b = 20
c = 30

# You can do it in one:
a, b, c = 10, 20, 30

print(a)   # 10
print(b)   # 20
print(c)   # 30
```

The rule: **the same number of variables on the left as values on the right**, separated by commas.

This is useful when a single function gives you back several values at once. You'll see it in the practice projects when a helper function returns a whole bunch of pet stats at the same time:

```python
# Pretend a helper function returns three things at once.
# Tuple unpacking lets us catch them all in one line:
pet_name, pet_age, pet_hunger = some_load_function()
```

Same idea — three variables on the left, three values on the right.

---

## Quick Reference

```python
# Writing
with open("file.txt", "w") as f:
    f.write("Hello")

# Writing multiple values (use \n between them!)
with open("save.txt", "w") as f:
    f.write(f"{name}\n")
    f.write(f"{score}\n")

# Reading the whole file
with open("file.txt", "r") as f:
    text = f.read()

# Reading line by line
with open("save.txt", "r") as f:
    name = f.readline().strip()
    score = int(f.readline())

# Checking if a file exists
import os
os.path.exists("file.txt")     # True or False

# Tuple unpacking
x, y, z = 1, 2, 3
```

---

## Common Pitfalls (and Fixes!)

| Problem | Fix |
|---------|-----|
| `FileNotFoundError` when reading | Use `os.path.exists()` to check first |
| File is empty after running again | `"w"` mode **erases first**! Use `"a"` if you want to append. |
| Numbers come out wrong | Files store **text** — wrap reads with `int()` or `float()` |
| Extra `\n` in your text | Use `.strip()` after `.readline()` |
| `NameError: name 'os' is not defined` | Add `import os` at the top |
| File saves with everything on one line | Did you forget `\n` between values when writing? |

---

## 🏠 Homework Task: Player Profile

Build a small program that asks for the player's **name**, **favorite color**, and **lucky number** — then **saves** them to a file called `profile.txt`. The next time the program runs, it should **greet the player by name** and show their saved info.

**Your program should:**
1. Use `os.path.exists()` to check for `profile.txt`
2. **If it exists:** read the saved info and welcome the player back with a personalized greeting
3. **If not:** ask for the info, save it, and welcome them as a brand-new user

**Bonus:**
- Add a "Reset profile" option that uses `os.remove("profile.txt")` to delete the file
- Save extra fields like favorite food or hometown

**Example second-run output:**
```
👋 Welcome back, Luna!
🎨 Your favorite color: purple
🍀 Your lucky number: 7
```

---

## ✅ Ready for Module 6?

If you can save data to a file and read it back the next time your program runs, you've unlocked one of the most powerful skills in programming. Real apps live and die by this!

**Next up: Module 6 — Practise Projects** (the next project, **Pixel Pet**, uses files to keep your virtual pet alive across days!)
