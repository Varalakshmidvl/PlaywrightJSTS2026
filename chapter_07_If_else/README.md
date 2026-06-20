# Chapter 7: If-Else Statements

## Overview
This chapter covers conditional logic using `if`, `else if`, and `else` statements in JavaScript. We explore how to make decisions in code based on different conditions, with real-world examples and interview questions.

## Files

| File | Description | Status |
|------|-------------|--------|
| `48_if_Else.js` | Basic if-else example with age check | Completed |
| `49_if_Elseif_else.js` | Multiple conditions with else-if | Completed |
| `50_Real_If_else.js` | Real-world if-else scenarios | Completed |
| `51_API_if_else.js` | API-related conditional examples | Completed |
| `52_IQ_if_else.js` | Interview questions on if-else | Completed |
| `53_IF_Else_real.js` | Login validation with logical operators | Completed |
| `54_IQ.js` | More interview questions | Completed |
| `55_IE.js` | If-else practice exercises | Completed |
| `56_IQ_EVEN_ODD.js` | Even/odd check logic | Completed |
| `57_Grade_Calc.js` | Grade calculator using if-else | Completed |
| `58_Leap_Year.js` | Leap year checker | Completed |

## What We Learned

### 48_if_Else.js
- Basic syntax of `if` and `else`
- Checking conditions with comparison operators

```javascript
let age = 20;
if (age > 18) {
    console.log("You are allowed to vote!");
} else {
    console.log("You are not allowed to vote!");
}
```

### 53_IF_Else_real.js
- Combining multiple conditions with logical operators (`&&`, `||`)
- Real-world login validation example

```javascript
let username = "Dev";
let password = "secure123";
let isAccountLocked = true;

if ((username === "Dev" && password === "secure123") && isAccountLocked) {
    console.log("Allowed to enter");
} else {
    console.log("Not allowed to enter");
}
```

## Key Takeaways
- `if` statements execute code when a condition is `true`
- `else` provides an alternative path when the condition is `false`
- `else if` allows checking multiple conditions in sequence
- Logical operators (`&&`, `||`, `!`) combine multiple conditions
- Comparison operators (`>`, `<`, `===`, `!==`, etc.) evaluate expressions

## How to Run
```bash
node chapter_07_If_else/48_if_Else.js
node chapter_07_If_else/53_IF_Else_real.js
```

## Next Chapter
Chapter 8: Switch Statement
