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



    
def saude()
    texto1 = """
    Faz quanto tempo que você procurou ajuda médica ?

 Você mantem um hábito alimentação saudável ? 

Você tem realizado exercícios regulares ?

Você tem feito um descanso adequado ?

Você tem um sono de qualidade, e com período adequado? 

Você acorda cansado ?
"""



def desenvolvimento_pessoal()
    texto1 =
"""
1. Estabelecer metas claras e alcançáveis.
2. Aprender continuamente, seja por meio da leitura, cursos online, workshops, etc.
3. Praticar a auto-reflexão e autoconhecimento.
4. Desenvolver habilidades interpessoais, como comunicação eficaz e empatia.
5. Cuidar da saúde mental através de práticas como meditação, exercícios de respiração, ou terapia.
6. Sair da zona de conforto, desafiando-se regularmente.
7. Construir e manter relacionamentos positivos.
8. Praticar a gratidão e a positividade.
9. Equilibrar vida pessoal e profissional para evitar o esgotamento.
10. Ser paciente consigo mesmo e celebrar o progresso, mesmo que pequeno.
"""






def Carreira_Profissão()
   vtexto1 =
"""
Desenvolver-se na carreira profissional envolve várias etapas


 o que você tem feito para adquirir novas habilidades ?

você tem buscado experiências relevantes?

você tem construído networking ?

 o que você tem feito para desenvolver seu autoconhecimento?

quais  cursos você fez ultimamente ?

você tem participado de eventos da sua área?

você tem buscado mentoria ?

 você acha que você se mantem atualizado sobre as tendências do mercado ?

você Tem uma visão clara de seus objetivos ?

você tem trabalhado de forma consistente para alcançá-los ?
"""




def Carreira_Profissão()
   vtexto1 =
"""

"""





def Carreira_Profissão()
   vtexto1 =
"""

"""






def Carreira_Profissão()
   vtexto1 =
"""

"""






def Carreira_Profissão()
   vtexto1 =
"""

"""





def Carreira_Profissão()
   vtexto1 =
"""

"""





def Carreira_Profissão()
   vtexto1 =
"""

"""






def Carreira_Profissão()
   vtexto1 =
"""

"""