# Lista de nomes das area
nomes_areas = ["Saúde", "Desenvolvimento Pessoal", "Carreira/Profissão", "Relacionamentos", "Finanças", "Espiritualidade", "Diversão", "Ambiente", "SAIR"]
# Lista para armazenar os dados das áreas
areas = {}


def opcao_areas():
    print("Vamos continuar então...")# Loop para 
    #tempo de espera

    #solicitar a idade dos garotos
    for nome in nomes_areas:
        nota = int(input("Digite a nota de {}: ".format(nome)))
        areas[nome] = nota


    # Ordenar os garotos por idade
    areas_ordenadas = sorted(areas, key=areas.get)[:2]

    # Retornar os nomes das 2 áreas de menores notas
    print("As áreas de notas mais baixas são: ", areas_ordenadas )


while True:
    escolha = input("Digite 'c' para continuar ou 's' para sair: ")
    if escolha == 'c':
        print("Continuando...")
        opcao_areas()  # Chamada da função
    elif escolha == 's':
        print("Saindo...")
        break
    else:
        print("Opção inválida. Por favor, digite 'c' para continuar ou 's' para sair.")
    
    