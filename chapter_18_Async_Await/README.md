# Chapter 18: Async Await

## Overview
This chapter covers `async/await` syntax in JavaScript - writing asynchronous code that looks synchronous, error handling with try/catch/finally, sequential vs parallel execution, and Playwright integration.

## Files

| File | Description | Status |
|------|-------------|--------|
| `161_Async.js` | Async/await basics with error handling | Completed |
| `162_Async_p2.js` | Async/await part 2 | Completed |
| `163_PyoDom_P2.js` | Async patterns and DOM manipulation | Completed |
| `164_Async_Ex.js` | Async/await exercises | Completed |
| `165_AA_Parallel.js` | Parallel execution with Promise.allSettled | Completed |
| `165_AA_Seq.js` | Sequential async execution | Completed |
| `166_IQ.js` | Async/await interview questions | Completed |
| `167_ACLogin.js` | Playwright test example using async/await | Completed |

## What We Learned

### 161_Async.js
- `async` functions always return a Promise
- `await` pauses execution until the Promise resolves
- `try/catch/finally` for robust error handling

```javascript
async function testapi() {
    try {
        let result = await Promise.reject("503 reject");
    }
    catch (error) {
        console.log('Error', error);
    }
    finally {
        console.log("Clean up!!");
    }
}
testapi();
```

### 165_AA_Parallel.js
- Running multiple async operations in parallel
- Using `Promise.allSettled()` to wait for all results

```javascript
async function parallelTest() {
    let [r1, r2, r3] = await Promise.allSettled([
        apiCall("Auth Service"),
        apiCall("User Account Creation"),
        apiCall("Support Page API")
    ]);
    console.log(r1, r2, r3);
}
```

### 167_ACLogin.js
- Real Playwright test using async/await
- Page navigation and assertions

```javascript
import { test, expect } from '@playwright/test';

test('has title', async ({ page }) => {
    await page.goto('https://playwright.dev/');
    await expect(page).toHaveTitle(/Playwright/);
});
```

## Key Takeaways
- `async/await` makes asynchronous code readable and maintainable
- Always wrap `await` calls in `try/catch` for error handling
- Use `Promise.all()` for parallel independent operations
- Use sequential `await` when operations depend on each other
- Playwright tests are fully async - every action uses `await`

## How to Run
```bash
node chapter_18_Async_Await/161_Async.js
node chapter_18_Async_Await/165_AA_Parallel.js
npx playwright test chapter_18_Async_Await/167_ACLogin.js
```

## Next Chapter
Chapter 19: Playwright Basics
