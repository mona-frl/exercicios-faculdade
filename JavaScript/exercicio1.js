let botao = document.querySelector("#botao");
botao.style.background="blue";
let isBroken=false;


botao.addEventListener("mouseover",e =>{
    if(!isBroken)
        botao.style.background="green"
});

botao.addEventListener("mouseout", e =>{
    if (!isBroken)
        botao.style.background="blue"
});

botao.addEventListener("click", e =>{
    botao.style.background="red";
    botao.innerHTML="Broken!"
    isBroken===true;
})
