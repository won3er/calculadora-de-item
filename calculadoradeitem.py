#Definindo as funcionalidades:
def calcular_total(lista_itens):
    total = 0
    for item in lista_itens:
        total += item
    return total

itens = []  # Lista para armazenar os nomes dos itens
nomes_itens = []  # Lista para armazenar os nomes dos itens
continuar = 'y'

while continuar.lower() == 'y':
    nome = input('Digite o nome do item: ')
    valor = float(input('Digite o valor do item: '))
    itens.append(valor) 
    nomes_itens.append(nome) # Adiciona o nome do item à lista de nomes
    continuar = input("Deseja adicionar outro item? (y/n): ")

resultado_total = calcular_total(itens)
print("Total de itens:", len(itens))

# Imprime os itens adicionados com seus respectivos nomes
print("Itens adicionados: ")
for nome, valor in zip(nomes_itens, itens):
    print(f"{nome}: {valor}R$")

print("Total a pagar:", resultado_total,'R$')