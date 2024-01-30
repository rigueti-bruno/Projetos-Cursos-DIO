let vit = 105;
let der = 55;

function sald(vit, der) {
    let sad = vit - der;
    return sad
}

let sado = sald(vit,der);
function categ(sad) {
    if (sad <= 10) {
        return 'Ferro'
    } else if (sad > 10 && sad <= 20) {
        return 'Bronze'
    } else if (sad > 20 && sad <= 50) {
        return 'Prata'
    } else if (sad > 50 && sad <= 80) {
        return 'Ouro'
    } else if (sad > 80 && sad <= 90) {
        return 'Diamante'
    } else if (sad > 90 && sad <= 100) {
        return 'Lendário'
    } else if (sad > 100) {
        return 'Imortal'
    }
};

console.log(`O Herói tem saldo de ${sado} Vitórias e está no Nível ${categ(sado)}.`);