const addStudent = document.getElementById("addStudent");
const fname = document.getElementById("fname");
const lname = document.getElementById("lname");
const gpa = document.getElementById("gpa");
const id = document.getElementById("id");
addStudent.addEventListener("submit", (e) => {
    e.preventDefault();
    validateInputs();
});
let valid = {

};
const setError = (element, message) => {
    const inputControl = element.parentElement;
    const errorDisplay = inputControl.querySelector(".error");

    errorDisplay.innerText = message;
    inputControl.classList.add("error");
    inputControl.classList.remove("success");
    valid[element] = false;
};

const setSuccess = (element) => {
    const inputControl = element.parentElement;
    const errorDisplay = inputControl.querySelector(".error");

    errorDisplay.innerText = "";
    inputControl.classList.add("success");
    inputControl.classList.remove("error");
    valid[element] = true;
};
const isValidEmail = (email) => {
    const re =
        /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(String(email).toLowerCase());
};
const validateInputs = () => {
    const fnameValue = fname.value.trim();
    const lnameValue = lname.value.trim();
    const gpaValue = gpa.value.trim();
    const emailValue = email.value.trim();
    const PNValue = PN.value.trim();
    const idValue = id.value.trim();
    var letters = /^[A-Za-z]+$/;
    if (fnameValue == "") {
        setError(fname, "First Name is required");
    }
    else if (fnameValue.match(letters)) {
        setSuccess(fname);
    }
    else {
        setError(fname, "Enter a valid name");
    }
    if (lnameValue == "") {
        setError(lname, "Last Name is required");
    }
    else if (lnameValue.match(letters)) {
        setSuccess(lname);
    }
    else {
        setError(lname, "Enter a valid name");
    }
    if (gpaValue < 0 || gpaValue > 4 || gpaValue.toString().length === 0) {
        setError(gpa, "gpa is invalid");
    }
    else {
        setSuccess(gpa);
    }
    if (emailValue === "") {
        setError(email, "Email is required");
    }
    else if (!isValidEmail(emailValue)) {
        setError(email, "Provide a valid email address");
    }
    else {
        setSuccess(email);
    }
    if (PNValue.toString().length !== 11) {
        setError(PN, "phone number is invalid");
    }
    else {
        setSuccess(PN);
    }
    if (idValue.toString().length === 0) {
        setError(id, "ID is required");
    }
    else if (idValue.toString().length < 8) {
        setError(id, "Enter a valid id");
    }
    else {
        setSuccess(id);
    }

};
function confirmDeletion() {
    validateInputs();
    let isValid = true;
    Object.keys(valid).forEach(key => {
        if (!valid[key]) {
            isValid = false;
        }
    })
    console.log(JSON.stringify(valid));
    if (isValid) {
        let confirmAction = confirm("Are you sure to delete this student?");
        if (confirmAction) {
            alert("deletion successfully done");
        } else {
            alert("deletion canceled");
        }
    }

}
function ConfirmDelete() {
    return confirm("Are you sure you want to delete?");
}
function Reset() {
    document.getElementById("addStudent").reset();
}
function Save() {
    alert("save successfully done ")
}