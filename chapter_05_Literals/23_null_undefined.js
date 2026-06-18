// Null vs Undefined in JavaScript
// ================================

// 1. undefined
// ------------
// A variable that has been declared but not assigned any value.
// It is the default state given by JavaScript automatically.
// Think of it as: "Not yet defined."

let notAssigned;
console.log("Value of notAssigned:", notAssigned);           // undefined
console.log("Type of notAssigned:", typeof notAssigned);     // "undefined"

// Functions return undefined if no return statement is used
function greet() {
    console.log("Hello!");
}
let result = greet();
console.log("Function return value:", result);                // undefined

// Accessing a missing property returns undefined
let person = { name: "Alice" };
console.log("Missing property:", person.age);                 // undefined


// 2. null
// ---------
// A special value explicitly assigned by the developer.
// It indicates "no value" or "empty" intentionally.
// Think of it as: "Intentionally nothing."

let emptyValue = null;
console.log("Value of emptyValue:", emptyValue);              // null
console.log("Type of emptyValue:", typeof emptyValue);         // "object" (known quirk in JS)

// Use null when you want to clear or reset a variable deliberately
let user = "John";
user = null;  // Explicitly saying: "there is no user now"
console.log("User after reset:", user);                       // null


// 3. Key Differences at a Glance
// --------------------------------
// | Feature      | undefined                | null                     |
// |--------------|--------------------------|--------------------------|
// | Meaning      | Not assigned yet         | Intentionally empty      |
// | Set by       | JavaScript automatically | Developer explicitly     |
// | Type         | "undefined"              | "object"                 |
// | Equality (==)| undefined == null  → true| null == undefined → true |
// | Strict (===) | undefined === null → false| null === undefined → false|

console.log("undefined == null :", undefined == null);        // true (loose equality)
console.log("undefined === null:", undefined === null);       // false (strict equality)


// 4. Quick Check Examples
// ------------------------
let a;
let b = null;

console.log("\n--- Quick Check ---");
console.log("a:", a);                                         // undefined
console.log("b:", b);                                         // null
console.log("typeof a:", typeof a);                           // "undefined"
console.log("typeof b:", typeof b);                           // "object"

if (a === undefined) {
    console.log("Variable 'a' is undefined.");
}

if (b === null) {
    console.log("Variable 'b' is explicitly null.");
}

// Recommended: Use strict equality (===) to avoid confusion



let Audi = "";
console.log("typeof Audi:", typeof Audi); 
let age = 0;
console.log("typeof age:", typeof age);
