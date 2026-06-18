// JavaScript Number Literals - All Types & Representations
// ========================================================
// In JavaScript, there is ONLY ONE number type: 'number'.
// All numbers are stored as double-precision 64-bit binary format (IEEE 754).


// 1. Integer Literals
// --------------------
let decimal = 42;
let negative = -17;
let zero = 0;

console.log("Integer:", decimal);          // 42
console.log("Negative:", negative);        // -17
console.log("Zero:", zero);                // 0


// 2. Floating-Point Literals
// ---------------------------
let float1 = 3.14;
let float2 = 0.5;
let float3 = 2.0;      // Treated as integer 2 internally
let float4 = .75;      // Leading zero can be omitted

console.log("Float 3.14:", float1);        // 3.14
console.log("Float 0.5:", float2);         // 0.5
console.log("Float 2.0:", float3);         // 2
console.log("Float .75:", float4);         // 0.75


// 3. Binary Literals (Base 2) - Prefix: 0b or 0B
// ------------------------------------------------
let binary = 0b1010;   // 1*8 + 0*4 + 1*2 + 0*1 = 10
let binary2 = 0B1111;  // 15

console.log("Binary 0b1010:", binary);     // 10
console.log("Binary 0B1111:", binary2);    // 15


// 4. Octal Literals (Base 8) - Prefix: 0o or 0O
// -----------------------------------------------
let octal = 0o17;      // 1*8 + 7 = 15
let octal2 = 0O10;     // 8

console.log("Octal 0o17:", octal);         // 15
console.log("Octal 0O10:", octal2);        // 8


// 5. Hexadecimal Literals (Base 16) - Prefix: 0x or 0X
// ------------------------------------------------------
let hex = 0xFF;        // 255
let hex2 = 0x1A3;      // 1*256 + 10*16 + 3 = 419
let hex3 = 0Xabc;      // 2748

console.log("Hex 0xFF:", hex);             // 255
console.log("Hex 0x1A3:", hex2);           // 419
console.log("Hex 0Xabc:", hex3);           // 2748


// 6. Exponential (Scientific) Notation
// --------------------------------------
let exp1 = 1.5e3;      // 1.5 * 10^3 = 1500
let exp2 = 2e-3;       // 2 * 10^-3 = 0.002
let exp3 = 4E10;       // 4 * 10^10 = 40000000000
let exp4 = 6.022e23;   // Avogadro's number style

console.log("Exponential 1.5e3:", exp1);   // 1500
console.log("Exponential 2e-3:", exp2);    // 0.002
console.log("Exponential 4E10:", exp3);    // 40000000000
console.log("Exponential 6.022e23:", exp4);// 6.022e+23


// 7. Special Numeric Values
// --------------------------

// Infinity - Result of dividing by zero
let positiveInfinity = Infinity;
let negativeInfinity = -Infinity;
let divisionByZero = 1 / 0;

console.log("Infinity:", positiveInfinity);         // Infinity
console.log("-Infinity:", negativeInfinity);        // -Infinity
console.log("1 / 0:", divisionByZero);              // Infinity
console.log("-1 / 0:", -1 / 0);                     // -Infinity

// NaN (Not a Number) - Result of invalid numeric operations
let notANumber = NaN;
let invalidMath = 0 / 0;
let invalidParse = parseInt("not a number");

console.log("NaN:", notANumber);                    // NaN
console.log("0 / 0:", invalidMath);                 // NaN
console.log("parseInt('abc'):", invalidParse);      // NaN

// Important: NaN is the ONLY value not equal to itself
console.log("NaN === NaN:", NaN === NaN);           // false
console.log("isNaN('hello'):", isNaN("hello"));     // true
console.log("Number.isNaN('hello'):", Number.isNaN("hello")); // false


// 8. BigInt (Arbitrarily Large Integers) - Separate Type
// --------------------------------------------------------
// Used for integers larger than Number.MAX_SAFE_INTEGER
let bigIntLiteral = 123456789012345678901234567890n;
let bigFromNumber = BigInt(9007199254740991);

console.log("BigInt:", bigIntLiteral);              // 123456789012345678901234567890n
console.log("typeof BigInt:", typeof bigIntLiteral);// "bigint"
console.log("BigInt from Number:", bigFromNumber);  // 9007199254740991n


// 9. Number Object Properties
// ----------------------------
console.log("\n--- Number Constants ---");
console.log("Number.MAX_VALUE:", Number.MAX_VALUE);           // ~1.79e+308
console.log("Number.MIN_VALUE:", Number.MIN_VALUE);           // ~5e-324
console.log("Number.MAX_SAFE_INTEGER:", Number.MAX_SAFE_INTEGER); // 9007199254740991
console.log("Number.MIN_SAFE_INTEGER:", Number.MIN_SAFE_INTEGER); // -9007199254740991
console.log("Number.POSITIVE_INFINITY:", Number.POSITIVE_INFINITY); // Infinity
console.log("Number.NEGATIVE_INFINITY:", Number.NEGATIVE_INFINITY); // -Infinity
console.log("Number.EPSILON:", Number.EPSILON);               // ~2.22e-16
console.log("Number.NaN:", Number.NaN);                       // NaN


// 10. Underscores as Numeric Separators (ES2021+)
// -------------------------------------------------
let million = 1_000_000;
let creditCard = 1234_5678_9012_3456;
let binaryGrouped = 0b1010_1111;
let hexGrouped = 0xFF_FF;

console.log("\n--- Numeric Separators ---");
console.log("1_000_000:", million);                 // 1000000
console.log("Credit card grouping:", creditCard);   // 1234567890123456
console.log("Binary grouped:", binaryGrouped);      // 175
console.log("Hex grouped:", hexGrouped);            // 65535


// 11. typeof Check
// -----------------
console.log("\n--- typeof Checks ---");
console.log("typeof 42:", typeof 42);                // "number"
console.log("typeof 3.14:", typeof 3.14);            // "number"
console.log("typeof Infinity:", typeof Infinity);   // "number"
console.log("typeof NaN:", typeof NaN);              // "number" (quirk!)
console.log("typeof 10n:", typeof 10n);              // "bigint"
