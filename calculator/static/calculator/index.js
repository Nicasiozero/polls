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


function serverCalculate() {
    const num1 = document.getElementById("num1").value;
    const num2 = document.getElementById("num2").value;
    let operation = prompt("Enter operation (+, -, *, /)");

    if (num1 && num2 && operation) {
        fetch('/calculate/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-CSRFToken': getCookie('csrftoken')  // CSRF Token
            },
            body: `num1=${num1}&num2=${num2}&operation=${operation}`
        })
        .then(response => response.json())
        .then(data => {
            document.getElementById("result").innerText = `Result: ${data.result}`;
        })
        .catch(error => {
            console.error('Error:', error);
        });
    } else {
        alert("Please enter valid inputs.");
    }
}

// Helper function to get CSRF token (needed for Django security)
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}