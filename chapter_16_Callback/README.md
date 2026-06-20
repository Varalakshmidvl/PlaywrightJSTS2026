# Chapter 16: Callbacks

## Overview
This chapter covers callback functions in JavaScript - synchronous and asynchronous callbacks, callback hell, and real-world usage in Playwright and general JavaScript.

## Files

| File | Description | Status |
|------|-------------|--------|
| `143_Callback.js` | Callback basics (placeholder) | Completed |
| `144_CB.js` | Callback introduction (placeholder) | Completed |
| `145_CB_Fn.js` | Callback functions (placeholder) | Completed |
| `146_PW_CB.js` | Playwright callback examples (placeholder) | Completed |
| `147_JS_CB.js` | JavaScript callback patterns (placeholder) | Completed |
| `148_Sync_CB.js` | Synchronous callbacks | Completed |
| `149_Async_CB.js` | Asynchronous callbacks | Completed |
| `150_CB_H.js` | Callback hell example | Completed |
| `151_CB_H_20_steps.js` | Deep callback hell (20 steps) | Completed |
| `152_CB_parameter.js` | Callbacks as parameters | Completed |
| `153_CB_Return.js` | Returning callbacks | Completed |

## What We Learned

### 148_Sync_CB.js
- Synchronous callbacks execute immediately within the function
- Common in array methods like `forEach`, `map`, `filter`

### 149_Async_CB.js
- Asynchronous callbacks execute after an operation completes
- Used in timers, file operations, and API calls

### 150_CB_H.js
- Callback hell (Pyramid of Doom) occurs with nested async callbacks
- Makes code hard to read and maintain
- Solved by Promises and async/await

## Key Takeaways
- A callback is a function passed as an argument to another function
- Synchronous callbacks execute immediately
- Asynchronous callbacks execute later, after an event/operation
- Callback hell can be avoided with:
  - Named functions instead of anonymous
  - Promises
  - Async/await syntax
- Playwright heavily uses callbacks in its event-driven architecture

## How to Run
```bash
node chapter_16_Callback/148_Sync_CB.js
node chapter_16_Callback/149_Async_CB.js
```

## Next Chapter
Chapter 17: Promise
