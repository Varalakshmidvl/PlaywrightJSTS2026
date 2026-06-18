# Chapter 5: Literals

This chapter covers JavaScript literals — the notations for representing fixed values in source code. It includes all number representations, strings, `null`, `undefined`, template literals, and best practices for choosing quote types.

---

## Files in This Chapter

| File | Description |
|------|-------------|
| `22_literals.js` | Basic literal declarations and types overview |
| `23_null_undefined.js` | Deep dive into `null` vs `undefined` |
| `24_null` | `null` examples with `typeof` and numeric prefixes |
| `26_Literals_Numbers_all.js` | All JavaScript number literals and special values |
| `27_String.js` | Single, double, and backtick string basics |
| `28_Template_literals` | Template literals with real-world use cases |
| `29_backtick_single_double.js` | Complete comparison of quote types and escaping |

---

## 22_literals.js

A quick overview of common JavaScript literals.

### What It Covers

- Strings, booleans, numbers
- `null` and `undefined`

### How to Run

```bash
node 22_literals.js
```

---

## 23_null_undefined.js

Comprehensive explanation of the difference between `null` and `undefined`.

### What It Covers

- `undefined`: default state for unassigned variables
- `null`: intentionally empty value set by the developer
- `typeof` behavior for both
- Loose (`==`) vs strict (`===`) equality

### Key Takeaway

| Feature | `undefined` | `null` |
|---------|-------------|--------|
| Meaning | Not assigned yet | Intentionally empty |
| Set by | JavaScript automatically | Developer explicitly |
| `typeof` | `"undefined"` | `"object"` |

### How to Run

```bash
node 23_null_undefined.js
```

---

## 24_null

Practical `null` examples and numeric literal prefixes.

### What It Covers

- `typeof` checks for `null`, `0`, and empty strings
- Hexadecimal (`0x`) and octal (`0o`) number prefixes

### How to Run

```bash
node 24_null
```

---

## 26_Literals_Numbers_all.js

Complete guide to every number literal type in JavaScript.

### What It Covers

- Integer and floating-point literals
- Binary (`0b`), octal (`0o`), and hexadecimal (`0x`) literals
- Exponential (scientific) notation
- Special values: `Infinity`, `NaN`
- `BigInt` for arbitrarily large integers
- Numeric separators (`1_000_000`) — ES2021+
- `Number` object constants (`MAX_VALUE`, `EPSILON`, etc.)

### How to Run

```bash
node 26_Literals_Numbers_all.js
```

---

## 27_String.js

Introduction to JavaScript string quotes.

### What It Covers

- Single quotes (`'`), double quotes (`"`), and backticks (`` ` ``)
- Note on JavaScript vs TypeScript quote conventions

### How to Run

```bash
node 27_String.js
```

---

## 28_Template_literals

Real-world template literal usage, especially useful for automation and API testing.

### What It Covers

- String interpolation with `${variable}`
- Dynamic API URL construction
- Playwright-style locator strings with variables
- Log formatting with template literals
- Dynamic screenshot filenames
- JSON payload building

### How to Run

```bash
node 28_Template_literals
```

---

## 29_backtick_single_double.js

Detailed comparison of the three ways to define strings in JavaScript.

### What It Covers

- When to use single vs double quotes
- Backtick advantages: interpolation, multiline, no escaping
- Escaping characters inside strings
- Expression evaluation inside backticks
- Tagged template literals (advanced)

### How to Run

```bash
node 29_backtick_single_double.js
```

---

## Summary

By the end of this chapter, you should be comfortable with:

- All numeric literal formats in JavaScript
- The critical difference between `null` and `undefined`
- Choosing the right string quote style for the situation
- Using template literals for dynamic strings in real-world scenarios

**Note:** Run each file with `node <filename>` to see the output and experiment by modifying the values.
