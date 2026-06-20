# Chapter 8: Switch Statement

## Overview
This chapter covers the `switch` statement in JavaScript, which provides a cleaner way to handle multiple conditions compared to long if-else chains.

## Files

| File | Description | Status |
|------|-------------|--------|
| `59_Switch.js` | Basic switch statement with days of the week | Completed |
| `60_No_Break.js` | Demonstrates fall-through behavior without break | Completed |
| `61_Default.js` | Using the default case in switch | Completed |
| `62_Real_Time_examples.js` | Real-world switch examples | Completed |
| `63_Switch_group.js` | Grouping multiple cases together | Completed |
| `64_IQ.js` | Interview questions on switch | Completed |
| `65_IQ2.js` | More switch interview questions | Completed |
| `66_IQ3.js` | Advanced switch scenarios | Completed |
| `67_IQ4.js` | Switch statement puzzles | Completed |

## What We Learned

### 59_Switch.js
- Basic switch syntax with `case` and `break`
- Using `default` for unmatched cases
- Each case can contain multiple statements

```javascript
let day = 5;
switch (day) {
    case 1:
        console.log('Mon');
        break;
    case 2:
        console.log('Tue');
        let a = 10;
        let b = 30;
        console.log(a + b);
        break;
    // ... more cases
    default:
        console.log("No idea which day it is");
}
```

## Key Takeaways
- `switch` compares a value against multiple `case` labels
- Always use `break` to prevent fall-through to the next case
- `default` handles values that don't match any case
- Multiple cases can be grouped to share the same code block
- Switch is often cleaner than long if-else chains for discrete values

## How to Run
```bash
node chapter_08_Switch_Statement/59_Switch.js
node chapter_08_Switch_Statement/62_Real_Time_examples.js
```

## Next Chapter
Chapter 9: User Input
