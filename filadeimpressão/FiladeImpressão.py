class FilaDeImpressao:

        def configurar_incial(self):
            self.fila= []

        #isso daqui vai guardar a fila de impressao no vetor fila
        def adicionar_trabalho(self,trabalho):
            self.fila.append(trabalho)
            print(f"Trabalho '{trabalho}' adicionado a fila de impressao")

            #remover o trabalho da lista
        def processar_trabalho(self):
            if not self.esta_vazia(): #verifica se a lista nao esta vazia
                trabalho = self.fila.pop(0) #remove o primeiro da fila
                print(f"O trabalho '{trabalho}' esta sendo processado")
            else: 
                print("A fila de impressao esta vazia!")

                #mostrar a fila de impressao
                def mostra_fila(self):
                    if self.esta_vazia():
                        print("A fila esta vazia!")
                    else:
                        print("Fila atual de impressao: ")
                        for trabalho in self.fila:
                            print(f"-{trabalho}") #imprimir cada trabalho da lista 
                    
        def esta_vazia(self):
            return len(self.fila) == 0


def menu():

    fila_impressao=FilaDeImpressao()
                    #criando uma instancia para a classe
    fila_impressao.configurar_inicial()
                    #configurar os atributos de entrada/inicial
    while True:
                        #opcoes para o nosso usuario

            print("Opções: ")
            print("1. Adicionar um trabalho na fila de impressao")
            print("2. Imprimir o proximo trabalho da fila")
            print("3. Mostrar a fila de impressao")
            print("4. Sair")

            escolha =input("Escolha uma opção 1-4 ")
                        #aqui vai ser lido a escolha do usuario

            if escolha== "1":
                trabalho = input("Digite o nome do trabalho a ser impresso")
                            #maquina da pessoa que esta imprimindo
                fila_impressao.adicionar_trabalho(trabalho)
            elif escolha=="2":
                fila_impressao.processar_trabalho()
            elif escolha=="3":
                fila_impressao.mostrar_fila()
            elif escolha=="4":
                print("Saindo do Programa")
                break
            else:   
                print("Opção invalida")
menu()