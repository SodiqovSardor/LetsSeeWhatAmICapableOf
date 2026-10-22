# Python Basic Operators

> **Lesson date:** 22/10/2026
> **Covers:** Arithmetic operators, string operators, list operators
> **Code examples live in:** `BasicOperators.py`

---

## Contents

| # | Topic | Jump |
|---|-------|------|
| 1 | Arithmetic operators (numbers) | [→ Arithmetic](#1-arithmetic-operators) |
| 2 | Operators with strings | [→ Strings](#2-operators-with-strings) |
| 3 | Operators with lists | [→ Lists](#3-operators-with-lists) |

---

# 1. Arithmetic Operators

Arithmetic operators work with numbers (integers and floats) just like in math.

| Operator | Name | Example | Result |
|----------|------|---------|--------|
| `+` | Addition | `1 + 2 + 3 + 4` | `10` |
| `-` | Subtraction | `10 - 9 - 8 - 7` | `-14` |
| `*` | Multiplication | `2 * 1` | `2` |
| `/` | Division | `4 / 2` | `2.0` |
| `//` | Floor Division | `4 // 2` | `2` |
| `%` | Modulo (remainder) | `11 % 3` | `2` |
| `**` | Exponentiation (power) | `7 ** 2` | `49` |

## Code examples

```python
addition = 1 + 2 + 3 + 4        # 10
subtraction = 10 - 9 - 8 - 7    # -14
multiplication = 2 * 1          # 2
division = 4 / 2                # 2.0  (always returns float)
floor_div = 4 // 2              # 2    (integer result)
remainder = 11 % 3              # 2    (remainder after division)
squared = 7 ** 2                # 49   (7 to the power of 2)
cubed = 7 ** 3                  # 343  (7 to the power of 3)
```

> **Division vs Floor Division:**
> - `/` always returns a **float** (`2.0`)
> - `//` returns an **int** when both operands are ints (`2`)
> - Use `//` when you want to discard the decimal part

> **Modulo (`%`)** — "Qoldiq" in Uzbek — gives the **remainder** after division.
> `11 % 3` means: how many times does 3 go into 11? 3 × 3 = 9, remainder is 2.

> **Exponentiation (`**`)** — "darajalar uchun" — raises to a power.
> `7 ** 2` = 7² = 49. `7 ** 3` = 7³ = 343.

---

# 2. Operators with Strings

Strings support two operators: `+` (concatenation) and `*` (repetition).

## Concatenation with `+`

```python
helloworld = "hello" + " " + "world"  # "hello world"
```

> The `+` operator **joins strings together**. The space `" "` in the middle
> keeps the words from collapsing into `"helloworld"`.

## Repetition with `*`

```python
lots_of_hellos = "hello " * 5  # "hello hello hello hello hello "
```

> The `*` operator **repeats the string** that many times.
> The trailing space in `"hello "` keeps repetitions separated.

> **Note:** You cannot use `-`, `/`, `%`, or `**` with strings — only `+` and `*`.

---

# 3. Operators with Lists

Lists also support `+` (concatenation) and `*` (repetition).

## Concatenation with `+`

```python
odd_numbers = [1, 3, 5, 7]
even_numbers = [2, 4, 6, 8]
both_of_them = odd_numbers + even_numbers
# [1, 3, 5, 7, 2, 4, 6, 8]
```

> The `+` operator **joins two lists** into a new list. Original lists are unchanged.

## Repetition with `*`

```python
print([1, 2, 3] * 3)
# [1, 2, 3, 1, 2, 3, 1, 2, 3]
```

> The `*` operator **repeats the list contents** that many times.
> This creates a **new list** — the original is not modified.

> **Important:** `+` and `*` with lists create **new lists**. They do not modify
> the original lists in place. For in-place modification, use methods like
> `extend()` or `+=` (covered later).

---

## Summary Table

| Operator | Numbers | Strings | Lists |
|----------|---------|---------|-------|
| `+` | Add | Concatenate | Concatenate |
| `-` | Subtract | ❌ | ❌ |
| `*` | Multiply | Repeat | Repeat |
| `/` | Divide | ❌ | ❌ |
| `//` | Floor divide | ❌ | ❌ |
| `%` | Modulo | ❌ | ❌ |
| `**` | Power | ❌ | ❌ |

---

> **Next:** Comparison operators (`==`, `!=`, `<`, `>`, `<=`, `>=`) and
> logical operators (`and`, `or`, `not`) — these return **booleans** and
> are the foundation of control flow (`if` statements, loops).