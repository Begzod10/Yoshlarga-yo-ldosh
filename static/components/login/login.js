const eye = document.querySelector("#eye"),
    password = document.querySelector("#password")


eye.addEventListener("click" , () =>{
    if (password.type === "password"){
        password.type = "text"
    }else {
        password.type = "password"
    }
})