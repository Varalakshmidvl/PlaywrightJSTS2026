# Chapter 2: JavaScript Concepts

## Overview
This chapter introduces fundamental JavaScript concepts including block scope, variable shadowing, and function execution.

## Files

| File | Description | Status |
|------|-------------|--------|
| `05_JSBasics.js` | Introduction to block scope with `let` | Completed |

## What We Learned

### 05_JSBasics.js
- `let` keyword creates block-scoped variables
- Variables declared with `let` inside a block (if/else) are separate from outer variables
- JavaScript has function scope (var) and block scope (let/const)
- Variable shadowing: inner variable can temporarily hide outer variable

### Example Flow
```javascript
function letExample2() {
    let x = 10;        // outer x
    if (true) {
        let x = 30;    // block-scoped x (different variable)
        console.log(x); // prints 30
    } else {
        console.log(x = 20); // prints 20
    }
}
letExample2();
```

## Key Takeaways
- `let` respects block boundaries (if, else, for, while)
- Outer `x` and inner `x` are two different variables
- This is the foundation for understanding modern JavaScript scoping

## How to Run
```bash
node chapter_02_JavaScript_Concepts/05_JSBasics.js
```

## Next Chapter
Chapter 3: Identifiers & Literals - Learn naming rules and conventions
