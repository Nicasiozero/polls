function calculate(operation) {
    const num1 = parseFloat(document.getElementById("num1").value);
    const num2 = parseFloat(document.getElementById("num2").value);

    if (isNaN(num1) || isNaN(num2)) {
        document.getElementById("result").textContent = "Result: Invalid input";
        return;
    }

    let result;
    switch (operation) {
        case "add":
            result = num1 + num2;
            document.getElementById("result").style.color = "red";
            break;
        case "subtract":
            result = num1 - num2;
            document.getElementById("result").style.color = "green";
            break;
        case "multiply":
            result = num1 * num2;
            document.getElementById("result").style.color = "blue";
            break;
        case "divide":
            result = num2 !== 0 ? num1 / num2 : "Division by zero error";
            document.getElementById("result").style.color = "black";
            break;
        default:
            result = "Invalid operation";
    }

    document.getElementById("result").textContent = `Result: ${result}`;
    
}
