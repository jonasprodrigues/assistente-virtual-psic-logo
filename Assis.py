# Lista de nomes das area
nomes_areas = ["Saúde", "Desenvolvimento Pessoal", "Carreira/Profissão", "Relacionamentos", "Finanças", "Espiritualidade", "Diversão", "Ambiente", "SAIR"]
# Lista para armazenar os dados das áreas
areas = []

# Loop para solicitar a idade dos garotos
for nome in nomes_areas:
    nota = int(input("Digite a nota de {}: ".format(nome)))
    #areas.append((area, nota))
    areas[nome] = nota


# Ordenar os garotos por idade
areas_ordenadas = sorted(areas, key=lambda x: x[1])

# Retornar os nomes das 2 áreas de menores notas
print("As áreas de notas mais baixas são:")
for area, _ in areas_ordenados[:2]:
    print(area)
