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





// function validateForm() {
//     const firstname = document.getElementById("firstname");
//     const lastname = document.getElementById("lastname");
//     const email = document.getElementById("email");
//     const phone = document.getElementById("phone");
//     const subject = document.getElementById("subject");
//     const message = document.getElementById("message");
//     let alphabets = /^[A-Za-z]+$/;
//     if (firstname.value.trim().length === 0 && lastname.value.trim().length === 0 && email.value.trim().length === 0 && phone.value.trim().length === 0 && subject.value.trim().length === 0 && message.value.trim().length === 0) {
//         swal("Oops...", "Please! Enter the credentials first .", "error");
//         return false;
//     }
//     if (firstname.value.trim().length === 0) {
//         swal("Oops...", "Please! Enter your first name .", "error");
//         return false;
//     }
//     if (!firstname.value.trim().match(alphabets)) {
//         swal("Oops...", "Please! Enter a valid first name.", "error");
//         return false;
//     }
//     if (lastname.value.trim().length > 0) {
//         if (!lastname.value.trim().match(alphabets)) {
//             swal("Oops...", "Please! Enter a valid last name.", "error");
//             return false;
//         }
//     }
//     if (email.value.trim().length === 0) {
//         swal("Oops...", "Please! Enter your email address.", "error");
//         return false;
//     }
//     if (!email.value.trim().includes("@gmail.com")) {
//         swal("Oops...", "Please! Enter a valid email address.", "error");
//         return false;
//     }
//     if (phone.value.trim().length != 10 || isNaN(phone.value.trim())) {
//         swal("Oops...", "Phone number should be 10 digits. ", "error");
//         return false;
//     }
//     if (subject.value.trim().length === 0) {
//         swal("Oops...", "Please! Enter the subject.", "error");
//         return false;
//     }
//     if (message.value.trim().length === 0) {
//         swal("Oops...", "Please! Enter the message.", "error");
//         return false;
//     }
//     swal("Congrats!", "Message was delivered successfully! Thanks for your Submission", "success");
//     return true;
// }
//
// document.getElementById("submit-btn").addEventListener("click", validateForm);
//
// function clearFunc() {
//     document.getElementById("firstname").value = "";
//     document.getElementById("lastname").value = "";
//     document.getElementById("email").value = "";
//     document.getElementById("phone").value = "";
//     document.getElementById("subject").value = "";
//     document.getElementById("message").value = "";
// }
