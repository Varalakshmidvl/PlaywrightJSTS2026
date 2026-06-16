/* var a = 10; // Global scope
console.log(a);

function printHello() {
    console.log("Hello Playwright Automation");
    var a = 20; // Local scope (function-scoped)
    console.log(a);
    if (true) {
        var a = 30; // Same local scope (function-scoped)
        console.log(a);
    }
}
printHello(); */

/* 
var a = 10;
console.log(a); // 10

function printHello() {
    var a = 50; // Local scope
    console.log("Hello Playwright Automation");
    console.log(a); // 50
}

printHello();
 */
var a = 10;
console.log(a); // 10

function printHello() {
    console.log("Hello Playwright Automation");
    console.log(a); // 10 (uses global, since no local var declared)
}

printHello();

