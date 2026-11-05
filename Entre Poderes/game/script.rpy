# Entre Poderes - roteiro jogável até a comissão da Câmara

define narrador = Character(None)
define joaquim = Character("Joaquim")
define nome_jogador = Character("[nome]")
define jaqueline = Character("Jaqueline")
define deputado = Character("Deputado")
define ministra = Character("Ministra da Educação")

image bg cozinha = "images/cozinha.png"
image bg praça3poderes = "images/praça3poderes.png"
image bg congresso = "images/congresso_frente.png"
image bg comissao = "images/comissao_camara.png"

default nome = "visitante"

label start:
    scene black
    with fade

    $ nome = renpy.input("Como você se chama?", length=24).strip()
    if not nome:
        $ nome = "visitante"

    centered "{size=+8}Esta história é fictícia.{/size}\n\nPersonagens e casos foram criados para fins educativos."
    pause 1.0

    narrador "Acordo com a voz da minha mãe vindo da cozinha."
    jaqueline "Pai, chame [nome] pra mim, tô atrasada!"
    jaqueline "O senhor viu minhas anotações da escola?"
    joaquim "Estão embaixo da sua bolsa."
    jaqueline "Ah, tá. Obrigada. Mais tarde eu encontro vocês. E atende o celular hoje, por favor."
    joaquim "Se ele tocar, eu atendo."
    jaqueline "Ele toca. O senhor é que deixa no silencioso."
    narrador "Ouço a porta fechar. Fico mais alguns segundos olhando pro teto, até lembrar que ainda preciso levantar."

    scene bg cozinha
    with dissolve

    joaquim "Já ia lhe chamar, [nome]. Vamos fazer um passeio importante hoje."
    nome_jogador "Bom dia, vô Joaquim. Onde a gente vai e o que vamos fazer?"
    joaquim "Eu queria te ensinar um pouco sobre o trabalho que eu exercia uns anos atrás. Quem sabe você goste e siga também."
    nome_jogador "O senhor parece bem animado. E eu quero conhecer o lugar de tantas histórias suas!"
    joaquim "Pois então vamos logo."
    nome_jogador "Tudo bem, vô. Bora. Só deixa eu terminar o café."
    narrador "Ele já está de pé. Quando percebe que eu ainda nem peguei o pão, senta de novo."

    scene bg praça3poderes
    with fade

    joaquim "Bem, chegamos. Agora nós estamos na Praça dos Três Poderes. Daqui dá pra ver os principais prédios dos três Poderes da nossa República."
    nome_jogador "O senhor é ex-deputado federal, né? Vamos dar uma olhada por aqui hoje, então?"
    joaquim "Isso mesmo. Veja só: o Palácio do Planalto é onde trabalha o presidente da República, que dirige o Executivo federal com os ministros."
    joaquim "Já ali do outro lado está o Supremo Tribunal Federal, o STF, a mais alta corte do Judiciário. E ali, onde vamos primeiro, é o Congresso, com a Câmara dos Deputados e o Senado: o Legislativo federal."
    nome_jogador "Hum, parece interessante. Nunca entendi exatamente como trabalham esses setores diferentes."
    joaquim "E eu gostaria que você pensasse se deseja seguir o mesmo caminho do seu avô."
    nome_jogador "É o quê!? Eu vim conhecer!"
    joaquim "Bom, você não precisa decidir agora. Nem hoje. Quero que o que você vir ajude a entender melhor esse mundo."
    nome_jogador "Tudo bem, então. Eu sempre tive uma certa curiosidade mesmo."
    joaquim "Sua mãe veio comigo quando era mais nova. Não quis seguir meus passos. Preferiu dar aula."
    nome_jogador "Ela ainda dá bastante aula pro senhor, pelo visto."
    joaquim "Sobre o celular, principalmente. Vamos passar aqui primeiro, meu antigo local de trabalho: o Congresso."

    scene bg congresso
    with dissolve

    menu:
        "O que você comenta ao olhar o prédio?"
        "Por que essas duas tigelas grandes?":
            joaquim "Tigelas? Ótima observação, hahaha. São as cúpulas das duas Casas. A que parece aberta pra cima é a da Câmara; a outra é a do Senado."
        "Era aqui que o senhor passava o dia?":
            joaquim "Uma boa parte dele. Mas trabalhar aqui não era ficar o tempo todo naquele salão das votações. Tinha comissão, reunião, gente procurando a gente... Você já vai ver."

    joaquim "O Congresso tem uma estrutura que chamamos de bicameral. Isso diz respeito às duas Casas legislativas: a Câmara, com 513 deputados federais, e o Senado, com 81 senadores."
    nome_jogador "É bastante gente, mas faz sentido quando a gente olha pro tamanho do nosso país."
    joaquim "A Câmara representa o povo. As bancadas dos estados e do Distrito Federal consideram a população, com limites de oito a setenta deputados por unidade. No Senado, cada estado e o Distrito Federal têm três representantes."
    nome_jogador "Então a diferença não é só o tamanho da sala."
    joaquim "Não. As duas Casas participam da elaboração das leis federais e fiscalizam o Executivo, mas também têm tarefas próprias. Bom, melhor entrarmos logo. Vamos pra Câmara dos Deputados."

    scene bg comissao
    with fade

    narrador "A sala não é aquela enorme que eu conhecia da televisão. Um deputado pede silêncio. Na mesa, uma mulher abre uma pasta cheia de marcações."
    nome_jogador "O que tá acontecendo aqui?"
    joaquim "É uma reunião da Comissão de Educação. Os deputados convocaram a ministra da Educação pra explicar atrasos num programa federal de renovação de laboratórios dos institutos federais."
    nome_jogador "Ela trabalha pro presidente e veio responder aqui?"
    joaquim "Veio. Essa cobrança também faz parte do trabalho dos deputados. Vamos ouvir um pouco."
    deputado "Ministra, o programa começou no ano passado. Há laboratórios esperando computadores há meses. O cronograma que recebemos já venceu. O que aconteceu?"
    ministra "Parte das entregas atrasou. O ministério e as equipes responsáveis estão revendo os prazos e apurando o descumprimento dos contratos. Trouxe a relação das unidades afetadas."
    deputado "Precisamos dessa relação e das providências adotadas. Só anunciar outro prazo não explica o atraso."
    nome_jogador "Parece reunião de trabalho em grupo quando ninguém sabe quem ficou com a parte que falta."
    joaquim "Com uma diferença: eles têm de prestar contas do que fazem com recursos públicos. E quem cobra aqui não é quem administra aquelas entregas."
    joaquim "O que você diria que os deputados estão fazendo nesta reunião?"

    menu:
        "Qual é a atuação da comissão nesta situação?"
        "Assumir as compras para corrigir os atrasos do ministério.":
            joaquim "As compras continuam com a administração responsável. A comissão pode cobrar documentos, explicações e providências, mas essa fiscalização não a transforma na equipe que contrata e entrega os computadores."
            joaquim "O problema é justamente separar quem executa de quem acompanha e cobra."
        "Fiscalizar o programa e cobrar explicações da ministra.":
            joaquim "Isso. O Legislativo não trabalha só fazendo leis. A comissão está fiscalizando uma ação do Executivo e pode convocar a ministra pra explicar esse assunto."
            joaquim "Os deputados cobram; a administração continua responsável pelas entregas e pelas medidas pra corrigir o atraso."
        "Julgar criminalmente a ministra pelos atrasos nas entregas.":
            joaquim "Não é um julgamento criminal. Eles estão pedindo explicações e documentos. Isso pode revelar problemas que precisem de outras providências, mas a reunião não condena a ministra por um crime."
            joaquim "Aqui, a tarefa é fiscalizar a atuação do Executivo."

    deputado "Peço que os documentos apresentados sejam disponibilizados para o acompanhamento da comissão. Passaremos às próximas perguntas."
    nome_jogador "Eu não fazia ideia de que os deputados trabalhavam assim."
    joaquim "Pois é, [nome]. Isso é parte do dia a dia deles. Eu reclamava bastante do tamanho das reuniões... Até ser eu quem não queria largar o microfone."
    nome_jogador "Isso eu consigo imaginar."
    narrador "A reunião continua enquanto nós deixamos a sala. Fim da demonstração."

    return
