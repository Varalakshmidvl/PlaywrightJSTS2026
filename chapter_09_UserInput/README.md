# Chapter 9: User Input

## Overview
This chapter covers different ways to accept user input in JavaScript, including using the `prompt-sync` library and Node.js `readline` module.

## Files

| File | Description | Status |
|------|-------------|--------|
| `68_User_Input.js` | User input basics | Completed |
| `68_User_input_simple.js` | Simple user input with prompt-sync (even/odd checker) | Completed |
| `68_a_User_input.js` | Additional input examples | Completed |
| `69_Node_readline.js` | Using Node.js readline for input | Completed |
| `70_Prompt_sync` | Prompt sync examples | Completed |

## What We Learned

### 68_User_input_simple.js
- Using `prompt-sync` npm package for synchronous user input
- Converting string input to numbers with `Number()`
- Building interactive command-line programs

```javascript
const prompt = require("prompt-sync")();

let num = prompt("Enter a number: ");
num = Number(num);

if (num % 2 === 0) {
  console.log(num + " is Even");
} else {
  console.log(num + " is Odd");
}
```

## Key Takeaways
- `prompt-sync` is a simple way to get user input in Node.js
- User input is always returned as a string - convert with `Number()`, `parseInt()`, etc.
- `readline` module provides a more robust built-in alternative
- Always validate user input before processing

## Prerequisites
```bash
npm install prompt-sync
```

## How to Run
```bash
node chapter_09_UserInput/68_User_input_simple.js
```

## Next Chapter
Chapter 10: Loops
