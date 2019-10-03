var total = 0
var qtde = 0
var total_atual = document.querySelector("#total_atual")

function comprar(modelo) {
    switch (modelo) {
        case 'm1':
            qtde = document.querySelector("#qtde_m1")
            total = total + (qtde.value * 68.55)
            break;
        case 'm2':
            qtde = document.querySelector("#qtde_m2")
            total = total + (qtde.value * 199)
            break;
        case 'm3':
            qtde = document.querySelector("#qtde_m3")
            total = total + (qtde.value * 168.55)
            break;
    }
    total_atual.innerHTML = `Total: R$ ${total.toFixed(2)}`
}