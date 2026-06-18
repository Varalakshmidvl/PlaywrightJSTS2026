// JavaScript String Quotes: Single ('), Double ("), and Backtick (`)
// ================================================================
// JavaScript allows three ways to define string literals.
// All three can create strings, but backticks (template literals) add extra power.


// 1. Single Quotes
// -----------------
let single = 'Hello, Playwright!';
console.log("Single quote:", single);     // Hello, Playwright!

// Works fine for simple text
let course = 'Playwright Automation';
console.log("Course:", course);           // Playwright Automation


// 2. Double Quotes
// -----------------
let double = "Hello, Playwright!";
console.log("Double quote:", double);     // Hello, Playwright!

// Useful when the string contains an apostrophe
let sentence = "It's a great day to learn JavaScript";
console.log("Sentence:", sentence);       // It's a great day to learn JavaScript

// Useful when the string contains quotes
let quote = 'He said, "JavaScript is fun!"';
console.log("Quote:", quote);             // He said, "JavaScript is fun!"


// 3. Backticks (Template Literals - ES6+)
// ----------------------------------------
let backtick = `Hello, Playwright!`;
console.log("Backtick:", backtick);       // Hello, Playwright!

// a) String Interpolation - embed variables/expressions directly
let firstName = "Rahul";
let lastName = "Sharma";
let fullName = `${firstName} ${lastName}`;
console.log("Full Name:", fullName);      // Rahul Sharma

let a = 10;
let b = 20;
console.log(`Sum of ${a} and ${b} is ${a + b}`);  // Sum of 10 and 20 is 30

// b) Multiline Strings without escape characters
let multiLine = `This is line 1
This is line 2
This is line 3`;
console.log("Multiline:");
console.log(multiLine);

// c) Backticks allow both single and double quotes inside easily
let mixed = `It's "awesome" to use backticks`;
console.log("Mixed quotes:", mixed);      // It's "awesome" to use backticks


// 4. Escaping Characters
// -----------------------
// When the same quote surrounds the string, you must escape inner quotes with \
let escapedSingle = 'It\'s a sunny day';
let escapedDouble = "He said, \"Hello!\"";
console.log("Escaped single:", escapedSingle);   // It's a sunny day
console.log("Escaped double:", escapedDouble);   // He said, "Hello!"

// With backticks, no escaping needed for ' or "
let noEscape = `It's "perfect" without escaping`;
console.log("No escape:", noEscape);      // It's "perfect" without escaping


// 5. Expression Evaluation Inside Backticks
// ------------------------------------------
let price = 150;
let quantity = 3;
console.log(`Total cost: $${price * quantity}`);   // Total cost: $450

let isAvailable = true;
console.log(`Status: ${isAvailable ? "In Stock" : "Out of Stock"}`);  // Status: In Stock


// 6. Tagged Template Literals (Advanced)
// ---------------------------------------
function highlight(strings, ...values) {
    return strings.reduce((result, str, i) => {
        let value = values[i] ? `**${values[i]}**` : '';
        return result + str + value;
    }, '');
}

let tool = "Playwright";
let language = "JavaScript";
console.log(highlight`We use ${tool} with ${language}`);
// We use **Playwright** with **JavaScript**


// 7. Key Differences Summary
// ---------------------------
console.log("\n--- Summary ---");
console.log("Single ('):   Good for simple text, no double quotes inside");
console.log("Double (\"):   Good for simple text, no single quotes inside");
console.log("Backtick (`): Supports interpolation, multiline, and both quote types");
