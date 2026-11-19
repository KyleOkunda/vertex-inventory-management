window.addEventListener("DOMContentLoaded", function () {
  var firstNameElement = document.getElementById("first-name");
  var lastNameElement = document.getElementById("last-name");
  var phoneNumberElement = document.getElementById("phone-number");
  var staffEmailElement = document.getElementById("staff-email");
  var userRoleElement = document.getElementById("user-role");
  var departmentElement = document.getElementById("department");
  var temporaryPasswordElement = document.getElementById("temporary-password");
  var showTempPasswordBtn = document.getElementById("show-temporary-password");
  var confirmTempPasswordElement = document.getElementById(
    "confirm-temporary-password",
  );
  var showConfirmPasswordBtn = document.getElementById(
    "show-confirm-temporary-password",
  );
  var passwordMessageElement = document.getElementById("password-message");
  var cardFirstNameInit = document.getElementById("first-name-letter");
  var cardLastNameInit = document.getElementById("last-name-letter");
  var cardUserRole = document.getElementById("user-card-role");
  var cardUserFName = document.getElementById("user-card-fname");
  var cardUserLName = document.getElementById("user-card-lname");
  var cardDepartment = document.getElementById("user-card-dept");
  var cardPhoneNumber = document.getElementById("user-card-phone");
  var cardEmail = document.getElementById("user-card-email");
  var resetFormBtn = document.getElementById("reset-form-btn");
  var createUserBtn = document.getElementById("create-user-btn");

  // Show password
  showTempPasswordBtn.addEventListener("click", () => {
    let inputElement = showTempPasswordBtn.parentElement.children[1];
    let type = inputElement.getAttribute("type");

    if (type === "text") {
      inputElement.setAttribute("type", "password");
    } else if (type === "password") {
      inputElement.setAttribute("type", "text");
    }
  });
  showConfirmPasswordBtn.addEventListener("click", () => {
    let inputElement = showConfirmPasswordBtn.parentElement.children[1];
    let type = inputElement.getAttribute("type");

    if (type === "text") {
      inputElement.setAttribute("type", "password");
    } else if (type === "password") {
      inputElement.setAttribute("type", "text");
    }
  });

  // Populate preview card
  firstNameElement.addEventListener("input", () => {
    let name = firstNameElement.value;
    cardUserFName.textContent = name;
    cardFirstNameInit.textContent = name[0];
  });

  lastNameElement.addEventListener("input", () => {
    let name = lastNameElement.value;
    cardUserLName.textContent = name;
    cardLastNameInit.textContent = name[0];
  });

  phoneNumberElement.addEventListener("input", () => {
    let phone = phoneNumberElement.value;
    cardPhoneNumber.textContent = phone;
  });

  staffEmailElement.addEventListener("input", () => {
    let email = staffEmailElement.value;
    cardEmail.textContent = email;
  });

  userRoleElement.addEventListener("change", () => {
    let role = userRoleElement.value;

    if (role == "manager") {
      cardUserRole.textContent = "Manager";
    } else if (role == "accountant") {
      cardUserRole.textContent = "Accountant";
    } else if (role == "stock-manager") {
      cardUserRole.textContent = "Stock Manager";
    }
  });

  departmentElement.addEventListener("change", () => {
    let dept = departmentElement.value;
    cardDepartment.textContent = dept;
  });

  //Password message for matching passwords
  confirmTempPasswordElement.addEventListener("input", () => {
    let temporaryPassword = temporaryPasswordElement.value;
    let confirmPassword = confirmTempPasswordElement.value;

    if (temporaryPassword != confirmPassword) {
      passwordMessageElement.textContent = "Passwords do not match!";
      passwordMessageElement.classList.remove("text-green");
      passwordMessageElement.classList.add("text-rose-500");
    } else if (temporaryPassword == confirmPassword) {
      passwordMessageElement.textContent = "Passwords Match";
      passwordMessageElement.classList.remove("text-rose-500");
      passwordMessageElement.classList.add("text-green");
    }
  });

  // Create user button click
  createUserBtn.addEventListener("click", (e) => {
    e.preventDefault();
    createUserBtn.setAttribute("disabled", "");
    let firstName = firstNameElement.value;
    let lastName = lastNameElement.value;
    let phone = phoneNumberElement.value;
    let staffEmail = staffEmailElement.value;
    let userRole = userRoleElement.value;
    let department = departmentElement.value;
    let temporaryPassword = temporaryPasswordElement.value;
    let confirmPassword = confirmTempPasswordElement.value;

    if (!(firstName || lastName)) {
      alert("Please provide both first name and last name.");
      createUserBtn.removeAttribute("disabled");
      return;
    }

    if (!(phone || staffEmail)) {
      alert("Please provide both telephone number and staff email.");
      createUserBtn.removeAttribute("disabled");
      return;
    }

    if (!(userRole || department)) {
      alert("Please provide the user role and department of the user.");
      createUserBtn.removeAttribute("disabled");
      return;
    }

    if (!temporaryPassword) {
      alert("Provide a temporary password for the user.");
      createUserBtn.removeAttribute("disabled");
      return;
    }

    if (!confirmPassword) {
      alert("Please confirm temporary password");
      createUserBtn.removeAttribute("disabled");
      return;
    }

    if (!(staffEmail.includes("@") && staffEmail.includes("."))) {
      alert("Please enter a valid email");
      createUserBtn.removeAttribute("disabled");
      return;
    }

    if (temporaryPassword != confirmPassword) {
      alert("Passwords entered do not match.");
      createUserBtn.removeAttribute("disabled");
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

    fetch("/dashboard/user/new/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": csrfToken,
      },
      body: JSON.stringify({
        first_name: firstName,
        last_name: lastName,
        phone_number: phone,
        staff_email: staffEmail,
        user_role: userRole,
        department: department,
        temporary_password: temporaryPassword,
        confirm_password: confirmPassword,
      }),
    })
      .then((Response) => Response.json())
      .then((data) => {
        if (data.code == "USER_CREATION_SUCCESS") {
          alert(data.message);
          window.location.reload();
          return;
        } else {
          alert(data.message || "An error occurred while creating the user.");
          createUserBtn.removeAttribute("disabled");
          return;
        }
      });
  });
});
