// Confusing Comparisons in JavaScript

// null and undefined
console.log(null == undefined); // true
console.log(null === undefined); // false
console.log(null == 0); // false
console.log(null >= 0); // true
console.log(undefined == 0); // false

console.log("--------");

// NaN is never equal to anything, even itself
console.log(NaN == NaN); // false
console.log(NaN === NaN); // false
console.log(Number.isNaN(NaN)); // true

console.log("--------");

// Empty array and string
console.log([] == ""); // true
console.log([] == 0); // true
console.log([] == false); // true
console.log([""] == ""); // true

console.log("--------");

// Empty object
console.log({} == "[object Object]"); // true
console.log({} == true); // false
console.log({} == false); // false

console.log("--------");

// String and number
console.log("5" == 5); // true
console.log("5" === 5); // false
console.log("" == 0); // true
console.log(" " == 0); // true
console.log(" \t\n" == 0); // true

console.log("--------");

// Booleans
console.log(true == "1"); // true
console.log(true == "true"); // false
console.log(false == "0"); // true
console.log(false == ""); // true

console.log("--------");

// Arrays
console.log([1,2] == "1,2"); // true
console.log([0] == false); // true
console.log([1] == true); // true
console.log([2] == true); // false

console.log("--------");

// typeof vs value
console.log(typeof null); // object
console.log(null instanceof Object); // false
console.log(typeof []); // object
console.log([] instanceof Array); // true
