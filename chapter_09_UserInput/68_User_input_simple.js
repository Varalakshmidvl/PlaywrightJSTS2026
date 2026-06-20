const prompt = require("prompt-sync")();

let num = prompt("Enter a number: ");
num = Number(num);

if (num % 2 === 0) {
  console.log(num + " is Even");
} else {
  console.log(num + " is Odd");
}
