window.addEventListener("DOMContentLoaded", function () {
  var emailElement = document.getElementById("email");
  var passwordElement = document.getElementById("password");
  var loginButton = document.getElementById("login-button");

  loginButton.addEventListener("click", function (event) {
    loginButton.setAttribute("disabled", "");
    event.preventDefault();
    var email = emailElement.value;
    var password = passwordElement.value;

    if (!email || !password) {
      alert("Please enter both email and password.");
      loginButton.removeAttribute("disabled");
      return;
    }

    fetch("/login", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ email: email, password: password }),
    }).then(function (response) {
      if (response.ok) {
        window.location.href = "/dashboard";
      } else {
        response.json().then(function (data) {
          alert(data.message || "Login failed. Please try again.");
          loginButton.removeAttribute("disabled");
        });
      }
    });
  });
});
