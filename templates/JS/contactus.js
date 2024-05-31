function validateForm() {
    var firstname = document.forms["contact-form"]["firstname"].value;
    // var lastname = document.forms["contact-form"]["lastname"].value;
    var email = document.forms["contact-form"]["email"].value;
    var phone = document.forms["contact-form"]["phone"].value;
    // var subject = document.forms["contact-form"]["subject"].value;
    var message = document.forms["contact-form"]["message"].value;

    if (firstname == "" || email == "" || phone == "" || message == "") {
        alert("Please fill in all fields");
        return false;
    }

    // Validate email format
    var emailRegex = /^\S+@\S+\.\S+$/;
    if (!emailRegex.test(email)) {
        alert("Please enter a valid email address");
        return false;
    }

    // Validate phone number format
    var phoneRegex = /^\d{10}$/;
    if (!phoneRegex.test(phone)) {
        alert("Please enter a 10-digit phone number");
        return false;
    }
    return true;
}

function clearFunc() {
    document.getElementById("contact-form").reset();
}

document.getElementById("submit-btn").addEventListener("click", function() {
    if (validateForm()) {
        alert("Message was delivered successfully! Thanks for your Submission");
    }
});
