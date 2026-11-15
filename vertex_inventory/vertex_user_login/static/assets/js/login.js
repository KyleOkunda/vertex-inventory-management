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

    // Get csrf token from cookie
    var cookies = document.cookie.split("; ");
    var csrfToken = null;
    cookies.forEach((cookie) => {
      if (cookie.includes("csrftoken")) {
        csrfToken = cookie.split("=")[1];
      }
    });

    fetch("/login/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": csrfToken,
      },
      body: JSON.stringify({ email: email, password: password }),
    })
      .then((Response) => Response.json())
      .then((data) => {
        if (data.code == "EMAIL_AND_PASSWORD_REQUIRED") {
          alert(data.message || "Email and password are required.");
          loginButton.removeAttribute("disabled");
          return;
        } else if (data.code == "INVALID_CREDENTIALS") {
          alert(data.message);
          loginButton.removeAttribute("disabled");
          return;
        } else if (data.code == "USER_AUTH_ERROR") {
          alert(data.message);
          loginButton.removeAttribute("disabled");
          return;
        } else if (data.code == "LOGIN_SUCCESS") {
          alert(data.message);
          // window.location.href = "/dashboard/";
          return;
        }
      });
  });
});
