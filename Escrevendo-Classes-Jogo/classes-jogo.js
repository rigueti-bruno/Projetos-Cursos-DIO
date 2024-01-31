class Personagem {
    constructor(nome,idade,tipo) {
        this.nome = nome;
        this.idade = idade;
        this.tipo = tipo;
    }

    // Metodo que extrai o resultado invocando o metodo que calcula - esse que deve ser invocado:
    get ataque() {
        return this.tool();
    }

    // Metodo que calcula - é invocado pelo metodo get:
    tool() {        
        if (this.tipo === 'mago') {
            return 'magia'
        } else if (this.tipo === 'guerreiro') {
            return 'espada'
        } else if (this.tipo === 'monge') {
            return 'artes marciais'
        } else if (this.tipo === 'ninja') {
            return 'shuriken'
        }
    }
}

// Informar como tipo: mago, guerreiro, monge ou ninja:
let batman = new Personagem('Bruce',36,'ninja');
let goku = new Personagem('Kakaroto',56,'monge');

console.log(`O ${batman.tipo} atacou usando ${batman.ataque}.`);

console.log(`O ${goku.tipo} atacou usando ${goku.ataque}.`);