# Roteiro — Poderes da União

## Orientações para implementação

- `[nome]` representa o nome escolhido pelo jogador.
- As descrições de cenário e as indicações entre colchetes orientam a implementação; não são falas.
- **Narração** corresponde ao pensamento ou à percepção do protagonista.
- **Informe** corresponde a um texto lido no celular.
- **P1, P2 e P3** são escolhas pessoais, sem resposta correta.
- **E1, E2, E3 e E4** são escolhas educativas.
- Exibir somente o retorno correspondente à alternativa escolhida.
- Cada retorno termina na continuação comum indicada por **R-P1**, **R-E1** e assim por diante.
- As identificações de resposta correta ou incorreta são orientações para implementação; não devem aparecer antecipadamente no menu.
- Joaquim e Jaqueline são os personagens com sprites previstos. Os demais podem aparecer somente por nome e fala.
- Personagens, autoridades, programas e acontecimentos apresentados na história são fictícios.

## Cena 1 — Antes de sair

**Cenário:** casa de Joaquim, pela manhã. A abertura começa com a tela escura, enquanto o protagonista ainda está deitado. A cozinha só aparece depois que Jaqueline sai e ele se levanta.

[Solicitar o nome do jogador.]

**Tela:** Como você se chama?

[Armazenar o nome e utilizar `[nome]` nas falas seguintes.]

**Tela:** Esta história é fictícia. Personagens e casos foram criados para fins educativos.

**Narração:** Acordo com a voz da minha mãe vindo da cozinha.

**?** Pai, chame [nome] pra mim, tô atrasada!

**?:** O senhor viu minhas anotações da escola?

**??:** Estão embaixo da sua bolsa.

**?:** Ah, tá. Obrigada. Mais tarde eu encontro vocês. E atende o celular hoje, por favor.

**??:** Se ele tocar, eu atendo.

**?** Ele toca. O senhor é que deixa no silencioso.

**Narração:** Ouço a porta fechar. Fico mais alguns segundos olhando pro teto, até lembrar que ainda preciso levantar.

[Transição para a cozinha. Joaquim está à mesa.]

**??** Já ia lhe chamar, [nome]. Vamos fazer um passeio importante hoje.

**[nome]:**Bom dia, vô Joaquim, Onde a gente vai e o que vamos fazer?

**Joaquim:** Eu queria te ensinar um pouco sobre o trabalho que eu exercia uns anos atrás. Quem sabe você goste e siga também.

**[nome]:** O senhor me chamou pra passear ou já tá fazendo campanha?

**Joaquim:** Pra passear. Se fosse campanha, eu já tinha servido o café.

**[nome]:** Então senta aí, candidato. Eu ainda nem peguei o pão.

**Narração:** Ele já está de pé. Quando percebe que eu ainda nem peguei o pão, senta de novo.

## Cena 2 — A praça e as duas Casas

**Cenário:** Praça dos Três Poderes. Durante a conversa, o fundo muda para a fachada do Congresso Nacional.

**Joaquim:** Bem, chegamos. Agora nós estamos na Praça dos Três Poderes. Daqui dá pra ver os principais prédios dos três Poderes da nossa República.

**[nome]:** O senhor é ex-deputado federal, né? Vamos dar uma olhada por aqui hoje, então?

**Joaquim:** Isso mesmo. Veja só: o Palácio do Planalto é onde trabalha o presidente da República, que dirige o Executivo federal com os ministros.

**Joaquim:** Já ali do outro lado está o Supremo Tribunal Federal, o STF, a mais alta corte do Judiciário. E ali, onde vamos primeiro, é o Congresso, com a Câmara dos Deputados e o Senado: o Legislativo federal.

**[nome]:** Hum, parece interessante. Nunca entendi exatamente como trabalham esses setores diferentes.

**Joaquim:** E eu gostaria que você pensasse se deseja seguir o mesmo caminho do seu avô.

**[nome]:** É o quê!? Eu vim conhecer!

**Joaquim:** Bom, você não precisa decidir agora. Nem hoje. Quero que o que você vir ajude a entender melhor esse mundo.

**[nome]:** Tudo bem, então. Eu sempre tive uma certa curiosidade mesmo.

**Joaquim:** Sua mãe veio comigo quando era mais nova. Não quis seguir meus passos. Preferiu dar aula.

**[nome]:** Ela ainda dá bastante aula pro senhor, pelo visto.

**Joaquim:** Sobre o celular, principalmente. Vamos passar aqui primeiro, meu antigo local de trabalho: o Congresso.

[Mudar para a fachada do Congresso.]

### P1 — Escolha pessoal

**O que você comenta ao olhar o prédio?**

- **A.** Por que essas duas tigelas grandes?
- **B.** Era aqui que o senhor passava o dia?

### P1-A — Retorno da alternativa A

**Joaquim:** Tigelas? Ótima observação, hahaha. São as cúpulas das duas Casas. A que parece aberta pra cima é a da Câmara; a outra é a do Senado.

[Seguir para R-P1.]

### P1-B — Retorno da alternativa B

**Joaquim:** Uma boa parte dele. Mas trabalhar aqui não era ficar o tempo todo naquele salão das votações. Tinha comissão, reunião, gente procurando a gente... Você já vai ver.

[Seguir para R-P1.]

### R-P1 — Continuação comum

**Joaquim:** O Congresso tem uma estrutura que chamamos de bicameral. Isso diz respeito às duas Casas legislativas: a Câmara, com 513 deputados federais, e o Senado, com 81 senadores.

**[nome]:** É bastante gente, mas faz sentido quando a gente olha pro tamanho do nosso país.

**Joaquim:** A Câmara representa o povo. As bancadas dos estados e do Distrito Federal consideram a população, com limites de oito a setenta deputados por unidade. No Senado, cada estado e o Distrito Federal têm três representantes.

**[nome]:** Então a diferença não é só o tamanho da sala.

**Joaquim:** Não. As duas Casas participam da elaboração das leis federais e fiscalizam o Executivo, mas também têm tarefas próprias. Bom, melhor entrarmos logo. Vamos pra Câmara dos Deputados.

## Cena 3 — Cadê os computadores?

**Cenário:** sala de comissão da Câmara dos Deputados, vista da área destinada ao público. Joaquim e o protagonista acompanham uma reunião. Deputado e ministra aparecem por identificação e fala.

**Narração:** A sala não é aquela enorme que eu conhecia da televisão. Um deputado pede silêncio. Na mesa, uma mulher abre uma pasta cheia de marcações.

**[nome]:** O que tá acontecendo aqui?

**Joaquim:** É uma reunião da Comissão de Educação. Os deputados convocaram a ministra da Educação pra explicar atrasos num programa federal de renovação de laboratórios dos institutos federais.

**[nome]:** Ela trabalha pro presidente e veio responder aqui?

**Joaquim:** Veio. Essa cobrança também faz parte do trabalho dos deputados. Vamos ouvir um pouco.

**Deputado:** Ministra, o programa começou no ano passado. Há laboratórios esperando computadores há meses. O cronograma que recebemos já venceu. O que aconteceu?

**Ministra da Educação:** Parte das entregas atrasou. O ministério e as equipes responsáveis estão revendo os prazos e apurando o descumprimento dos contratos. Trouxe a relação das unidades afetadas.

**Deputado:** Precisamos dessa relação e das providências adotadas. Só anunciar outro prazo não explica o atraso.

**[nome]:** Parece reunião de trabalho em grupo quando ninguém sabe quem ficou com a parte que falta.

**Joaquim:** Com uma diferença: eles têm de prestar contas do que fazem com recursos públicos. E quem cobra aqui não é quem administra aquelas entregas.

**Joaquim:** O que você diria que os deputados estão fazendo nesta reunião?

### E1 — Escolha educativa

**Qual é a atuação da comissão nesta situação?**

- **A.** Assumir as compras para corrigir os atrasos do ministério.
- **B.** Fiscalizar o programa e cobrar explicações da ministra.
- **C.** Julgar criminalmente a ministra pelos atrasos nas entregas.

### E1-A — Retorno da alternativa A — Incorreta

**Joaquim:** As compras continuam com a administração responsável. A comissão pode cobrar documentos, explicações e providências, mas essa fiscalização não a transforma na equipe que contrata e entrega os computadores.

**Joaquim:** O problema é justamente separar quem executa de quem acompanha e cobra.

[Seguir para R-E1.]

### E1-B — Retorno da alternativa B — Correta

**Joaquim:** Isso. O Legislativo não trabalha só fazendo leis. A comissão está fiscalizando uma ação do Executivo e pode convocar a ministra pra explicar esse assunto.

**Joaquim:** Os deputados cobram; a administração continua responsável pelas entregas e pelas medidas pra corrigir o atraso.

[Seguir para R-E1.]

### E1-C — Retorno da alternativa C — Incorreta

**Joaquim:** Não é um julgamento criminal. Eles estão pedindo explicações e documentos. Isso pode revelar problemas que precisem de outras providências, mas a reunião não condena a ministra por um crime.

**Joaquim:** Aqui, a tarefa é fiscalizar a atuação do Executivo.

[Seguir para R-E1.]

### R-E1 — Continuação comum

**Deputado:** Peço que os documentos apresentados sejam disponibilizados para o acompanhamento da comissão. Passaremos às próximas perguntas.

**[nome]:** Eu não fazia ideia de que os deputados trabalhavam assim.

**Joaquim:** Pois é, [nome]. Isso é parte do dia a dia deles. Eu reclamava bastante do tamanho das reuniões... Até ser eu quem não queria largar o microfone.

**[nome]:** Se fosse o laboratório da minha escola, eu ainda ia querer saber quando os computadores chegam.

[Os dois saem da sala e voltam a conversar em volume normal.]

**[nome]:** Mudando de assunto: o Senado faz as mesmas coisas que aqui na Câmara?

**Joaquim:** Não exatamente. Como fazem parte do mesmo Poder, têm várias atribuições semelhantes. Mas vamos ver uma que cabe ao Senado.

## Cena 4 — Quem escolhe quem julga?

**Cenário:** galeria do plenário do Senado, inicialmente sem sessão em andamento. Na saída, os personagens ouvem uma transmissão de sabatina. Durante as duas falas da transmissão, exibir a faixa “Sabatina na CCJ” e identificar os falantes na caixa de diálogo. Retirar a faixa antes da pergunta do protagonista sobre uma entrevista de emprego.

**[nome]:** Aqui é menor, né?

**Joaquim:** Sim, porque são menos parlamentares que na Câmara.

**Narração:** Na saída da galeria, escuto uma pergunta vindo de uma transmissão. Não parece discussão sobre um projeto de lei.

**Senador, na transmissão:** A senhora foi indicada para uma vaga no Supremo. Como deve agir uma ministra se precisar julgar uma medida do governo que a indicou?

**Indicada ao STF, na transmissão:** A indicação não pode decidir meu voto. O julgamento precisa se apoiar na Constituição, nas leis e no processo.

**[nome]:** O que eles estão fazendo hoje? Uma entrevista de emprego?

**Joaquim:** É uma sabatina. A pessoa indicada pelo presidente pro STF responde às perguntas dos senadores. Essa acontece na Comissão de Constituição, Justiça e Cidadania, a CCJ.

**[nome]:** Mas não é um emprego dentro do Senado.

**Joaquim:** Não. É uma das formas de participação de um Poder na escolha de autoridades de outro. Depois da análise na comissão, a indicação vai à votação no Plenário do Senado.

**[nome]:** E os deputados também votam nesse nome?

**Joaquim:** Nessa escolha, não. Isso cabe ao Senado. Já um projeto de lei ordinária federal passa pelas duas Casas. Se a segunda muda o texto, ele volta à primeira para analisar as alterações.

### E2 — Escolha educativa

**Exibir antes das alternativas:** “Desafio da visita”.

**Como se divide a escolha de um ministro do STF?**

- **A.** O presidente indica; o Senado aprova; o presidente nomeia.
- **B.** O presidente indica; o Senado aconselha; o presidente decide sozinho.
- **C.** O presidente sugere; o Senado escolhe e nomeia quem preferir.

### E2-A — Retorno da alternativa A — Correta

**Joaquim:** Isso. A nomeação pelo presidente depende da aprovação da escolha pela maioria absoluta do Senado: mais da metade de todos os senadores.

**Joaquim:** A sabatina é uma etapa dessa análise. A indicação presidencial, sozinha, não põe a pessoa no cargo.

[Seguir para R-E2.]

### E2-B — Retorno da alternativa B — Incorreta

**Joaquim:** O Senado não dá só um conselho. É preciso que mais da metade de todos os senadores aprove a escolha. Sem essa aprovação, o presidente não pode concluir aquela nomeação.

**Joaquim:** Por isso, indicar alguém ainda não é colocar a pessoa no STF.

[Seguir para R-E2.]

### E2-C — Retorno da alternativa C — Incorreta

**Joaquim:** O Senado analisa o nome indicado; não escolhe outra pessoa livremente nem faz a nomeação. Se aprovar a escolha pela maioria absoluta, quem nomeia é o presidente.

**Joaquim:** Nenhuma das duas instituições faz tudo sozinha.

[Seguir para R-E2.]

### R-E2 — Continuação comum

**[nome]:** E depois ela tem que julgar a favor de quem ajudou a colocar ela lá?

**Joaquim:** Não. Ela terá de exercer a função com independência. O presidente não vira chefe dela nos julgamentos.

**[nome]:** Essa pergunta da sabatina faz mais sentido agora.

[Mudar para a fachada do Congresso.]

**[nome]:** Então esse é o Poder Legislativo federal...

**Joaquim:** Isso não é tudo que eles fazem, mas por hoje é o que lhe posso mostrar. Você achou interessante?

### P2 — Escolha pessoal

**O que você responde ao avô?**

- **A.** Sim, principalmente essa parte de cobrar explicações.
- **B.** Não muito. Acho que eu cansaria dessas reuniões.
- **C.** Ainda não sei. É bastante coisa pra entender.

### P2-A — Retorno da alternativa A

**Joaquim:** Essa parte dá trabalho. A resposta que chega nem sempre responde o que foi perguntado. Mas era uma das que eu mais gostava.

[Seguir para R-P2.]

### P2-B — Retorno da alternativa B

**Joaquim:** Cansa mesmo. Você não precisa gostar de trabalhar aqui pra entender o que acontece. E eu prometo que a gente vai parar pra comer.

[Seguir para R-P2.]

### P2-C — Retorno da alternativa C

**Joaquim:** É, eu tô lhe mostrando muita coisa de uma vez. Não precisa sair daqui sabendo tudo.

[Seguir para R-P2.]

### R-P2 — Continuação comum

**Joaquim:** Você pode se aprofundar em outro momento ou vir aqui de novo comigo. Ho, ho, ho.

**[nome]:** Onde vamos agora?

**Joaquim:** Depois do almoço, vamos visitar o Palácio do Planalto, sede do Executivo federal.

## Cena 5 — O artigo vetado

**Cenário:** fachada e interior de visitação do Palácio do Planalto, depois do almoço. Uma notícia recebida por Joaquim será apresentada como texto, sem exigir uma interface de celular.

[Transição com a indicação “Depois do almoço”.]

**[nome]:** Então é aqui que ficam resolvendo os problemas que o pessoal cobra lá?

**Joaquim:** Algumas decisões passam por aqui. Mas o governo federal não cabe neste prédio. Tem os ministérios e muita gente trabalhando em órgãos e entidades pelo país.

**[nome]:** Inclusive as equipes daqueles laboratórios.

**Joaquim:** Isso. O presidente dirige a administração federal com os ministros. Não escolhe pessoalmente cada computador que vai ser comprado.

**Narração:** O celular do vô toca alto. Ele demora a achar o botão de volume.

**[nome]:** Agora a mãe não pode reclamar que tá no silencioso.

**Joaquim:** É uma notícia sobre os laboratórios. Um colega me mandou depois daquela reunião. Olha aqui.

**Manchete:** Presidente veta atualização semanal dos relatórios

**Resumo:** O veto atingiu o artigo sobre a frequência das atualizações. Os demais trechos foram sancionados.

**[nome]:** Pera, é sobre aqueles computadores? Esse projeto começou por causa da reunião de hoje?

**Joaquim:** Não. Esse projeto tramita há meses. A Câmara aprovou e o Senado aprovou o mesmo texto na semana passada. A reunião de hoje cobrou as entregas do programa, que já existia.

**[nome]:** E o que significa esse “veta”?

**Joaquim:** Quando recebe o projeto aprovado, o presidente pode concordar, que é sancionar, ou vetar tudo ou uma parte, se considerar inconstitucional ou contrário ao interesse público. Tem de apresentar os motivos.

**Informe:** O veto atingiu o artigo sobre a frequência das atualizações. Os demais trechos foram sancionados.

**[nome]:** E quem tá esperando os computadores vai continuar sem saber de nada?

**Joaquim:** O veto é a essa regra de atualização semanal. Não apaga as obrigações de transparência que já existem. E dá pra discordar da justificativa apresentada.

**[nome]:** Eu discordaria. Se o prazo da entrega mudou, quem tá esperando precisa saber.

**Joaquim:** É uma cobrança razoável. Mas vamos separar sua opinião sobre o prazo da regra sobre quem decide o veto. Os deputados que queriam manter aquele artigo ainda podem fazer alguma coisa?

### E3 — Escolha educativa

**Exibir antes das alternativas:** “Desafio da visita”.

**Qual caminho permite decidir sobre esse veto?**

- **A.** O STF precisa decidir se a atualização semanal é conveniente.
- **B.** A Câmara pode rejeitar o veto sem participação do Senado.
- **C.** O Congresso pode manter ou rejeitar o veto, com as duas Casas.

### E3-A — Retorno da alternativa A — Incorreta

**Joaquim:** Essa discordância sobre o veto é apreciada pelo Congresso. Não existe uma passagem obrigatória pelo STF pra escolher o prazo que parece melhor.

**Joaquim:** Uma questão constitucional pode chegar à Justiça por um processo adequado, mas isso é diferente desta votação do veto.

[Seguir para R-E3.]

### E3-B — Retorno da alternativa B — Incorreta

**Joaquim:** A Câmara participa, mas não resolve sozinha. Deputados e senadores apreciam o veto em sessão conjunta. A rejeição precisa da maioria absoluta em cada Casa, contada separadamente.

**Joaquim:** A aprovação só dos deputados não basta para derrubá-lo.

[Seguir para R-E3.]

### E3-C — Retorno da alternativa C — Correta

**Joaquim:** Isso. O veto vai ao Congresso. Para rejeitá-lo, é preciso o voto de mais da metade de todos os deputados e de todos os senadores, com as contagens separadas.

**Joaquim:** As duas Casas se reúnem em sessão conjunta. Não basta juntar todo mundo numa única soma de votos.

[Seguir para R-E3.]

### R-E3 — Continuação comum

**[nome]:** Então o presidente pode discordar do Congresso, e o Congresso pode rejeitar o veto dele.

**Joaquim:** Pode. Se o veto for rejeitado, aquele artigo segue para promulgação e publicação. Hoje, ainda não sabemos o resultado.

**[nome]:** E os computadores?

**Joaquim:** Continuam dependendo das providências da administração. Mudar uma regra de relatório não faz uma entrega acontecer. Nem dispensa o governo de explicar o atraso.

[Mudar para a fachada do Planalto.]

**[nome]:** Mais ainda do que com os deputados, eu não fazia ideia de como trabalhava o Executivo.

**Joaquim:** É uma realidade um pouco diferente, de fato.

**[nome]:** Eu achava que a parte dele era só executar. Mas também participa das leis.

**Joaquim:** Participa. Pode até apresentar projetos, nos casos previstos na Constituição. O que não pode é aprovar tudo sozinho.

**[nome]:** Falta apenas o Judiciário, então?

**Joaquim:** Isso mesmo, [nome].

## Cena 6 — Uma lei pode passar do limite?

**Cenário:** fachada e espaço de visitação do STF. Durante a visita, o grupo acompanha brevemente uma sessão pela área destinada ao público. As conversas com Ana acontecem fora do plenário. A relatora já integra o STF e é uma personagem diferente da indicada apresentada no Senado.

**[nome]:** O pessoal que trabalha aqui não chega aqui por eleições, né?

**Joaquim:** Os ministros do STF, não. Lembra da indicação e da aprovação pelo Senado? Mas também há servidores de várias áreas. Nem todo mundo que trabalha no Judiciário é juiz.

**Ana:** Boa tarde. Podem acompanhar o grupo. Meu nome é Ana, eu vou conduzir esta parte da visita.

**[nome]:** E pra ser juiz em outro lugar é desse jeito também?

**Ana:** Não é uma regra única. O ingresso na carreira da magistratura ocorre por concurso, com formação em Direito e outros requisitos. Para os tribunais, existem formas específicas de composição, como essa do STF.

**Joaquim:** Eu ia acabar misturando as carreiras. Ainda bem que você perguntou.

[Antes de entrar na área destinada ao público, Ana apresenta o assunto em julgamento.]

**Ana:** Aqui no Supremo, a principal atribuição é guardar a Constituição. Isso inclui julgar ações que questionam se uma lei está de acordo com ela.

**[nome]:** Mesmo depois de a lei passar pelo Congresso e pelo presidente?

**Ana:** Mesmo assim. A sessão de hoje está examinando um artigo de uma lei federal sobre auxílio para estudantes.

**Ana:** Essa lei criou um auxílio, mas também uma regra que exclui quem publica críticas ao governo. Não estou falando de ameaça ou ofensa: é perder o benefício por discordar.

**[nome]:** Tipo falar que a entrega dos computadores atrasou e, por isso, ficar sem auxílio?

**Ana:** Exatamente. Mas este é outro programa. A lei foi aprovada, sancionada e publicada meses atrás. Um partido com representação no Congresso entrou no STF questionando esse artigo.

**Joaquim:** Ele está dizendo que a lei contraria a Constituição, certo?

**Ana:** Sim. A ação se chama ação direta de inconstitucionalidade, ou ADI. O partido apontou violação à igualdade e à liberdade de expressão. A Constituição protege esses direitos.

[Mudar para a vista do plenário pela área do público. O grupo acompanha alguns minutos em silêncio.]

**Narração:** Lá dentro, uma ministra lê seu voto. Eu tento acompanhar. Algumas palavras passam direto, até ela falar dos estudantes.

**Ministra relatora:** O artigo questionado exclui do auxílio quem manifesta críticas ao governo. A regra não exige qualquer descumprimento das condições de estudo ou de renda.

**Narração:** Olho pro vô. Ele percebe que vou perguntar alguma coisa e aponta discretamente para a saída. Esperamos o grupo voltar ao espaço da visita.

[Retomar o espaço de visitação. A conversa e a escolha acontecem fora do plenário.]

**[nome]:** É estranho ouvir uma coisa dessas como se fosse só mais um artigo.

**Ana:** É por isso que precisamos olhar o que a regra faz, e não só o nome da lei.

**[nome]:** E o STF pode mexer no que os outros dois aprovaram? Parece bem poderoso.

**Ana:** Ele pode analisar o que foi questionado dentro da sua competência. Mas não ganha autorização para reescrever qualquer política só porque os ministros preferem outra.

**Ana:** Nesse caso, qual seria a tarefa do tribunal?

### E4 — Escolha educativa

**Exibir antes das alternativas:** “Desafio da visita”.

**O que cabe ao STF na ação descrita?**

- **A.** Escolher novos valores para o auxílio conforme achar mais adequado.
- **B.** Examinar se a exclusão por crítica ao governo viola a Constituição.
- **C.** Confirmar a regra porque o Congresso e o presidente já a aprovaram.

### E4-A — Retorno da alternativa A — Incorreta

**Ana:** A questão apresentada não é qual valor seria melhor para o auxílio. É se aquela regra de exclusão viola direitos constitucionais.

**Ana:** Nesse processo, o STF não substitui os responsáveis pela política para redesenhá-la conforme a preferência dos ministros.

[Seguir para R-E4.]

### E4-B — Retorno da alternativa B — Correta

**Ana:** Isso. A ação questiona a compatibilidade daquela regra com a Constituição. Se o tribunal concluir que ela é inconstitucional, pode afastá-la, conforme a decisão.

**Ana:** A aprovação pelo Congresso e a sanção presidencial não impedem esse controle.

[Seguir para R-E4.]

### E4-C — Retorno da alternativa C — Incorreta

**Ana:** Essas aprovações não tornam a lei imune ao controle de constitucionalidade. Uma regra pode ter passado pelas duas instituições e ainda contrariar a Constituição.

**Ana:** O STF precisa examinar a questão apresentada no processo, não apenas confirmar o que já foi aprovado.

[Seguir para R-E4.]

### R-E4 — Continuação comum

**Ana:** A gente ouviu parte de um voto, não o resultado do julgamento. Se o tribunal declarar esse artigo inconstitucional, a administração terá de respeitar a decisão e seu alcance. A regra poderá ser afastada.

**[nome]:** Então não precisaria acabar com o auxílio inteiro por causa daquele artigo?

**Ana:** Não necessariamente. É possível afastar só aquela regra, mantendo o restante. Precisamos acompanhar o resultado e ler o que foi decidido.

**Joaquim:** E não foi uma etapa automática pela qual toda lei passa. Houve uma ação, proposta por quem podia apresentar.

**[nome]:** Se fosse comigo, eu poderia entrar com essa ADI?

**Ana:** Não individualmente. A Constituição define quem pode propor uma ADI, como o partido desse processo. Isso não impede você de buscar proteção judicial por uma via adequada ao seu caso, com orientação jurídica.

**Ana:** Também existem outros juízes e tribunais, com competências próprias. Nem todo conflito começa no STF ou chega até ele.

**[nome]:** Então “independentes” não quer dizer que cada um faz o que quer e ninguém pode questionar.

**Ana:** Isso. As instituições têm atribuições e limites. Controlar um ato nos casos previstos não significa mandar em todo o outro Poder.

**Joaquim:** Essa eu vou guardar pra próxima vez que me perguntarem quem manda mais.

**[nome]:** Só não diga que foi o senhor que explicou tudo sozinho.

**Joaquim:** Tá bem, tá bem. Obrigado pela ajuda, Ana.

**Ana:** Boa volta pra vocês.

## Cena 7 — De volta à praça

**Cenário:** Praça dos Três Poderes, no fim da tarde. Reutilizar o fundo da primeira visita. Jaqueline chega depois da conversa entre avô e neto. Sua atividade envolve a escola da rede pública do Distrito Federal em que trabalha.

**Narração:** De volta à praça, o vô finalmente para um pouco.

**[nome]:** Agora acabou? Meu pé tá pedindo que sim.

**Joaquim:** Acabou. Foi bom voltar aqui com você. E então... Consegue se imaginar trabalhando nisso?

### P3 — Escolha pessoal

**Como você se sente depois do passeio?**

- **A.** Talvez. Fiquei com vontade de conhecer melhor esse trabalho.
- **B.** Não me vejo nessa carreira, mas gostei de vir com o senhor.
- **C.** Ainda não sei o que eu quero fazer.

### P3-A — Retorno da alternativa A

**Joaquim:** Eu fico contente. Mas conheça a parte difícil também. Nas minhas histórias, às vezes eu escolho só as partes boas.

[Seguir para R-P3.]

### P3-B — Retorno da alternativa B

**Joaquim:** Eu também gostei. E tá tudo bem não querer seguir essa carreira.

[Seguir para R-P3.]

### P3-C — Retorno da alternativa C

**Joaquim:** Não precisa resolver sua vida numa tarde. Eu sei que me animei demais com essa ideia.

[Seguir para R-P3.]

### R-P3 — Continuação comum

**Jaqueline:** Achei vocês!

**Joaquim:** Seu filho já conhece meu antigo lugar de trabalho.

**[nome]:** Oi, mãe! Onde a senhora estava?

**Jaqueline:** Numa reunião com professores e famílias. A gente está tentando reabrir a biblioteca da escola fora do horário das aulas.

**[nome]:** O vô disse que a senhora não quis seguir os passos dele.

**Jaqueline:** Pra ser deputada? Não quis mesmo. Preferi ser professora. Mas continuo me metendo nas reuniões da escola e do bairro.

**Joaquim:** Eu queria saber de quem você herdou essa mania...

**Jaqueline:** Vamos deixar essa investigação pro caminho. Eu tô com fome.

**[nome]:** Boa. Antes que ele lembre de mais algum prédio.

**Joaquim:** Tá bem, por hoje chega.

[Os personagens saem. Transição para a tela de encerramento.]

**Tela:** Fim.

[Disponibilizar as opções “Reiniciar”, “Créditos e fontes” e “Voltar ao menu”.]
