 var a = 10; // Global scope
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
printHello();