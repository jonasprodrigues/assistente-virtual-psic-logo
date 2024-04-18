import time

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
    texto1 =  """
Olá. Eu sou um Assistente Virtual pra te ajudar a fazer sua avaliação da roda da vida.

A roda da vida é uma ferramenta de autoavaliação e desenvolvimento pessoal utilizada para avaliar e visualizar diferentes áreas da vida de uma pessoa. 

Geralmente, essas áreas incluem aspectos como carreira, finanças, saúde, relacionamentos, desenvolvimento pessoal, lazer, espiritualidade, entre outros.

A roda da vida consiste em um círculo dividido em seções, representando cada uma dessas áreas da vida. 

A pessoa avalia sua satisfação ou desempenho em cada área atribuindo uma pontuação, geralmente de 1 a 10, com base em sua percepção. 

Depois de atribuir as pontuações, a pessoa conecta os pontos no círculo, criando uma representação visual de sua situação atual.

Essa representação visual ajuda a identificar áreas que estão equilibradas e áreas que precisam de mais atenção e desenvolvimento. 

Com base nessa análise, a pessoa pode definir metas e criar um plano de ação para melhorar as áreas que deseja aprimorar, buscando um equilíbrio mais satisfatório em sua vida.
    """
    print(texto1)
    time.sleep(2)
    texto2 = """
As 10 áreas comuns frequentemente incluídas na roda da vida:

Carreira/Profissão: Satisfação e progresso na carreira ou no trabalho.
Finanças: Gerenciamento e estabilidade financeira.
Saúde Física: Bem-estar físico e saúde geral do corpo.
Saúde Mental/Emocional: Equilíbrio emocional, saúde mental e resiliência.
Relacionamentos: Qualidade e satisfação nos relacionamentos pessoais e familiares.
Desenvolvimento Pessoal: Crescimento pessoal, aprendizado contínuo e autodesenvolvimento.
Espiritualidade: Conexão espiritual, propósito e significado na vida.
Lazer/Recreação: Atividades de lazer, hobbies e tempo de qualidade para relaxamento.
Ambiente: Conforto e satisfação com o ambiente físico, seja em casa ou no trabalho.
Contribuição/Serviço: Sentido de contribuição para a comunidade, voluntariado e impacto social positivo. """
    print(texto2)
    time.sleep(2)
    escolha = input("Digite 'c' para continuar ou 's' para sair: ")
    if escolha == 'c':
        print("Continuando...")
        opcao_areas()  # Chamada da função
    elif escolha == 's':
        print("Saindo...")
        break
    else:
        print("Opção inválida. Por favor, digite 'c' para continuar ou 's' para sair.")
    
    