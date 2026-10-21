# Python Lists

> **Lesson date:** 21/10/2026
> **Covers:** `list` — creation, indexing, iteration, errors
> **Code examples live in:** `Lists.py`

---

## Contents

| # | Topic | Jump |
|---|-------|------|
| 1 | What is a list? | [→ What is a List?](#1-what-is-a-list) |
| 2 | Creating lists | [→ Creating Lists](#2-creating-lists) |
| 3 | Accessing elements (indexing) | [→ Indexing](#3-accessing-elements-indexing) |
| 4 | Iterating with a for loop | [→ Iteration](#4-iterating-with-a-for-loop) |
| 5 | Index errors | [→ Index Errors](#5-index-errors) |

---

# 1. What is a List?

**A list is an ordered collection.** It can hold any type of value —
numbers, strings, booleans, even other lists. You can add as many
elements as you need. Think of it like a row of rooms, each with a
number starting at 0.

Lists are similar to arrays in other languages, but more flexible:
- Mixed types allowed: `[1, "hello", True, 3.14]`
- Dynamic size: append, remove, insert anytime
- Built-in methods for common operations

---

# 2. Creating Lists

## Empty list, then append

```python
mylist = []        # create an empty list
mylist.append(1)   # add 1 to the end
mylist.append(2)   # add 2 to the end
mylist.append(3)   # add 3 to the end
# mylist is now [1, 2, 3]
```

## Literal syntax (all at once)

```python
mylist = [1, 2, 3]
```

Both approaches produce the same result. The literal syntax is shorter
when you know the values upfront. `append()` is useful when building
a list step by step.

---

# 3. Accessing Elements (Indexing)

Indexes start at **0** — the first element is at index 0, second at 1,
third at 2, and so on.

```
  1   2   3
  0   1   2   ← indexes
```

```python
mylist = [1, 2, 3]
mylist[0]   # 1  → first element
mylist[1]   # 2  → second element
mylist[2]   # 3  → third element
```

> **Why start at 0?** Same reason as strings — it's a rule in
> programming. The index represents the *offset* from the start.
> Offset 0 means "no offset," i.e., the first item.

---

# 4. Iterating with a for Loop

To print or process every element without writing each index manually:

```python
mylist = [1, 2, 3]

for x in mylist:
    print(x)
```

**Output:**
```
1
2
3
```

> The loop variable `x` takes on each value in the list, one at a time.
> This works for any iterable — lists, strings, tuples, etc.

---

# 5. Index Errors

If you ask for an index that doesn't exist, Python raises an **IndexError**.

```python
list = [1, 2, 3]
print(list[3])  # IndexError: list index out of range
```

Valid indexes for a 3-element list are `0`, `1`, `2`. Index `3` is the
fourth position, which doesn't exist.

> **Tip:** Use `len(list)` to get the length. The last valid index is
> always `len(list) - 1`.

```python
mylist = [1, 2, 3]
len(mylist)        # 3
mylist[len(mylist) - 1]  # 3  → last element
```

> **Also:** Python supports **negative indexing** — `-1` is the last
> element, `-2` is second-to-last, etc.
> `mylist[-1]` → `3` (cleaner than `len()` trick)

---

## Common List Methods (Preview)

| Method | What it does |
|--------|--------------|
| `append(x)` | Add `x` to the end |
| `insert(i, x)` | Insert `x` at index `i` |
| `remove(x)` | Remove first occurrence of `x` |
| `pop(i)` | Remove and return element at index `i` (default: last) |
| `index(x)` | Return index of first `x` |
| `count(x)` | Count occurrences of `x` |
| `sort()` | Sort in place |
| `reverse()` | Reverse in place |
| `len(list)` | Built-in function — returns length |

> These will be covered in detail in the next documentation.

---

> **Note:** Lists are **mutable** — you can change their contents after
> creation. This is different from strings, which are immutable.