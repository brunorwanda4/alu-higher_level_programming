# Everything Is an Object: What Python Variables Really Hold

![Python object identity, aliasing, and immutable rebinding](python-objects-cover.png)

## Introduction

When I started learning Python, I imagined a variable as a box. If I wrote `score = 10`, I thought Python created a box called `score` and placed the number `10` inside it. That explanation was useful at first, but it stopped making sense when I began working with lists, copies, and functions. Why did changing one list sometimes change another one? Why did the same thing not happen with integers?

The answer is one of Python's most important ideas: everything is an object. A variable is not a box containing an object. It is a name that refers to an object. Every object has a type, a value, and an identity. Once I understood that, many results that had seemed strange became predictable.

## Identity, type, and the difference between `==` and `is`

Python gives us two useful built-in functions for inspecting objects. `type()` tells us what kind of object we are working with, while `id()` gives us an integer that uniquely identifies that object during its lifetime. In CPython, the value returned by `id()` represents the object's memory address. Other Python implementations are allowed to handle identity differently.

Here is a simple example:

```python
a = [1, 2, 3]
b = [1, 2, 3]

print(type(a))          # <class 'list'>
print(a == b)           # True
print(a is b)           # False
print(id(a) == id(b))   # False
```

At first, seeing both `True` and `False` here can be confusing. The expression `a == b` asks whether the two lists have the same value. They do. The expression `a is b` asks whether both names point to the exact same object. They do not.

Assignment is also important. Writing `b = a` does not automatically copy the object. It simply makes `b` refer to the same object as `a`. This is the difference between assignment and copying a value.

```python
a = [1, 2, 3]
b = a

print(a == b)  # True
print(a is b)  # True
```

In memory, the relationship can be pictured like this:

```text
a ─────┐
       ├────> list object [1, 2, 3] at identity 0x100
b ─────┘
```

The names `a` and `b` are aliases. There is only one list, but there are two ways to reach it.

## Mutable objects

A mutable object is an object whose contents can change after it has been created. Python's common mutable built-in types include:

- `list`
- `dict`
- `set`
- `bytearray`

Lists make mutability easy to see:

```python
scores = [10, 20]
other_name = scores
old_id = id(scores)

other_name.append(30)

print(scores)                 # [10, 20, 30]
print(other_name)             # [10, 20, 30]
print(id(scores) == old_id)   # True
```

I only called `append()` through `other_name`, yet `scores` also appears to change. In reality, neither variable contains its own list. Both names refer to one shared list, and that list was changed in place. Its identity stayed the same.

```text
Before:

scores ──────┐
             ├────> [10, 20]       identity 0x200
other_name ──┘

After other_name.append(30):

scores ──────┐
             ├────> [10, 20, 30]   identity 0x200
other_name ──┘
```

This behavior is called aliasing. It can be useful when two parts of a program are intentionally sharing data, but it can also cause bugs when we expect one variable to have an independent copy.

To create a shallow copy of a list, I can use slicing, `copy()`, or the `list()` constructor:

```python
original = [1, 2, 3]
copied = original[:]

copied.append(4)

print(original)            # [1, 2, 3]
print(copied)              # [1, 2, 3, 4]
print(copied == original)  # False
print(copied is original)  # False
```

Now there are two separate list objects, so changing one does not change the other.

## Immutable objects

An immutable object cannot have its value changed after it is created. Python's main immutable built-in types are:

- numbers: `int`, `float`, and `complex`
- `str`
- `tuple`
- `frozenset`
- `bytes`

Consider what happens when an integer is incremented:

```python
n = 1
old_id = id(n)
n += 1

print(n)               # 2
print(id(n) == old_id) # False in the usual CPython case
```

Python did not change the integer object `1` into `2`. Integers are immutable, so Python made `n` refer to a different integer object. The old object remained unchanged.

```text
Before:
n ─────> integer object 1   identity 0x300

After n += 1:
n ─────> integer object 2   identity 0x320

The integer object 1 was never modified.
```

Strings behave in the same general way:

```python
message = "Hello"
old_id = id(message)
message += " Python"

print(message)                 # Hello Python
print(id(message) == old_id)   # False
```

The text looks as if it was extended, but a new string was created and `message` was rebound to it.

There is an interesting detail with tuples and frozen sets. A tuple is immutable because its references cannot be replaced, but an object stored inside a tuple may itself be mutable.

```python
data = ([1, 2], "unchanged")
data[0].append(3)

print(data)  # ([1, 2, 3], 'unchanged')
```

The tuple still points to the same list, so the tuple itself was not changed. The list inside it was changed. A `frozenset` is also immutable, but its elements must be hashable. For that reason, ordinary lists, dictionaries, and sets cannot be direct elements of a `frozenset`. A custom hashable object could still contain mutable internal data, although changing anything used to calculate its hash would be unsafe.

## Why the difference matters

Mutability matters because it decides whether an operation updates an existing object or makes a name refer to a new one. A good example is the difference between `+=` and `+` with lists:

```python
a = [1, 2, 3]
b = a

a += [4]

print(a)       # [1, 2, 3, 4]
print(b)       # [1, 2, 3, 4]
print(a is b)  # True
```

For a list, `+=` normally changes the existing object. Since `a` and `b` are aliases, both names still show the updated list.

Now compare that with this:

```python
a = [1, 2, 3]
b = a

a = a + [4]

print(a)       # [1, 2, 3, 4]
print(b)       # [1, 2, 3]
print(a is b)  # False
```

This time, `a + [4]` created a new list and assignment rebound only `a`. The name `b` continued to refer to the original list.

Mutability also matters when we choose dictionary keys or set elements. Those objects need a stable hash value, which is why mutable containers such as lists and dictionaries cannot be used as dictionary keys. The same idea matters when designing functions, sharing application state, caching data, and deciding whether to make a copy before changing something.

CPython has another interesting object-related optimization: small integer pre-allocation. When CPython starts, it creates 262 commonly used integer objects, covering the range from `-5` to `256` inclusive. These ranges have historically been described in the CPython source using `NSMALLNEGINTS` for the five negative integers and `NSMALLPOSINTS` for the 257 non-negative integers. In newer source code, the names may have an internal prefix.

These particular integers are reused because small numbers appear constantly as indexes, counters, lengths, return values, and status codes. Reusing the objects avoids repeatedly allocating the most common integer values.

```python
a = 89
b = 89

print(a == b)  # True
print(a is b)  # Commonly True in CPython
```

This does not mean we should compare numbers using `is`. Integer caching and other identity optimizations are implementation details. I use `==` when comparing values and `is` when I genuinely care about identity, especially in checks such as `value is None`.

## What happens when objects are passed to functions?

Python passes arguments by assignment, a model that is also called call-by-sharing. When I pass an object to a function, the function's parameter becomes another name for that object.

If the object is mutable and the function changes it in place, the caller can see the change:

```python
def add_item(items):
    items.append(4)


numbers = [1, 2, 3]
add_item(numbers)

print(numbers)  # [1, 2, 3, 4]
```

While `add_item()` is running, `items` and `numbers` are aliases for the same list. The function changes that shared object.

However, assigning a different object to the parameter only changes the local name:

```python
def replace_list(items):
    items = [9, 9, 9]


numbers = [1, 2, 3]
replace_list(numbers)

print(numbers)  # [1, 2, 3]
```

The new list is assigned to the local parameter `items`. The caller's name `numbers` is not rebound, so it still points to the original list.

Immutable objects follow exactly the same argument-passing rule:

```python
def increment(value):
    value += 1
    print(value)  # 2


number = 1
increment(number)

print(number)  # 1
```

Because an integer cannot be modified in place, `value += 1` makes the local name `value` refer to the integer `2`. The name `number` outside the function still refers to `1`.

## Final thoughts

The biggest lesson I took from this project is that Python is consistent once I think in terms of objects and references. Assignment binds a name to an object. Aliases share the same object. Mutable objects can change in place, while operations on immutable objects create or select another object and rebind a name. Function arguments follow those same rules.

Understanding this has made me more careful when copying lists, passing data to functions, comparing objects, and choosing between mutating an object and creating a new one. More importantly, results that once looked like Python tricks now make sense.

## Publication links

- Blog post: add the Medium or LinkedIn article URL after publishing.
- LinkedIn share: add the LinkedIn post URL after sharing.
