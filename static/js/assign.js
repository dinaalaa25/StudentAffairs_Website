const id = document.getElementById("id");
const level = document.getElementById('level');
const name = document.getElementById('name');
assignStudent.addEventListener("submit", (e) => {
    e.preventDefault();
    validateInputs();
});
const setError = (element, message) => {
    const inputControl = element.parentElement;
    const errorDisplay = inputControl.querySelector(".error");

    errorDisplay.innerText = message;
    inputControl.classList.add("error");
    inputControl.classList.remove("success");
};

const setSuccess = (element) => {
    const inputControl = element.parentElement;
    const errorDisplay = inputControl.querySelector(".error");

    errorDisplay.innerText = "";
    inputControl.classList.add("success");
    inputControl.classList.remove("error");
};
const validateInputs = () => {
    const idValue = id.value.trim();
    const levelValue = level.value.trim();
    const nameValue = name.value.trim();
    var letters = /^[A-Za-z]+$/;
    if (idValue.toString().length === 0) {
        setError(id, "ID is required");
    }
    else if (idValue.toString().length < 8) {
        setError(id, "Enter a valid id");
    }
    else {
        setSuccess(id);
    }
    if (levelValue != 3) {
        setError(level, "Assign department is avalible for Third level only.");
    }
    else {
        setSuccess(level);
    } if (nameValue == "") {
        setError(name, " Name is required");
    }
    else if (nameValue.match(letters)) {
        setSuccess(name);
    }
    else {
        setError(name, "Enter a valid name");
    }
}