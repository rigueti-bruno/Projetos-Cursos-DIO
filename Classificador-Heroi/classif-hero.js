//Projeto Classificador do Heroi:

//Dados do Heroi:
let heroName = 'Bruno';
let exp = 7500;
let clas;

//Classificacao:
if (exp <= 1000) {
    clas = 'Ferro';
} else if (exp > 1000 && exp <= 2000) {
    clas = 'Bronze';
} else if (exp > 2000 && exp <= 5000) {
    clas = 'Prata';
} else if (exp > 5000 && exp <= 7000) {
    clas = 'Ouro';
} else if (exp > 7000 && exp <= 8000) {
    clas = 'Platina';
} else if (exp > 8000 && exp <= 9000) {
    clas = 'Ascendente';
} else if (exp > 9000 && exp <= 10000) {
    clas = 'Imortal';
} else {
    clas = 'Radiante';
};

console.log(`O Herói ${heroName} está no nível de ${clas}!`);