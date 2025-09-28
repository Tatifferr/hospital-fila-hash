class Nodo:
    def __init__(self, numero, cor):
        self.numero = numero
        self.cor = cor
        self.proximo = None


class FilaHospitalar:
    def __init__(self):
        self.head = None
        self.contador_v = 1     # Numeração de cartões verdes (começa em 1)
        self.contador_a = 201   # Numeração de cartões amarelos (começa em 201)

    def inserir_sem_prioridade(self, novo_nodo):
        if self.head is None:
            self.head = novo_nodo
        else:
            atual = self.head
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = novo_nodo

    def inserir_com_prioridade(self, novo_nodo):
        if self.head is None:
            self.head = novo_nodo
        elif self.head.cor == "V":
            novo_nodo.proximo = self.head
            self.head = novo_nodo
        else:
            atual = self.head
            while atual.proximo and atual.proximo.cor == "A":
                atual = atual.proximo
            novo_nodo.proximo = atual.proximo
            atual.proximo = novo_nodo

    def inserir(self):
        cor = input("Digite a cor do cartão (A ou V): ").strip().upper()
        if cor == "A":
            numero = self.contador_a
            self.contador_a += 1
        elif cor == "V":
            numero = self.contador_v
            self.contador_v += 1
        else:
            print("Cor inválida. Use apenas 'A' ou 'V'.")
            return

        novo_nodo = Nodo(numero, cor)

        if self.head is None:
            self.head = novo_nodo
        elif cor == "A":
            self.inserir_com_prioridade(novo_nodo)
        else:
            self.inserir_sem_prioridade(novo_nodo)

        print(f"Paciente com cartão {cor}{numero} inserido com sucesso.")

    def imprimir_lista_espera(self):
        atual = self.head
        if atual is None:
            print("Fila vazia.")
        else:
            print("Pacientes na fila:")
            while atual:
                print(f"Cartão {atual.cor}{atual.numero}")
                atual = atual.proximo

    def atender_paciente(self):
        if self.head is None:
            print("Não há pacientes na fila.")
        else:
            paciente = self.head
            self.head = self.head.proximo
            print(f"Chamando paciente com cartão {paciente.cor}{paciente.numero} para atendimento.")


def menu():
    fila = FilaHospitalar()
    while True:
        print("\nMENU:")
        print("1 - Adicionar paciente à fila")
        print("2 - Mostrar pacientes na fila")
        print("3 - Chamar paciente")
        print("4 - Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            fila.inserir()
        elif opcao == "2":
            fila.imprimir_lista_espera()
        elif opcao == "3":
            fila.atender_paciente()
        elif opcao == "4":
            print("Encerrando programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()
