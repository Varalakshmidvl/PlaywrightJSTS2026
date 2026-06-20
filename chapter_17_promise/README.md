# Chapter 17: Promises

## Overview
This chapter covers JavaScript Promises - creation, chaining, handling API calls, error handling with catch/finally, Promise.all, and interview questions.

## Files

| File | Description | Status |
|------|-------------|--------|
| `154_Promise.js` | Promise basics (placeholder) | Completed |
| `155_Promise_REAL_API.js` | Real API calls with promises (placeholder) | Completed |
| `156_Promise_REAL_API_Part2.js` | Advanced API promise patterns (placeholder) | Completed |
| `157_Finally.js` | Using finally blocks | Completed |
| `158_Call_py_Problems.js` | Converting callback patterns to promises | Completed |
| `159_Promise_All.js` | Promise.all and parallel execution | Completed |
| `160_Promise_IQ.js` | Promise interview questions | Completed |

## What We Learned

### Promise States
- **Pending** - initial state
- **Fulfilled** - operation completed successfully
- **Rejected** - operation failed

### 157_Finally.js
- `.finally()` runs regardless of promise outcome
- Perfect for cleanup operations

```javascript
fetch('/api/data')
  .then(response => response.json())
  .catch(error => console.error(error))
  .finally(() => {
    console.log("Cleanup completed");
  });
```

### 159_Promise_All.js
- `Promise.all()` waits for all promises to resolve
- Fails fast if any promise rejects
- `Promise.allSettled()` waits for all regardless of outcome

## Key Takeaways
- Promises solve callback hell by enabling chaining with `.then()`
- Always handle errors with `.catch()`
- `.finally()` is great for cleanup (closing connections, hiding loaders)
- `Promise.all()` runs promises in parallel
- `Promise.race()` returns the first settled promise
- Async/await is syntactic sugar over promises

## How to Run
```bash
node chapter_17_promise/157_Finally.js
node chapter_17_promise/159_Promise_All.js
```

## Next Chapter
Chapter 18: Async Await
