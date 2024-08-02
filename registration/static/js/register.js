const choicelogin = document.getElementById("reg-login");
const choicesignup = document.getElementById("reg-signup");
const loginbtn = document.getElementById("loginbtn");
const signupbtn = document.getElementById("signupbtn");

const validateEmail = (email) => {
    return email.match(
      /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
    );
};

function togglePass(id, btn) {
    let input = document.getElementById(id);
    if (input.type === "password") {
        input.type = "text";
        btn.firstChild.innerHTML = "visibility_off"
    } else {
        input.type = "password";
        btn.firstChild.innerHTML = "visibility"
    }
}


function activateLogin() {
    choicelogin.style.display = "block";
    choicesignup.style.display = "none";
    loginbtn.classList.add("cur-on");
    signupbtn.classList.remove("cur-on");
    choicelogin.style.animation = "Fadein 0.8s"
}

function activateSignup() {
    choicelogin.style.display = "none";
    choicesignup.style.display = "block";
    loginbtn.classList.remove("cur-on");
    signupbtn.classList.add("cur-on");
    choicesignup.style.animation = "Fadein 0.8s"
}

function checkInputLength(input, n) {
    const fspass = document.getElementById("fs-pass");
    const fspasscon = document.getElementById("fs-passcon");
    if (fspass.value == fspasscon.value) {
        fspasscon.classList.remove("inputerror");
    }

    if (input.value.length < n) {
        input.classList.add("inputerror");
        return false;
    } else {
        input.classList.remove("inputerror");
        return true;
    }

}

function checkPassCon() {
    const fspass = document.getElementById("fs-pass");
    const fspasscon = document.getElementById("fs-passcon");
    if (fspasscon.value != fspass.value) {
        fspasscon.classList.add("inputerror");
        return false;
    } else {
        fspasscon.classList.remove("inputerror");
        return true;
    }
}

function checkEmail() {
    const fsemail = document.getElementById("fs-email");
    if (!validateEmail(fsemail.value)) {
        fsemail.classList.add("inputerror");
        return false;
    } else {
        fsemail.classList.remove("inputerror");
        return true;
    }

}

function submitFS() {
    const fspass = document.getElementById("fs-pass");
    const fsname = document.getElementById("fs-name");
    const form = document.getElementById("reg-signup");
    if (checkInputLength(fsname, 6) && checkEmail() && checkInputLength(fspass, 6) && checkPassCon()) {
        form.submit();
    }
}
function submitFL(e) {
    const flpass = document.getElementById("fl-pass");
    const flname = document.getElementById("fl-name");
    const form = document.getElementById("reg-login");
    if (checkInputLength(flname, 1) && checkInputLength(flpass, 1)) {
        form.submit();
    }
}