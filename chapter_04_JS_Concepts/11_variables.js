var a = 10;// Global SCOPE
// var is function scoped
console.log(a);

function printHello() {
    console.log("Hello Playwright Automation");
    var a = 20; // Local Scope
    console.log(a);
    if (true) {
        var a = 50;
        console.log(a); // 30
    }

}

printHello();

