# Chapter 10: Loops

## Overview
This chapter covers all types of loops in JavaScript: `for`, `while`, `do-while`, `for...of`, `for...in`, and `forEach`. Loops help repeat code blocks efficiently.

## Files

| File | Description | Status |
|------|-------------|--------|
| `71_For_loop1.js` | Introduction to the need for loops | Completed |
| `72_For_loop2.js` | Basic for loop syntax and examples | Completed |
| `73_For_loop3.js` | Advanced for loop patterns | Completed |
| `74_IQ.js` | Loop-related interview questions | Completed |
| `75_For_OF_IN_Each.js` | for...of, for...in, and forEach comparisons | Completed |
| `76_While.js` | While loop with increment patterns | Completed |
| `77_Do_while.js` | Do-while loop basics | Completed |
| `78_Do_While.js` | Do-while loop practice | Completed |
| `79_IQ.js` | More loop interview questions | Completed |
| `80_IQ.js` | Loop logic puzzles | Completed |
| `81_IQ.js` | Advanced loop challenges | Completed |
| `82_IQ.js` | Loop optimization questions | Completed |

## What We Learned

### 71_For_loop1.js
- Understanding why loops are needed (avoiding repetitive code)
- Introduction to the `for` loop structure

### 76_While.js
- `while` loop syntax: initialization, condition, and updation
- Using while loops for retry logic and counting

```javascript
let attempt = 1;
while (attempt < 3) {
    console.log(attempt);
    attempt++;
}
```

## Key Takeaways
- `for` loop: best when you know the number of iterations
- `while` loop: best when the condition is dynamic
- `do...while` loop: executes at least once before checking condition
- `for...of`: iterates over values of iterable objects (arrays, strings)
- `for...in`: iterates over keys of an object
- `forEach`: array method for clean iteration
- Always ensure loops have a termination condition to avoid infinite loops

## How to Run
```bash
node chapter_10_Loops/71_For_loop1.js
node chapter_10_Loops/76_While.js
```

## Next Chapter
Chapter 11: Arrays
