# Chapter 15: 2D Array

## Overview
This chapter covers two-dimensional arrays in JavaScript - creation, access, nested iteration, and real-world applications like test matrices.

## Files

| File | Description | Status |
|------|-------------|--------|
| `138_2D_Array.js` | 2D array basics and nested loops | Completed |
| `139_2d.js` | 2D array practice | Completed |
| `140_REAL.js` | Real-world 2D array - test matrix example | Completed |
| `141_2d_Array_Fn.js` | Functions with 2D arrays | Completed |
| `142_IQ_Right_Pattern_Py.js` | Pattern problems with 2D arrays | Completed |

## What We Learned

### 138_2D_Array.js
- 2D arrays are arrays of arrays
- Access elements with double indexing: `grid[row][col]`
- Nested loops iterate through rows and columns

```javascript
let rakesh_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
];

for (let i = 0; i < 3; i++) {
    for (let j = 0; j < 3; j++) {
        console.log(rakesh_grid[i][j]);
    }
}
```

### 140_REAL.js
- Real-world application: test result matrix
- Different iteration styles: classic for, for...of, forEach

```javascript
let testMatrix = [
    ["login", "pass", 200],
    ["checkout", "fail", 404],
    ["search", "pass", 180]
];

testMatrix.forEach(row => {
    row.forEach(cell => process.stdout.write(cell + " "));
    console.log();
});
```

## Key Takeaways
- 2D arrays represent grids, tables, and matrices
- `array.length` gives number of rows
- `array[row].length` gives number of columns in that row
- Jagged arrays (rows of different lengths) are allowed in JavaScript
- Nested `forEach` provides clean functional iteration
- 2D arrays are essential for game boards, spreadsheets, and test data

## How to Run
```bash
node chapter_15_2D_Array/138_2D_Array.js
node chapter_15_2D_Array/140_REAL.js
```

## Next Chapter
Chapter 16: Callback
