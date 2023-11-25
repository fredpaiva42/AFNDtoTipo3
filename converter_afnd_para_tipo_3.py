import json

'''
Observação: as transições devem estar ordenadas de acordo com os estados definidos, ou seja,
se nos estados tivermos "estados": ["S", "A", "B"] a transição deve começar com S, depois A e por fim B.

*Explicando as transições*
"transicoes": {
    "S": { "a": ["S", "A"], "b": ["S"]},
    "A": { "b": ["B"]},
    "B": { "a": ["B"], "b": ["B"]}
}
 1 vai nele mesmo e em A com o simbolo a, 1 também vai em nele mesmo com o simbolo b
 A vai em B com b
 B vai nele mesmo com o simbolo a e b
 
'''


class AFND:
    def __init__(self):
        self.regras = []  # transições diretas
        self.estados = []
        self.alfabeto = []
        self.transicoes = {}
        self.estado_inicial = None
        self.estados_finais = []

    def afnd_para_gramatica_regular(self):

        if self.estado_inicial != self.estados[0]:
            self.adiciona_regra(False)
        else:
            self.adiciona_regra()

        # Regra para adicionar o ε nas transições cada estado final
        for estado in self.estados:
            if estado in self.estados_finais:
                regra = f"{estado} -> e"
                self.regras.append(regra)

        return self.regras

    def adiciona_regra(self, inicio=True):
        # Usa o items() para acessar os pares chave-valor do JSON

        for estado, transicoes in self.transicoes.items():
            for simbolo, proximos_estados in transicoes.items():
                for proximo_estado in proximos_estados:
                    # Enquando o início não for igual ao estado atual, avança as transições
                    if estado != self.estado_inicial and not inicio:
                        inicio = False
                    else:
                        if simbolo == "e":  # Símbolo do ε
                            regra = f"{estado} -> {proximo_estado}"
                            self.regras.append(regra)
                        else:
                            regra = f"{estado} -> {simbolo}{proximo_estado}"
                            self.regras.append(regra)


def main():
    with open("afnds.json", "r") as afnd_file:
        dados = json.load(afnd_file)

    for i, dado in enumerate(dados):

        afnd = AFND()
        afnd.estados = dado["estados"]
        afnd.alfabeto = dado["alfabeto"]
        afnd.estado_inicial = dado["estado_inicial"]
        afnd.estados_finais = dado["estados_finais"]
        afnd.transicoes = dado["transicoes"]

        # Converta o AFND em uma gramática regular
        gramatica = afnd.afnd_para_gramatica_regular()

        # Imprime a gramática
        print(f"\n{i + 1} - Gramática Regular:")
        for regra in gramatica:
            print(regra)


if __name__ == "__main__":
    main()
