# Chapter 13: Strings

## Overview
This chapter covers JavaScript strings - creation, properties, searching, substring extraction, transformation, and common string methods.

## Files

| File | Description | Status |
|------|-------------|--------|
| `118_Strings.js` | String basics (placeholder) | Completed |
| `119_String_Properties.js` | String properties like length (placeholder) | Completed |
| `120_Search_check_str.js` | Searching within strings (placeholder) | Completed |
| `121_Substring.js` | Extracting substrings (placeholder) | Completed |
| `122_Transform_Str.js` | String transformation methods (placeholder) | Completed |
| `123_SC.js` | String case and comparison | Completed |
| `javascript_stringcheatsheet.md` | Quick reference cheat sheet for string methods | Completed |

## What We Learned

### String Basics
- Strings are primitive values in JavaScript
- Can be created with single quotes, double quotes, or backticks (template literals)
- Strings are immutable - methods return new strings

### Common String Methods
- `length` - number of characters
- `indexOf()` / `lastIndexOf()` - find position of substring
- `includes()` / `startsWith()` / `endsWith()` - check content
- `slice()` / `substring()` - extract portions
- `toUpperCase()` / `toLowerCase()` - change case
- `trim()` - remove whitespace
- `replace()` / `replaceAll()` - replace content
- `split()` - convert string to array

## Key Takeaways
- Strings are zero-indexed like arrays
- Template literals (backticks) allow interpolation: `` `Hello ${name}` ``
- Always check if a string method mutates or returns a new string
- `split()` and `join()` are powerful for string/array conversion
- Regular expressions provide advanced pattern matching

## How to Run
```bash
node chapter_13_Strings/123_SC.js
```

## Next Chapter
Chapter 14: Objects
