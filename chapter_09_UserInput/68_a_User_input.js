<!DOCTYPE html>
<html>
<head>
  <title>Even or Odd Checker</title>
</head>
<body>
  <script>
    let num = prompt("Enter a number:");
    num = Number(num);

    if (num % 2 === 0) {
      alert(num + " is Even");
    } else {
      alert(num + " is Odd");
    }
  </script>
</body>
</html>

//Save as html file and open in browser to get the user input and check if it is even or odd.