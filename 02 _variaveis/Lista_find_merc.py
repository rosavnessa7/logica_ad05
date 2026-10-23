print("Lista de frutas e itens para churrasco")
Lista_frutas = [
    "Banana",
    "Maçã",
    "Uva",
    "Pera",
]
print(Lista_frutas)
Lista_frutas.append(input("Digite uma fruta: "))
print(Lista_frutas)
Lista_churrasco = [
    "Carne",
    "Linguiça",
    "Pão de alho",
    'carvão',
]
print(Lista_churrasco)
Lista_churrasco.append(input("Digite um item para o churrasco: "))
print(Lista_churrasco)

Toda_lista_de_mercado = (Lista_frutas + Lista_churrasco)
print("Lista de mercado: ", Toda_lista_de_mercado)