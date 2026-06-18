# Chapter 6: Operators

This chapter covers all major JavaScript operators — from basic arithmetic and assignment to comparison, logical, ternary, increment/decrement, and the nullish coalescing operator.

---

## Files in This Chapter

| File | Description |
|------|-------------|
| `30_Operator.js` | Assignment operator basics |
| `31_Arithemetic.js` | Arithmetic operators (`+`, `-`, `*`, `/`) |
| `32_Modules.js` | Modulo (`%`) operator and even/odd checks |
| `33_Expo_OP.js` | Exponentiation (`**`) operator |
| `34_IQ.js` | Addition assignment (`+=`) shorthand |
| `35_Comparios_Os.js` | Comparison operators (`>`, `<`, `>=`, `<=`, `==`, `===`, `!=`, `!==`) |
| `36_Comparision_Strict_loose.js` | Strict (`===`) vs loose (`==`) equality |
| `37_IQ_loose_strict.js` | Loose equality edge case (`0 == ""`) |
| `38_confusing_comparision.js` | Tricky comparison scenarios in JavaScript |
| `39_Logical_OS.js` | Logical operators (`&&`, `\|\|`, `!`) |
| `40_String_Con_op.js` | String concatenation with `+=` |
| `41_Ternary_op.js` | Ternary (`?:`) operator with real-world examples |
| `42_Type_OS.js` | `typeof` operator |
| `43_Incre_decre_os.js` | Pre and post decrement operators |
| `44_Null_Os.js` | Nullish coalescing (`??`) operator |
| `45_Post_increment.js` | Post-increment (`a++`) behavior |
| `46_IQ_Increment.js` | Increment operator practice |
| `47_Advanced_ID.js` | Advanced increment/decrement expressions |

---

## 30_Operator.js

Basic assignment operator demonstration.

### What It Covers

- Reassigning a variable multiple times
- Final value after sequential assignments

### How to Run

```bash
node 30_Operator.js
```

---

## 31_Arithemetic.js

Fundamental arithmetic operations in JavaScript.

### What It Covers

- Addition (`+`)
- Subtraction (`-`)
- Multiplication (`*`)
- Division (`/`)

### How to Run

```bash
node 31_Arithemetic.js
```

---

## 32_Modules.js

The modulo (`%`) operator and its practical use.

### What It Covers

- Remainder after division
- Checking even/odd numbers (`n % 2`)

### How to Run

```bash
node 32_Modules.js
```

---

## 33_Expo_OP.js

Exponentiation using the `**` operator.

### What It Covers

- `2 ** 3` equals `8`
- Variable-based exponentiation

### How to Run

```bash
node 33_Expo_OP.js
```

---

## 34_IQ.js

Compound assignment operator (`+=`).

### What It Covers

- `x += 10` is shorthand for `x = x + 10`

### How to Run

```bash
node 34_IQ.js
```

---

## 35_Comparios_Os.js

Overview of all comparison operators.

### What It Covers

- Relational: `>`, `<`, `>=`, `<=`
- Loose equality: `==`, `!=`
- Strict equality: `===`, `!==`

### How to Run

```bash
node 35_Comparios_Os.js
```

---

## 36_Comparision_Strict_loose.js

The critical difference between strict and loose equality.

### What It Covers

- `10 == "10"` → `true` (loose, type coercion)
- `10 === "10"` → `false` (strict, no coercion)
- Boolean coercion edge cases (`0 == false`, `1 == true`)

### Key Takeaway

> Always prefer `===` and `!==` to avoid unexpected type coercion.

### How to Run

```bash
node 36_Comparision_Strict_loose.js
```

---

## 37_IQ_loose_strict.js

A quick loose equality edge case.

### What It Covers

- `0 == ""` evaluates to `true` due to type coercion

### How to Run

```bash
node 37_IQ_loose_strict.js
```

---

## 38_confusing_comparision.js

Tricky comparison scenarios every JavaScript developer should know.

### What It Covers

- `null` vs `undefined` comparisons
- `NaN` is never equal to anything, even itself
- Empty arrays/strings coercing to `0` or `false`
- Object-to-primitive comparisons
- Whitespace strings coercing to `0`

### How to Run

```bash
node 38_confusing_comparision.js
```

---

## 39_Logical_OS.js

Logical operators for boolean logic.

### What It Covers

- AND (`&&`)
- OR (`||`)
- NOT (`!`)

### How to Run

```bash
node 39_Logical_OS.js
```

---

## 40_String_Con_op.js

String concatenation using `+=`.

### What It Covers

- Building strings incrementally

### How to Run

```bash
node 40_String_Con_op.js
```

---

## 41_Ternary_op.js

The conditional (ternary) operator with practical automation examples.

### What It Covers

- Basic ternary syntax: `condition ? valueIfTrue : valueIfFalse`
- Test result evaluation (PASS/FAIL)
- Environment-based URL selection
- Browser mode selection (`headless` vs `headed`)
- SLA status checks
- Nested ternary operators
- HTTP status code categorization
- Temperature classification

### How to Run

```bash
node 41_Ternary_op.js
```

---

## 42_Type_OS.js

Using the `typeof` operator.

### What It Covers

- `typeof` for strings, numbers, arrays
- Key quirks: arrays return `"object"`, `null` returns `"object"`

### How to Run

```bash
node 42_Type_OS.js
```

---

## 43_Incre_decre_os.js

Pre-decrement and post-decrement operators.

### What It Covers

- Pre-decrement (`--a`): decrease then assign
- Post-decrement (`a--`): assign then decrease

### How to Run

```bash
node 43_Incre_decre_os.js
```

---

## 44_Null_Os.js

Nullish coalescing (`??`) and `null` comparison quirks.

### What It Covers

- `null >= 0` evaluates to `true`
- `??` provides a fallback only for `null` or `undefined`

### How to Run

```bash
node 44_Null_Os.js
```

---

## 45_Post_increment.js

Post-increment (`a++`) behavior.

### What It Covers

- `b = a++` assigns the original value, then increments `a`

### How to Run

```bash
node 45_Post_increment.js
```

---

## 46_IQ_Increment.js

Practice with post-increment.

### What It Covers

- `result = a++` behavior
- Final values of both variables

### How to Run

```bash
node 46_IQ_Increment.js
```

---

## 47_Advanced_ID.js

Complex increment/decrement expressions.

### What It Covers

- `a++ + ++a` combined expressions
- Understanding intermediate values step by step

### How to Run

```bash
node 47_Advanced_ID.js
```

---

## Summary

By the end of this chapter, you should be confident with:

- All arithmetic and assignment operators
- When to use strict (`===`) vs loose (`==`) equality
- Logical operators and boolean logic
- Increment/decrement nuances (pre vs post)
- Ternary operators for concise conditionals
- `typeof` and the nullish coalescing (`??`) operator

**Note:** Run each file with `node <filename>` to see the output and experiment by modifying the values.
