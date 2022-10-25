{% load static %}

var menu = document.querySelector('nav ul');
var menuBar = document.querySelector('nav .menu-icon');
var iconMenu = document.querySelector('nav .menu-icon img');

menuBar.addEventListener('click',function(){

    if (iconMenu.getAttribute("src") == {% static 'img/menu.png'%}) {
        iconMenu.setAttribute("src",{% static 'img/close.png'%});
    }else{
        iconMenu.setAttribute("src",{% static 'img/menu.png'%});
    }

   menu.classList.toggle('active');

   function Enviar() {

    var nome = document.getElementById("nomeid");

    if (nome.value != "") {
        alert('Obrigado sr(a) ' + nome.value + ' os seus dados foram encaminhados com sucesso');
    }

}
});