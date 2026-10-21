# Python Data Types

> **Lesson date:** 20/10/2026
> **Covers:** `int` · `float` · `str` · `bool`
> **Code examples live in:** `Integer.py`, `Float.py`, `Strings.py`, `Boolean.py`

---

## Contents

| # | Data Type | What it holds | Jump |
|---|-----------|---------------|------|
| 1 | **Integer** (`int`) | Whole numbers | [→ Integer](#1-integer-int) |
| 2 | **Float** (`float`) | Numbers with a decimal point | [→ Float](#2-floating-point-float) |
| 3 | **String** (`str`) | Text — words, sentences, anything in quotes | [→ String](#3-string-str) |
| 4 | **Boolean** (`bool`) | True or False | [→ Boolean](#4-boolean-bool) |

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

# 4. Boolean (`bool`)

**The boolean data type represents one of two values: `True` or `False`.**
These values are essential for controlling program flow, making decisions,
and evaluating conditions.

## Basic boolean values

See the top of `Boolean.py`:

```python
is_logged_in = True
is_premium_acc = False
```

Booleans are not strings — `True` and `False` are **keywords**, not text in quotes.

## Booleans from comparison operators

Comparison operators **return** a boolean:

| Operator | Meaning | Example | Result |
|----------|---------|---------|--------|
| `==` | Equal to | `5 == 5` | `True` |
| `!=` | Not equal to | `5 != 3` | `True` |
| `>` | Greater than | `10 > 3` | `True` |
| `<` | Less than | `2 < 5` | `True` |
| `>=` | Greater or equal | `5 >= 5` | `True` |
| `<=` | Less or equal | `4 <= 6` | `True` |

```python
age = 25
is_adult = age >= 18      # True
is_senior = age >= 65     # False
names_match = "Sarah" == "sarah"  # False (case-sensitive)
```

> **Notice:** `"Sarah" == "sarah"` is `False` because Python is
> **case-sensitive** — capital `S` vs lowercase `s`.

## Logical operators — combining conditions

| Operator | Name | Result |
|----------|------|--------|
| `and` | Logical AND | `True` only if **both** sides are `True` |
| `or` | Logical OR | `True` if **either** side is `True` |
| `not` | Logical NOT | Flips `True` to `False`, `False` to `True` |

### `and` — both must be true

```python
is_logged_in = True
has_premium_account = False
can_access_premium = is_logged_in and has_premium_account  # False
```

> **Why `False`?** `and` requires **both** sides to be `True`.
> Here we have `True and False` → `False`.

### `or` — at least one must be true

```python
can_view_content = is_logged_in or has_premium_account  # True
```

> **Why `True`?** `or` only needs **one** side to be `True`.
> `True or False` → `True`.
> Only `False or False` gives `False`.

### `not` — flip the value

```python
is_regular_user = not has_premium_account  # True
```

> **Why `True`?** `has_premium_account` is `False`, so `not False` → `True`.
> Think of `not` as a switch: it always gives you the opposite.

## Complex conditions

You can combine multiple comparisons and logical operators:

```python
is_target_demographic = (age >= 18 and age <= 35) and is_logged_in  # True
```

> **Read it left to right:** Is age between 18 and 35 **AND** is the user logged in?
> Parentheses group the age check together, then the `and is_logged_in` adds the second requirement.

## Converting other types to `bool`

Python has a concept of **truthiness** — most values convert to `True`,
but a few are "falsy" and convert to `False`:

| Value | `bool(value)` |
|-------|---------------|
| `0` | `False` |
| `0.0` | `False` |
| `""` (empty string) | `False` |
| `[]` (empty list) | `False` |
| `None` | `False` |
| **Anything else** | **`True`** |

```python
bool(0)        # False
bool(42)       # True
bool("")       # False
bool("hello")  # True
bool([])       # False
bool([1, 2])   # True
```

## Where booleans are used in real applications

- User authentication (logged in / logged out)
- Feature flags and permissions
- Form validation (is this email valid?)
- Game logic (is the player alive? has the level been completed?)
- Conditional rendering in web apps
- Loop control and branching

---

> **Note:** Booleans are the foundation of **control flow** — `if` statements,
> `while` loops, and ternary expressions all run on boolean logic.
> That comes in the next documentation.