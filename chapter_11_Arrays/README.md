# Chapter 11: Arrays

## Overview
This chapter covers JavaScript arrays - creation, access, manipulation, searching, iteration, transformation, and common array methods.

## Files

| File | Description | Status |
|------|-------------|--------|
| `83_Arrays.js` | Array basics and creation | Completed |
| `84_Arrays.js` | Array fundamentals | Completed |
| `85_Access_Array.js` | Accessing array elements by index | Completed |
| `86_Arrays_Adding_Remove.js` | Adding and removing elements (push, pop, unshift, shift) | Completed |
| `87_Adding_Remove2.js` | More array manipulation examples | Completed |
| `88_Real_Example.js` | Real-world array examples | Completed |
| `89_Searching.js` | Searching in arrays (indexOf, includes, find) | Completed |
| `90_Iterate.js` | Iterating over arrays | Completed |
| `91_Transforms_Array.js` | Array transformation methods (map, filter, reduce) | Completed |
| `92_Array.js` | Array methods overview | Completed |
| `93_Array_Slicing.js` | Slicing and splicing arrays | Completed |
| `94_Contact_array.js` | Concatenating arrays | Completed |
| `95_Array_Checking.js` | Checking array properties and types | Completed |

## What We Learned

### 83_Arrays.js
- Creating empty and populated arrays
- Understanding zero-based indexing
- Arrays can hold mixed data types

```javascript
let fruits = [];
let fruits_fresh = ["apple", "banana", "cheery"];
let mixed = [1, "hello", true, null];
console.log(arr[0]); // First element
console.log(arr[3]); // Fourth element
console.log(arr[4]); // undefined (out of bounds)
```

### 86_Arrays_Adding_Remove.js
- `push()` / `pop()` - add/remove from end
- `unshift()` / `shift()` - add/remove from beginning

```javascript
let arr = [1, 2, 3];
arr.push(4);    // [1, 2, 3, 4]
arr.pop();      // [1, 2, 3]
arr.unshift(0); // [0, 1, 2, 3]
arr.shift();    // [1, 2, 3]
```

## Key Takeaways
- Arrays are ordered collections accessed by index (starting at 0)
- `push()`/`pop()` are efficient for end operations (O(1))
- `unshift()`/`shift()` are slower for large arrays (O(n))
- `map()`, `filter()`, `reduce()` are powerful for data transformation
- `slice()` creates a copy, `splice()` modifies the original
- `concat()` merges arrays without mutation

## How to Run
```bash
node chapter_11_Arrays/83_Arrays.js
node chapter_11_Arrays/86_Arrays_Adding_Remove.js
```

## Next Chapter
Chapter 12: Functions
