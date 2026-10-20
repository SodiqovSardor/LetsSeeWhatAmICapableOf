# Python Data Types

> **Lesson date:** 20/10/2026
> **Covers:** `int` · `float` · `str`
> **Code examples live in:** `Integer.py`, `Float.py`, `Strings.py`

---

## Contents

| # | Data Type | What it holds | Jump |
|---|-----------|---------------|------|
| 1 | **Integer** (`int`) | Whole numbers | [→ Integer](#1-integer-int) |
| 2 | **Float** (`float`) | Numbers with a decimal point | [→ Float](#2-floating-point-float) |
| 3 | **String** (`str`) | Text — words, sentences, anything in quotes | [→ String](#3-string-str) |

---

# 1. Integer (`int`)

**Integers are just for whole numbers** — no dot, no decimal part. Like `5`, `250`, `-3`.

## Operations you can do on an int

| Operation | Symbol | Example |
|-----------|--------|---------|
| Addition | `+` | `2 + 3` → `5` |
| Subtraction | `-` | `9 - 4` → `5` |
| Multiplication | `*` | `3 * 4` → `12` |
| Division | `/` | `10 / 4` → `2.5` |
| Floor Division | `//` | `10 // 4` → `2` |
| Exponentiation | `**` | `2 ** 3` → `8` |

## Converting other types to `int`

You can turn other data types into integers with `int()`.
**See the "Type Conversion" section of `Integer.py`.**

```python
word = "250"                # looks like a number, but it's a string
stringtonumber = int(word)  # 250  → now a real integer
```

```python
notaregularnumber = 0.213
floattonumber = int(notaregularnumber)  # 0
```

> **Important:** `int()` **truncates**, it does **not** round.
> The part after the `.` is simply removed: `0.213` → `0`

```python
trueandfalse = True
booleantonumber = int(trueandfalse)  # 1
```

> **Why does this work?** A computer only knows two states —
> active and inactive. `True` is active = `1`, `False` is inactive = `0`.

## Where integers are used in real applications

- Employee IDs and user identification
- Counting items in inventory
- Representing whole numbers in financial calculations
- Array / list indexing and slicing
- Representing dates and times (as timestamps)
- HTTP status codes in web applications

---

# 2. Floating-Point (`float`)

**Floats represent real numbers with decimal points.** They are essential
for any calculation requiring fractional parts beyond whole numbers
(whole numbers = integers = "basic numbers", however you want to call them).

## Basic examples

See the top of `Float.py`:

```python
example_one = 1.123
example_two = 22.34
example_three = 334.5
```

Floats can do the **same basic arithmetic** as integers:
Addition, Subtraction, Multiplication, Division...

## Converting other types to `float`

You can convert strings and integers to a float with `float()`.
**See the "Type Conversion" examples in `Float.py`.**

### String to Float

```python
price_string = "1.99"                    # a string, because of the quotes
price_string_to_float = float(price_string)  # 1.99 → now a real float
```

> **Notice:** the value *looks* the same (`1.99`), but the **data type changed**.

### Integer to Float

```python
price_number = 2                         # an integer — no dot
price_number_to_float = float(price_number)  # 2.0
```

> **Why `2.0` and not `2`?** A float always keeps the `.` and the part
> after it. Since we switched `2` into a float, Python writes it as `2.0`.

## Where floats are used in real life

- Prices and financial calculations *(with care)*
- Scientific measurements and calculations
- Probabilities and statistical values
- Coordinates in graphics or mapping
- Time measurements with fractional parts
- Machine learning model parameters and metrics

---

# 3. String (`str`)

**Strings are for words, sentences, etc.**

## Ways to create a string

All three of these are strings — **the quote style doesn't matter**:

```python
name = "Sardor"        # double quotes
surname = 'Sodiqov'    # single quotes
multi = """triple quotes can span
multiple lines"""
```

See `Strings.py` for the first two in action.

## Strings are immutable

*Immutable* means: **once created, you cannot change the contents.**
Any operation that *appears* to modify a string actually creates a
brand-new string.

## Indexing — accessing characters

Indexes are like **rooms in an office**. Each letter gets a room number.

```
  S a r d o r
  0 1 2 3 4 5
```

> **"Why start at 0? Isn't that dumb?"**
> No — in programming, indexes **always start at zero.** It's a rule,
> not a mistake.

```python
name = "Sardor"
first_char = name[0]   # "S"  → first letter
second_char = name[1]  # "a"  → second letter
```

**See the indexing section of `Strings.py` to run it yourself.**

## Where strings are used

- User data and input processing
- File content manipulation
- Web content (HTML, JSON, XML)
- Database queries
- Configuration settings
- Output formatting and display
- Regular expression pattern matching

---

> **Note:** Python has very powerful **string methods**, but this is the
> first documentation — just the starting point. They come in the next
> documentation.
