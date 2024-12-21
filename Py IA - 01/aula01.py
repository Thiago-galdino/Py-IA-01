# numero_procurado = 7

# for i in range(1, 11):
#     if i == numero_procurado:
#         print(f"Numero {numero_procurado} encontrado!")
#         break
#     print(i)


# for i in range(1, 11):
#    if i % 2 != 0:
#      continue
# print(i)



# for num in range(2, 20):
#     for i in range(2, num):
#         if num % i == 0:
#             break
#     else:
#         print(f"{num} é um numero primo!")


# listas_de_numeros = [1,2,3,4,5]

# listas_de_letras = ["a", "e", "i", "o", "u"]

# listas_de_logicos = [True, False, False,True]

# listas_de_mistas = ['Gabriel', 12, True]
# print(listas_de_letras)



# nota = [10.0,9.8,8.7]
# print(nota[1])


# numeros = [1, 2, 3, 4, 5]

# numeros.append(6)
# print(numeros)


# numeros = [10, 30, 40, 50]
# letras = ['a', 'e', 'o', 'u']
# pesos = [1.2, 3.4, 5.3, 6.7]

# numeros.insert
# letras.insert
# pesos.insert

# print(numeros)
# print(letras)
# print(pesos)



# listas_compras = [
#     "2 pct de arroz",
#     "6 pct de Feijão",
#     "2 pct de Farinha",
#     "4Kg de Linguiça",
#     "4Kg de charque",
#     "2KG de Bacon",
#     "2Kg de Pe de porco",
# ]

# print("LISTAS DE COMPRAS", end='\n\n')

# for item in listas_compras:
#     print("[]", item)


#             TUPLAS


# frutas = ("maçã","banana","laranja","abacaxi")

# indice_laranja = frutas.index("laranja")
# print("Quantidade de laranja:", indice_laranja)


# quantidade_banana = frutas.count("banana")
# print("Quantidade de banana:", quantidade_banana)

# maca, banana, laranja, abacaxi = frutas
# print("Fruta 1:", maca)
# print("Fruta 2:", banana)
# print("Fruta 3:", laranja)
# print("Fruta 4:", abacaxi)


############################################################



# Criando a tupla com informações dos palestrantes
palestrantes = (
    ("João Silva", "Inteligência Artificial", "Universidade XYZ"),
    ("Maria Oliveira", "Machine Learning", "Instituto ABC"),
    ("Carlos Souza", "Redes Neurais", "Universidade DEF")
)

# Exibindo as informações do terceiro palestrante
terceiro_palestrante = palestrantes[2]  # Índice 2 para o terceiro palestrante
nome, tema, instituicao = terceiro_palestrante

print(f"Nome: {nome}")
print(f"Tema da Palestra: {tema}")
print(f"Instituição: {instituicao}")



#######################################################





# Lista de resultados das equipes, cada tupla contém o nome da equipe e as pontuações em cada rodada
resultados = [
    ("Equipe A", [8, 9, 7, 6]),
    ("Equipe B", [9, 10, 8, 9]),
    ("Equipe C", [7, 6, 8, 7]),
    ("Equipe D", [10, 9, 9, 10])
]

# 1. Calcular a média das pontuações de cada equipe e armazenar em uma nova lista chamada medias
medias = []
for equipe, pontuacoes in resultados:
    media = sum(pontuacoes) / len(pontuacoes)
    medias.append((equipe, media))

# 2. Ordenar a lista medias em ordem decrescente de média
medias.sort(key=lambda x: x[1], reverse=True)

# 3. Criar a lista classificacao com o nome da equipe e sua média
classificacao = medias

# 4. Exibir a classificação final das equipes
print("Classificação Final:")
for equipe, media in classificacao:
    print(f"{equipe}: {media:.2f}")

