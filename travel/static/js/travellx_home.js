const bus = document.querySelector("nav");
const navlink = document.querySelector(".nav-link");
const links = document.querySelectorAll(".nav-link li");
var moi = document.querySelector(".part .part1");
var bool = 1;

bus.addEventListener('click', () => {
    navlink.classList.toggle('open');
    links.forEach(link => {
        link.classList.toggle('fade');
    });
    if(bool === 1){
        moi.style.display = "none";
        bool = 0;
    }
    else{
        moi.style.display = "flex";
        bool = 1;
    }
})
