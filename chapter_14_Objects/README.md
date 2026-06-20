# Chapter 14: Objects

## Overview
This chapter covers JavaScript objects - creation, property access, methods, destructuring, spread operator, getters/setters, and the difference between primitive and reference types.

## Files

| File | Description | Status |
|------|-------------|--------|
| `124_Object.js` | Object basics and creation | Completed |
| `125_Objects2.js` | Object properties and reference types | Completed |
| `126_Objects_Creation.js` | Different ways to create objects | Completed |
| `127_Objects_Real.js` | Real-world object examples (config object) | Completed |
| `128_Primitive_Ref.js` | Primitive vs reference type comparison | Completed |
| `129_Ob_Examples.js` | Object usage examples | Completed |
| `130_IQ.js` | Object interview questions | Completed |
| `131_Object_Fn.js` | Object methods and functions | Completed |
| `132_Obj_decon.js` | Object destructuring | Completed |
| `133_Spead.js` | Spread operator with objects | Completed |
| `134_Objects_GET_SET_Methods.js` | Getter and setter methods | Completed |
| `135_IQ` | Object puzzles | Completed |
| `136_Obj_Real.js` | Real-world object patterns | Completed |
| `137_Let_Const_obj.ts` | Using let/const with objects (TypeScript) | Completed |

## What We Learned

### 124_Object.js
- Objects store data as key-value pairs
- Keys are strings (or Symbols), values can be any type
- JSON format uses quoted keys

```javascript
let obj1 = {
    name: "Pramod",
    age: 42,
    rollNo: 123
};
```

### 125_Objects2.js
- Objects are reference types
- Assigning an object to another variable copies the reference, not the value
- Modifying through one reference affects all references

```javascript
let a = { status: "pass" };
let b = a;
b.status = "fail";
console.log(a.status); // "fail" - same object!
```

### 127_Objects_Real.js
- Using objects for configuration
- Dynamic property addition and deletion
- Conditional logic based on object properties

```javascript
let config = {};
config.browser = "chrome";
config.timeout = 3000;
delete config.browser;
```

## Key Takeaways
- Objects are reference types - be careful with assignment and comparison
- Use dot notation (`obj.key`) when possible, bracket notation (`obj["key"]`) for dynamic keys
- `Object.keys()`, `Object.values()`, `Object.entries()` for iteration
- Destructuring extracts properties cleanly: `const { name, age } = person`
- Spread operator creates shallow copies: `const copy = { ...original }`
- Getters and setters control property access

## How to Run
```bash
node chapter_14_Objects/124_Object.js
node chapter_14_Objects/125_Objects2.js
node chapter_14_Objects/127_Objects_Real.js
```

## Next Chapter
Chapter 15: 2D Array
