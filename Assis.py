import time
import python_avatars as pa
from tkinter import *

root = Tk()

root.mainloop()

'''
from PySimpleGUI import PySimpleGUI as sg

#LAYOUT
sg.theme('Reddit')
layout = [
    {sg.Text('Usuario'), sg.Input(key='usuario')},
    {sg.Text('senha'), sg.Input(key='senha')},
    {sg.Checkbox('Salvar')},
    {sg.Button('entrar')},
]
#JANELA
janela = sg.Window('tela login', layout)
#LER EVENTOS
while True:
    eventos, valoes = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'entrar':
        ("Vamos continuar então...")# Loop para 

'''


my_avatar = pa.Avatar(
    style=pa.AvatarStyle.CIRCLE,
    background_color=pa.BackgroundColor.BLACK,
    top=pa.HairType.STRAIGHT_2,
    eyebrows=pa.EyebrowType.DEFAULT_NATURAL,
    eyes=pa.EyeType.DEFAULT,
    nose=pa.NoseType.DEFAULT,
    mouth=pa.MouthType.EATING,
    facial_hair=pa.FacialHairType.NONE,
    # You can use hex colors on any color attribute...
    skin_color="#00FFFF",
    # Or you can use the colors provided by the library
    hair_color=pa.HairColor.BLACK,
    accessory=pa.AccessoryType.NONE,
    clothing=pa.ClothingType.HOODIE,
    clothing_color=pa.ClothingColor.HEATHER
)

# Save to a file
my_avatar.render("my_avatar.svg")


funcao1 = ""
funcao2 = ""

# Lista de nomes das area
nomes_areas = ["Saúde", "Desenvolvimento Pessoal", "Carreira/Profissão", "Relacionamentos", "Finanças", "Espiritualidade", "Diversão", "Ambiente", "SAIR"]
# Lista para armazenar os dados das áreas
areas = {}


def opcao_areas():
    print("Vamos continuar então...")# Loop para 
    #tempo de espera

    #solicitar as notas de casa área 
    for nome in nomes_areas:
        nota = int(input("Digite a nota de {}: ".format(nome)))
        areas[nome] = nota


    # Ordenar as piores áreas pela nota 
    areas_ordenadas = sorted(areas, key=areas.get)[:2]

    # Retornar os nomes das 2 áreas de menores notas
    print("As áreas de notas mais baixas são: ", areas_ordenadas )
    time.sleep(2)

    #area_negativa1 = (areas_ordenadas, key=areas_ordenadas.get)[:1]
    #area_negativa2 = (areas_ordenadas, key=areas_ordenadas.get)[:1]
    #
    funcao1 = globals()[area_negativa1]
    funcao2 = globals()[area_negativa2]
    print(funcao1())
    #
    #
    #
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
    '''
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
    '''

    escolha = input("Digite 'c' para continuar ou 's' para sair: ")
    if escolha == 'c':
        print("Continuando...")
        opcao_areas()  # Chamada da função
    elif escolha == 's':
        print("Saindo...")
        break
    else:
        print("Opção inválida. Por favor, digite 'c' para continuar ou 's' para sair.")



    
def saude():
    texto1 = """
    Faz quanto tempo que você procurou ajuda médica ?

 Você mantem um hábito alimentação saudável ? 

Você tem realizado exercícios regulares ?

Você tem feito um descanso adequado ?

Você tem um sono de qualidade, e com período adequado? 

Você acorda cansado ?
"""



def desenvolvimento_pessoal():
    texto1 ="""
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






def Carreira_Profissão():
   vtexto1 ="""
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




def relacionamentos():
   vtexto1 ="""
Você considera que sua comunicação é aberta e honesta?

você pratica empatia?

você acredita que você pratica o respeito pelas pessoas ?

você acredita que você pratica o  apoio mútuo ?

você acredita estar disposto a comprometer-se e a resolver conflitos de forma construtiva ?

você demonstra interesse genuíno nas pessoas?

você valorizar as opiniões e emoções das pessoas ?

 você está presente quando precisarem de apoio?

 você estabelece limites saudáveis?

você cativa a confiança e cultivar momentos de diversão e conexão?

você pratica a gentileza e a gratidão no dia a dia?
( pois pequenos gestos podem fortalecer os laços afetivos)
"""





def financas():
   vtexto1 ="""

você tem disciplina em anotar e acompanhar seu orçamento mensal ?

você consegue fazer economia de dinheiro?

quais investimentos você já fez e prática hoje ?

você já fez algum planejamento de gestão de dívidas? 

você já estabeleceu metas financeiras claras ?

você acompanha regularmente seus gastos ?

você pesquisa sobre diferentes tipos de investimentos e diversifica sua carteira ?

você Prioriza o pagamento de dívidas de alta taxa de juros e evita acumular novas dívidas desnecessárias ?

você já considerou a possibilidade de buscar aconselhamento financeiro profissional ?

você pratica a disciplina financeira ?
"""





'''
def espiritualidade ():
   vtexto1 ="""
1. Qual é o propósito da minha vida e como minha espiritualidade pode me guiar para alcançá-lo?

2. Como posso cultivar uma conexão mais profunda comigo mesmo e com os outros?

3. Quais práticas espirituais ressoam mais comigo e como posso integrá-las à minha rotina diária?

4. Quais são os valores fundamentais que guiam minhas ações e como minha espiritualidade influencia esses valores?

5. Como posso encontrar mais significado e propósito nas experiências cotidianas?

6. Qual é o meu relacionamento com o universo ou uma força superior e como posso fortalecê-lo?

7. Como posso cultivar um estado de gratidão e aceitação em minha vida?

8. Quais são os desafios ou bloqueios que impedem o crescimento espiritual e como posso superá-los?

9. De que maneiras posso contribuir para o bem-estar dos outros e do mundo ao meu redor?

10. Como posso praticar o perdão, tanto para os outros quanto para mim mesmo, como parte do meu caminho espiritual?
"""






def diversão/lazer()
   vtexto1 ="""
1. O que me faz sentir verdadeiramente feliz e animado?

2. Quais são minhas paixões e interesses e como posso integrá-los mais em minha vida cotidiana?

3. Quando foi a última vez que me diverti muito e o que estava fazendo?

4. Quais atividades eu gostava de fazer quando era criança e posso trazê-las de volta à minha vida adulta?

5. Quais são os hobbies ou atividades que sempre quis experimentar e ainda não fiz?

6. Como posso reservar tempo regularmente para relaxar e desfrutar do momento presente?

7. Quais são as pequenas coisas que me trazem alegria e como posso incorporá-las mais em minha rotina?

8. Com quem eu gosto de passar tempo e como posso planejar mais atividades juntos?

9. Como posso explorar minha criatividade de maneiras novas e divertidas?

10. Quais são os lugares na minha cidade ou região que ainda não explorei e que podem ser fonte de diversão e aventura?
"""





def ambiente():
   vtexto1 ="""
1. Como me sinto em relação ao ambiente físico da minha casa? Ele me traz paz e conforto, ou sinto que precisa de melhorias?

2. Quais são as mudanças que posso fazer no meu espaço de trabalho para torná-lo mais produtivo e agradável?

3. Como posso contribuir para a preservação e sustentabilidade do meio ambiente na minha comunidade?

4. Quais são as áreas verdes ou parques na minha região que posso explorar para relaxar e conectar-me com a natureza?

5. Como posso reduzir o desperdício e adotar práticas mais ecológicas no meu dia a dia?

6. Quais são as formas de me envolver mais ativamente na minha comunidade local, seja por meio de voluntariado, atividades sociais ou grupos de interesse comum?

7. Qual é o impacto da minha rotina diária no meio ambiente e como posso fazer escolhas mais conscientes para reduzir esse impacto?

8. Como posso criar um ambiente em casa que promova o bem-estar mental e emocional, como um espaço para meditação, leitura ou relaxamento?

9. Quais são os espaços na minha cidade que ainda não explorei e que podem oferecer oportunidades de aprendizado e crescimento?

10. Como posso cultivar relacionamentos mais significativos com meus vizinhos e colegas de trabalho para promover um ambiente mais harmonioso e solidário?
"""





def Carreira_Profissão():
   vtexto1 ="""

"""






def Carreira_Profissão()
   vtexto1 ="""

"""
'''