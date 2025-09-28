class NodoEstado:
    def __init__(self, sigla, nome):
        self.sigla = sigla
        self.nome = nome
        self.proximo = None


def inserir_na_lista(head, sigla, nome):
    novo_nodo = NodoEstado(sigla, nome)
    novo_nodo.proximo = head
    return novo_nodo


def imprimir_tabela_hash():
    print("==== TABELA HASH ====")
    for i in range(10):
        print(f"Posição {i}: ", end="")
        atual = tabela_hash[i]
        while atual:
            print(f"[{atual.sigla}] -> ", end="")
            atual = atual.proximo
        print("None")
    print()


def funcao_hash(sigla):
    if sigla.upper() == "DF":
        return 7
    else:
        a = ord(sigla[0].upper())
        b = ord(sigla[1].upper())
        return (a * 100 + b) % 10


# Tabela hash com 10 posições
tabela_hash = [None] * 10

# Lista de estados brasileiros + DF
estados = [
    ("AC", "Acre"), ("AL", "Alagoas"), ("AP", "Amapá"), ("AM", "Amazonas"),
    ("BA", "Bahia"), ("CE", "Ceará"), ("DF", "Distrito Federal"), ("ES", "Espírito Santo"),
    ("GO", "Goiás"), ("MA", "Maranhão"), ("MT", "Mato Grosso"), ("MS", "Mato Grosso do Sul"),
    ("MG", "Minas Gerais"), ("PA", "Pará"), ("PB", "Paraíba"), ("PR", "Paraná"),
    ("PE", "Pernambuco"), ("PI", "Piauí"), ("RJ", "Rio de Janeiro"), ("RN", "Rio Grande do Norte"),
    ("RS", "Rio Grande do Sul"), ("RO", "Rondônia"), ("RR", "Roraima"), ("SC", "Santa Catarina"),
    ("SP", "São Paulo"), ("SE", "Sergipe"), ("TO", "Tocantins")
]

if __name__ == "__main__":
    print(">>> Antes de qualquer inserção:")
    imprimir_tabela_hash()

    for sigla, nome in estados:
        indice = funcao_hash(sigla)
        tabela_hash[indice] = inserir_na_lista(tabela_hash[indice], sigla, nome)

    print(">>> Após inserir os 27 estados (incluindo DF):")
    imprimir_tabela_hash()

    sigla_ficticia = "TF"
    nome_ficticio = "Tatiana Ferreira"
    indice_ficticio = funcao_hash(sigla_ficticia)
    tabela_hash[indice_ficticio] = inserir_na_lista(tabela_hash[indice_ficticio], sigla_ficticia, nome_ficticio)

    print(">>> Após inserir estado fictício:")
    imprimir_tabela_hash()
