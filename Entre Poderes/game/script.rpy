# Entre Poderes - roteiro jogável

define narrador = Character(None)
define joaquim = Character("Joaquim")
define nome_jogador = Character("[nome]")
define jaqueline = Character("Jaqueline")
define deputado = Character("Deputado")
define ministra = Character("Ministra da Educação")
define senador = Character("Senador")
define indicada = Character("Indicada ao STF")
define ana = Character("Ana")
define ministra_relatora = Character("Ministra relatora")

image bg cozinha = im.Scale("images/cozinha.png", 1280, 720)
image bg praça3poderes = im.Scale("images/praça3poderes_GeraldoMagela_AgênciaSenado.png", 1280, 720)
image bg congresso = im.Scale("images/frenteCongresso_LeonardoSá_AgênciaSenado.png", 1280, 720)
image bg comissao = im.Scale("images/comissao_KayoMagalhãesCâmaraDeputados.png", 1280, 720)
image bg senado = im.Scale("images/plenarioSenado_JeffersonRudy_AgênciaSenado.png", 1280, 720)
image bg fachada_planalto = im.Scale("images/fachadaPlanalto_PedroFrança_AgênciaSenado.png", 1280, 720)
image bg visita_planalto = im.Scale("images/visitaPlanalto_RobertoStuckertFilho_PresidenciaRepublica.png", 1280, 720)
image bg fachada_stf = im.Scale("images/fachadaSTF_FellipeSampaio_SCO_STF.png", 1280, 720)
image bg plenario_stf = im.Scale("images/plenarioSTF_FellipeSampaioSTF.png", 1280, 720)

default nome = "visitante"

screen faixa_sabatina:
    frame:
        xalign 0.5
        yalign 0.08
        padding (24, 12)
        background "#17212DDD"
        text "Sabatina na CCJ" size 34 color "#FFFFFF"

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
    jaqueline "Ah tá. Obrigada. Mais tarde eu encontro vocês. E atende o celular hoje, por favor."
    joaquim "Se ele tocar eu atendo."
    jaqueline "Ele toca. O senhor é que deixa no silencioso."
    narrador "Ouço a porta fechar. Fico mais alguns segundos olhando pro teto, até lembrar que ainda preciso levantar."

    scene bg cozinha
    with dissolve

    joaquim "Já ia lhe chamar, [nome]. Vamos fazer um passeio importante hoje."
    nome_jogador "Bom dia, vô Joaquim. Onde a gente vai e o que vamos fazer?"
    joaquim "Eu queria te ensinar um pouco sobre o trabalho que eu exercia uns anos atrás. Quem sabe você goste e siga também."
    nome_jogador "O senhor me chamou pra passear ou já tá fazendo campanha?"
    joaquim "Pra passear. Se fosse campanha, eu já tinha servido o café."
    nome_jogador "Então senta aí, candidato. Eu ainda nem peguei o pão."
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
    nome_jogador "Se fosse o laboratório da minha escola, eu ainda ia querer saber quando os computadores chegam."
    narrador "A reunião continua enquanto nós deixamos a sala."
    nome_jogador "Mudando de assunto: o Senado faz as mesmas coisas que aqui na Câmara?"
    joaquim "Não exatamente. Como fazem parte do mesmo Poder, têm várias atribuições semelhantes. Mas vamos ver uma que cabe ao Senado."

    scene bg senado
    with fade

    nome_jogador "Aqui é menor, né?"
    joaquim "Sim, porque são menos parlamentares que na Câmara."
    narrador "Na saída da galeria, escuto uma pergunta vindo de uma transmissão. Não parece discussão sobre um projeto de lei."
    show screen faixa_sabatina
    senador "A senhora foi indicada para uma vaga no Supremo. Como deve agir uma ministra se precisar julgar uma medida do governo que a indicou?"
    indicada "A indicação não pode decidir meu voto. O julgamento precisa se apoiar na Constituição, nas leis e no processo."
    hide screen faixa_sabatina
    nome_jogador "O que eles estão fazendo hoje? Uma entrevista de emprego?"
    joaquim "É uma sabatina. A pessoa indicada pelo presidente pro STF responde às perguntas dos senadores. Essa acontece na Comissão de Constituição, Justiça e Cidadania, a CCJ."
    nome_jogador "Mas não é um emprego dentro do Senado."
    joaquim "Não. É uma das formas de participação de um Poder na escolha de autoridades de outro. Depois da análise na comissão, a indicação vai à votação no Plenário do Senado."
    nome_jogador "E os deputados também votam nesse nome?"
    joaquim "Nessa escolha, não. Isso cabe ao Senado. Já um projeto de lei ordinária federal passa pelas duas Casas. Se a segunda muda o texto, ele volta à primeira para analisar as alterações."

    centered "Desafio da visita"
    menu:
        "Como se divide a escolha de um ministro do STF?"
        "O presidente indica; o Senado aprova; o presidente nomeia.":
            joaquim "Isso. A nomeação pelo presidente depende da aprovação da escolha pela maioria absoluta do Senado: mais da metade de todos os senadores."
            joaquim "A sabatina é uma etapa dessa análise. A indicação presidencial, sozinha, não põe a pessoa no cargo."
        "O presidente indica; o Senado aconselha; o presidente decide sozinho.":
            joaquim "O Senado não dá só um conselho. É preciso que mais da metade de todos os senadores aprove a escolha. Sem essa aprovação, o presidente não pode concluir aquela nomeação."
            joaquim "Por isso, indicar alguém ainda não é colocar a pessoa no STF."
        "O presidente sugere; o Senado escolhe e nomeia quem preferir.":
            joaquim "O Senado analisa o nome indicado; não escolhe outra pessoa livremente nem faz a nomeação. Se aprovar a escolha pela maioria absoluta, quem nomeia é o presidente."
            joaquim "Nenhuma das duas instituições faz tudo sozinha."

    nome_jogador "E depois ela tem que julgar a favor de quem ajudou a colocar ela lá?"
    joaquim "Não. Ela terá de exercer a função com independência. O presidente não vira chefe dela nos julgamentos."
    nome_jogador "Essa pergunta da sabatina faz mais sentido agora."
    scene bg congresso
    with dissolve
    nome_jogador "Então esse é o Poder Legislativo federal..."
    joaquim "Isso não é tudo que eles fazem, mas por hoje é o que lhe posso mostrar. Você achou interessante?"

    menu:
        "O que você responde ao avô?"
        "Sim, principalmente essa parte de cobrar explicações.":
            joaquim "Essa parte dá trabalho. A resposta que chega nem sempre responde o que foi perguntado. Mas era uma das que eu mais gostava."
        "Não muito. Acho que eu cansaria dessas reuniões.":
            joaquim "Cansa mesmo. Você não precisa gostar de trabalhar aqui pra entender o que acontece. E eu prometo que a gente vai parar pra comer."
        "Ainda não sei. É bastante coisa pra entender.":
            joaquim "É, eu tô lhe mostrando muita coisa de uma vez. Não precisa sair daqui sabendo tudo."

    joaquim "Você pode se aprofundar em outro momento ou vir aqui de novo comigo. Ho, ho, ho."
    nome_jogador "Onde vamos agora?"
    joaquim "Depois do almoço, vamos visitar o Palácio do Planalto, sede do Executivo federal."

    scene bg visita_planalto
    with fade
    centered "Depois do almoço"
    nome_jogador "Então é aqui que ficam resolvendo os problemas que o pessoal cobra lá?"
    joaquim "Algumas decisões passam por aqui. Mas o governo federal não cabe neste prédio. Tem os ministérios e muita gente trabalhando em órgãos e entidades pelo país."
    nome_jogador "Inclusive as equipes daqueles laboratórios."
    joaquim "Isso. O presidente dirige a administração federal com os ministros. Não escolhe pessoalmente cada computador que vai ser comprado."
    narrador "O celular do vô toca alto. Ele demora a achar o botão de volume."
    nome_jogador "Agora a mãe não pode reclamar que tá no silencioso."
    joaquim "É uma notícia sobre os laboratórios. Um colega me mandou depois daquela reunião. Olha aqui."
    centered "{size=+6}Presidente veta atualização semanal dos relatórios{/size}\n\nO veto atingiu o artigo sobre a frequência das atualizações. Os demais trechos foram sancionados."
    nome_jogador "Pera, é sobre aqueles computadores? Esse projeto começou por causa da reunião de hoje?"
    joaquim "Não. Esse projeto tramita há meses. A Câmara aprovou e o Senado aprovou o mesmo texto na semana passada. A reunião de hoje cobrou as entregas do programa, que já existia."
    nome_jogador "E o que significa esse “veta”?"
    joaquim "Quando recebe o projeto aprovado, o presidente pode concordar, que é sancionar, ou vetar tudo ou uma parte, se considerar inconstitucional ou contrário ao interesse público. Tem de apresentar os motivos."
    centered "O veto atingiu o artigo sobre a frequência das atualizações. Os demais trechos foram sancionados."
    nome_jogador "E quem tá esperando os computadores vai continuar sem saber de nada?"
    joaquim "O veto é a essa regra de atualização semanal. Não apaga as obrigações de transparência que já existem. E dá pra discordar da justificativa apresentada."
    nome_jogador "Eu discordaria. Se o prazo da entrega mudou, quem tá esperando precisa saber."
    joaquim "É uma cobrança razoável. Mas vamos separar sua opinião sobre o prazo da regra sobre quem decide o veto. Os deputados que queriam manter aquele artigo ainda podem fazer alguma coisa?"

    centered "Desafio da visita"
    menu:
        "Qual caminho permite decidir sobre esse veto?"
        "O STF precisa decidir se a atualização semanal é conveniente.":
            joaquim "Essa discordância sobre o veto é apreciada pelo Congresso. Não existe uma passagem obrigatória pelo STF pra escolher o prazo que parece melhor."
            joaquim "Uma questão constitucional pode chegar à Justiça por um processo adequado, mas isso é diferente desta votação do veto."
        "A Câmara pode rejeitar o veto sem participação do Senado.":
            joaquim "A Câmara participa, mas não resolve sozinha. Deputados e senadores apreciam o veto em sessão conjunta. A rejeição precisa da maioria absoluta em cada Casa, contada separadamente."
            joaquim "A aprovação só dos deputados não basta para derrubá-lo."
        "O Congresso pode manter ou rejeitar o veto, com as duas Casas.":
            joaquim "Isso. O veto vai ao Congresso. Para rejeitá-lo, é preciso o voto de mais da metade de todos os deputados e de todos os senadores, com as contagens separadas."
            joaquim "As duas Casas se reúnem em sessão conjunta. Não basta juntar todo mundo numa única soma de votos."

    nome_jogador "Então o presidente pode discordar do Congresso, e o Congresso pode rejeitar o veto dele."
    joaquim "Pode. Se o veto for rejeitado, aquele artigo segue para promulgação e publicação. Hoje, ainda não sabemos o resultado."
    nome_jogador "E os computadores?"
    joaquim "Continuam dependendo das providências da administração. Mudar uma regra de relatório não faz uma entrega acontecer. Nem dispensa o governo de explicar o atraso."
    scene bg fachada_planalto
    with dissolve
    nome_jogador "Mais ainda do que com os deputados, eu não fazia ideia de como trabalhava o Executivo."
    joaquim "É uma realidade um pouco diferente, de fato."
    nome_jogador "Eu achava que a parte dele era só executar. Mas também participa das leis."
    joaquim "Participa. Pode até apresentar projetos, nos casos previstos na Constituição. O que não pode é aprovar tudo sozinho."
    nome_jogador "Falta apenas o Judiciário, então?"
    joaquim "Isso mesmo, [nome]."

    scene bg fachada_stf
    with fade
    nome_jogador "O pessoal que trabalha aqui não chega aqui por eleições, né?"
    joaquim "Os ministros do STF, não. Lembra da indicação e da aprovação pelo Senado? Mas também há servidores de várias áreas. Nem todo mundo que trabalha no Judiciário é juiz."
    ana "Boa tarde. Podem acompanhar o grupo. Meu nome é Ana, eu vou conduzir esta parte da visita."
    nome_jogador "E pra ser juiz em outro lugar é desse jeito também?"
    ana "Não é uma regra única. O ingresso na carreira da magistratura ocorre por concurso, com formação em Direito e outros requisitos. Para os tribunais, existem formas específicas de composição, como essa do STF."
    joaquim "Eu ia acabar misturando as carreiras. Ainda bem que você perguntou."
    ana "Aqui no Supremo, a principal atribuição é guardar a Constituição. Isso inclui julgar ações que questionam se uma lei está de acordo com ela."
    nome_jogador "Mesmo depois de a lei passar pelo Congresso e pelo presidente?"
    ana "Mesmo assim. A sessão de hoje está examinando um artigo de uma lei federal sobre auxílio para estudantes."
    ana "Essa lei criou um auxílio, mas também uma regra que exclui quem publica críticas ao governo. Não estou falando de ameaça ou ofensa: é perder o benefício por discordar."
    nome_jogador "Tipo falar que a entrega dos computadores atrasou e, por isso, ficar sem auxílio?"
    ana "Exatamente. Mas este é outro programa. A lei foi aprovada, sancionada e publicada meses atrás. Um partido com representação no Congresso entrou no STF questionando esse artigo."
    joaquim "Ele está dizendo que a lei contraria a Constituição, certo?"
    ana "Sim. A ação se chama ação direta de inconstitucionalidade, ou ADI. O partido apontou violação à igualdade e à liberdade de expressão. A Constituição protege esses direitos."

    scene bg plenario_stf
    with dissolve
    narrador "Lá dentro, uma ministra lê seu voto. Eu tento acompanhar. Algumas palavras passam direto, até ela falar dos estudantes."
    ministra_relatora "O artigo questionado exclui do auxílio quem manifesta críticas ao governo. A regra não exige qualquer descumprimento das condições de estudo ou de renda."
    narrador "Olho pro vô. Ele percebe que vou perguntar alguma coisa e aponta discretamente para a saída. Esperamos o grupo voltar ao espaço da visita."
    scene bg fachada_stf
    with dissolve
    nome_jogador "É estranho ouvir uma coisa dessas como se fosse só mais um artigo."
    ana "É por isso que precisamos olhar o que a regra faz, e não só o nome da lei."
    nome_jogador "E o STF pode mexer no que os outros dois aprovaram? Parece bem poderoso."
    ana "Ele pode analisar o que foi questionado dentro da sua competência. Mas não ganha autorização para reescrever qualquer política só porque os ministros preferem outra."
    ana "Nesse caso, qual seria a tarefa do tribunal?"

    centered "Desafio da visita"
    menu:
        "O que cabe ao STF na ação descrita?"
        "Escolher novos valores para o auxílio conforme achar mais adequado.":
            ana "A questão apresentada não é qual valor seria melhor para o auxílio. É se aquela regra de exclusão viola direitos constitucionais."
            ana "Nesse processo, o STF não substitui os responsáveis pela política para redesenhá-la conforme a preferência dos ministros."
        "Examinar se a exclusão por crítica ao governo viola a Constituição.":
            ana "Isso. A ação questiona a compatibilidade daquela regra com a Constituição. Se o tribunal concluir que ela é inconstitucional, pode afastá-la, conforme a decisão."
            ana "A aprovação pelo Congresso e a sanção presidencial não impedem esse controle."
        "Confirmar a regra porque o Congresso e o presidente já a aprovaram.":
            ana "Essas aprovações não tornam a lei imune ao controle de constitucionalidade. Uma regra pode ter passado pelas duas instituições e ainda contrariar a Constituição."
            ana "O STF precisa examinar a questão apresentada no processo, não apenas confirmar o que já foi aprovado."

    ana "A gente analisa os atos dentro da competência do tribunal. Controlar um ato nos casos previstos não significa mandar em todo o outro Poder."
    joaquim "Essa eu vou guardar pra próxima vez que me perguntarem quem manda mais."
    nome_jogador "Só não diga que foi o senhor que explicou tudo sozinho."
    joaquim "Tá bem, tá bem. Obrigado pela ajuda, Ana."
    ana "Boa volta pra vocês."

    scene bg praça3poderes
    with fade
    narrador "De volta à praça, o vô finalmente para um pouco."
    nome_jogador "Agora acabou? Meu pé tá pedindo que sim."
    joaquim "Acabou. Foi bom voltar aqui com você. E então... Consegue se imaginar trabalhando nisso?"

    menu:
        "Como você se sente depois do passeio?"
        "Talvez. Fiquei com vontade de conhecer melhor esse trabalho.":
            joaquim "Eu fico contente. Mas conheça a parte difícil também. Nas minhas histórias, às vezes eu escolho só as partes boas."
        "Não me vejo nessa carreira, mas gostei de vir com o senhor.":
            joaquim "Eu também gostei. E tá tudo bem não querer seguir essa carreira."
        "Ainda não sei o que eu quero fazer.":
            joaquim "Não precisa resolver sua vida numa tarde. Eu sei que me animei demais com essa ideia."

    jaqueline "Achei vocês!"
    joaquim "Seu filho já conhece meu antigo lugar de trabalho."
    nome_jogador "Oi, mãe! Onde a senhora estava?"
    jaqueline "Numa reunião com professores e famílias. A gente está tentando reabrir a biblioteca da escola fora do horário das aulas."
    nome_jogador "O vô disse que a senhora não quis seguir os passos dele."
    jaqueline "Pra ser deputada? Não quis mesmo. Preferi ser professora. Mas continuo me metendo nas reuniões da escola e do bairro."
    joaquim "Eu queria saber de quem você herdou essa mania..."
    jaqueline "Vamos deixar essa investigação pro caminho. Eu tô com fome."
    nome_jogador "Boa. Antes que ele lembre de mais algum prédio."
    joaquim "Tá bem, por hoje chega."
    jump encerramento

label encerramento:
    scene black
    with fade
    centered "{size=+12}Fim.{/size}"
    menu:
        "Reiniciar":
            jump start
        "Créditos e fontes":
            centered "Entre Poderes\n\nRoteiro e desenvolvimento: projeto educativo\nImagens: acervo do projeto, com créditos preservados nos nomes dos arquivos."
            pause
            jump encerramento
        "Voltar ao menu":
            return
