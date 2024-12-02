/*CHRISTIAN IVAN MARTINEZ MARTINEZ*/

//Cambiar el header cuando el usuario haga scroll
const header = document.querySelector("header");

window.addEventListener("scroll", function () {
    header.classList.toggle("stickycimm", this.window.scrollY > 60)
});
/*
//Mostrar mensaje de alerta con haga click en el boton
document.querySelector('.btn-accion').addEventListener('click', function(){
    alert("Iniciaras tu registro ahora");
}); 

//Aplicar a todos los botones de clase .btn-accion
document.querySelectorAll('.btn-accion').forEach(function(button){
    button.addEventListener('click', function(){
        alert("Has presionado uno de los botones");
    })
});
*/

//Funcion para el primer boton
document.getElementById("btn-registro").addEventListener('click', function () {
    alert("Boton de registro")
});
//Funcion para el segundo boton
document.getElementById("btn-oferta").addEventListener('click', function () {
    alert("Boton de oferta")
});

//Seleccionar todos los enlaces dentro de la clase .navbar
document.querySelectorAll('.navbar a[href^="#"]').forEach(function (enlace) {
    enlace.addEventListener('click', function (e) {
        e.preventDefault();//Prevenir el comportamiento por defecto del enlace
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'instant'
        })
    })
});

//Cambiar la imagen de fondo cada ciertos segundos
const images = [
    '/static/minuz/images/fondoCIMM.jpg',
    '/static/minuz/images/fondoCIMM2.jpg',
    '/static/minuz/images/fondoCIMM3.jpg'
];
const homeSection = document.querySelector('.descrip');
const intervalo = 5000;
let indiceImagen = 0;
function cambiarFondo() {
    homeSection.style.backgroundImage = `url(${images[indiceImagen]})`;
    indiceImagen = (indiceImagen + 1) % images.length;
}
setInterval(cambiarFondo, intervalo);

//MOSTRAR Y OCULTAR NAVBAR
let menu = document.querySelector('#menu_icon');
let navbar = document.querySelector('.navbar');
menu.onclick = () => {
    navbar.classList.toggle('open');
    menu.classList.toggle('bx-x');//Para cambiar el icono del menu lateral
}
//PARA CERRAR EL MENU CUANDO SELECCIONEMOS UN LINK DEL NAVBAR
let enlaces = document.querySelectorAll('.navbar a');
enlaces.forEach(link => {
    link.onclick = () => {
        navbar.classList.remove('open');
        menu.classList.remove('bx-x');
    }
});

//ANIMACION DE TEXTO
var typed = new Typed('#typecimm', {
    strings: ['Tu momento es ahora', 'Construye la cancion de tu vida', 'Aprende de los mejores en:'],
    typeSpeed: 50,
    loop: 'true',
    cursorChar: '|#|',
    backSpeed: 20
  });