# Chapter 4: JavaScript Concepts (Variables, Scope, Hoisting)

## Overview
This chapter covers variable declarations, scope rules, and hoisting behavior in JavaScript.

## Files

| File | Description | Status |
|------|-------------|--------|
| `09_var_let_const.js` | Introduction to var scope and function behavior | Completed |
| `09_var_more_examples.js` | Global vs local scope examples with comments | Completed |
| `10_functions.js` | Function declarations and expressions (placeholder) | Completed |
| `11_variables.js` | Variable scope deep dive (var) | Completed |
| `12_let.js` | let keyword and block scope (placeholder) | Completed |
| `13_const.js` | const keyword and immutability (placeholder) | Completed |
| `14_var_function_scope.js` | var function scope examples (placeholder) | Completed |
| `15_let_scope.js` | let block scope examples (placeholder) | Completed |
| `16_hosisting.js` | var hoisting explanation (placeholder) | Completed |
| `17_hoisting_fn.js` | Function hoisting (placeholder) | Completed |
| `18_let_hoisting.js` | let hoisting and TDZ (placeholder) | Completed |
| `19_let_hoisting_block.js` | let hoisting in block scope (placeholder) | Completed |
| `20_let_const.js` | let vs const comparison (placeholder) | Completed |

## What We Learned

### 09_var_let_const.js
- `var` is function-scoped (not block-scoped)
- Inside a function, `var` declarations are all in the same scope
- `var` can be redeclared within the same function
- Variables inside if blocks are not separate when using `var`

### 09_var_more_examples.js
Three scenarios demonstrated:
1. **Scenario 1**: `var` inside function and if block - all same scope
2. **Scenario 2**: `var` inside function shadows global variable
3. **Scenario 3**: Function without local `var` accesses global variable

```javascript
var a = 10; // Global scope
console.log(a); // 10

function printHello() {
    console.log("Hello Playwright Automation");
    console.log(a); // 10 (uses global, no local var declared)
}
printHello();
```

### 11_variables.js
- `var` is function-scoped (not block-scoped)
- `var` declared inside `if` block is still in the function scope
- This can lead to unexpected behavior if not understood

## Key Takeaways

### var
- Function-scoped (available throughout entire function)
- Can be redeclared
- Can be reassigned
- Hoisted to top of function (initialized as `undefined`)

### let
- Block-scoped (available only inside {} block)
- Cannot be redeclared in same scope
- Can be reassigned
- Hoisted but NOT initialized (Temporal Dead Zone)

### const
- Block-scoped (available only inside {} block)
- Cannot be redeclared
- Cannot be reassigned
- Hoisted but NOT initialized (Temporal Dead Zone)

### Hoisting
- `var` declarations are hoisted and initialized with `undefined`
- `let` and `const` declarations are hoisted but NOT initialized (TDZ)
- Function declarations are hoisted with their definition
- Function expressions are NOT hoisted (only variable is hoisted)

## How to Run
```bash
node chapter_04_JS_Concepts/09_var_let_const.js
node chapter_04_JS_Concepts/09_var_more_examples.js
node chapter_04_JS_Concepts/11_variables.js
```

## Next Chapter
Chapter 5: Data Types (Primitive vs Reference) - Coming soon

## Note on Placeholder Files
Several files in this chapter are currently empty placeholders ready for future learning sessions:
- `12_let.js`, `13_const.js`, `14_var_function_scope.js`, `15_let_scope.js`
- `16_hosisting.js`, `17_hoisting_fn.js`, `18_let_hoisting.js`
- `19_let_hoisting_block.js`, `20_let_const.js`, `10_functions.js`

These will be filled with examples as we progress through the topic.
