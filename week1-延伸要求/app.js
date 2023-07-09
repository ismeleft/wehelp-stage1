let hamburger = document.querySelector(".hamburger");
let navitem = document.querySelector(".nav-menu");

hamburger.addEventListener("click",()=>{
    navitem.classList.toggle("active");
})

