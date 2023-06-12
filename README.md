# voting_sys_simulator
Voting system simulator developed in my first semester of college.

Original project guidelines (in portuguese):
PROJETO PRÁTICO
SIMULADOR DE UM SISTEMA DE VOTAÇÃO
OBJETIVO: Este projeto tem como objetivo aplicar o conteúdo trabalhado durante o semestre na disciplina de Algoritmos e Programação I e consolidar o aprendizado dos conceitos nela abordados. Para tal, simularemos um sistema de votação simplificado, que compreende o cadastro dos candidatos e eleitores; processo da apuração, além da emissão de relatórios e dados estatísticos.
Ao ser iniciado, o programa da Urna Eletrônica apresenta um menu principal interativo, através do qual o usuário pode selecionar as diferentes operações do sistema, A Figura 1 ilustra a tela principal com o menu de opções disponíveis.
O término da execução do programa ocorre somente quando o usuário digita a opção 6 e confirma que deseja encerrar, no final do expediente de votação por exemplo. Para todas as demais escolhas do menu, após realizar tarefa apontada, o programa retorna para a tela principal reexibindo o menu e ficando pronto para uma nova interação do usuário.
Cada opção escolhida dispara uma sequência de operações responsável por realizar a tarefa especificada. Assim, de acordo com a escolha, uma função específica deve ser invocada para desempenhar a ação correspondente. O código deverá ser estruturado e organizado em funções separadas, de acordo com o menu.
A seguir são apresentadas descrição básicas da tarefa que cada item do menu deve realizar:
1. Cadastrar Candidatos
Ler o Nome, Número, Partido e Cargo que disputa e adicionar em uma lista. Devemos ter uma lista dos candidatos a presidente, outra dos candidatos a governador e outra para prefeito.
Após cada inserção, o programa deve perguntar se deseja inserir outro candidato ou não. O cadastro deve ser interrompido quando o usuário digitar NÃO nesta opção.
2. Cadastrar Eleitores
Ler o Nome e CPF e adicionar em uma lista de eleitores.
Após cada inserção, o programa deve perguntar se deseja inserir outro eleitor ou não. O cadastro deve ser interrompido quando o usuário responder digitando NÃO.
3. Votar
Os votos são coletados em 3 etapas: Prefeito -> Governador -> Presidente; ou seja, primeiramente o voto para Prefeito, em seguida para Governador e por fim para Presidente.
A informação de cada voto é dada a partir da entrada, considerando o seguinte esquema:
Voto para um candidato em particular: número do candidato o Voto branco: digitar -1
Voto nulo: digitar -2
Em cada uma das etapas (Prefeito -> Governador -> Presidente), após a entrada do número do candidato, a urna eletrônica deve mostrar o nome do candidato, seu partido e pedir uma confirmação do voto. No caso de voto nulo ou branco uma mensagem adequada de confirmação também é apresentada.
Cada voto é então registrado nas listas de candidatos para que seja feita posteriormente a apuração do total de votos.
4. Apurar Resultados
Mostra quem são os candidatos vencedores para cada cargo, e
Apresenta um ranking ordenado do resultado da eleição (do mais votado para o menos), separado por cargo, além de alguns dados estatísticos conforme o exemplo dado na Figura 2.
Dica: Pense em uma formatação estilo tabela para a apresentação do ranking.
5. Relatório e Estatísticas
Exibi uma lista dos eleitores que votaram, ordenados por nome.
Verifica se a quantidade de eleitores bate com o total de votos que foram registrados na
eleição (auditoria)
Mostra qual partido elegeu mais políticos
Mostra qual partido elegeu menos políticos
INFORMAÇÕES ADICIONAIS E ORIENTAÇÕES:
O projeto será AVALIADO de acordo com os seguintes critérios:
Completude, clareza e ausência de erros de linguagem no relatório;
Funcionamento correto do menu e suas funcionalidades;
O trabalho deve ser desenvolvido na linguagem Python;
O quão fiel é o programa quanto à descrição do enunciado;
Indentação, comentários e legibilidade do código;
Clareza na nomenclatura de variáveis e funções;
Qualidade e completude do conteúdo do relatório;
Apresentação realizada com clareza, conhecimento e cumprimento do tempo estabelecido.
Observações:
O trabalho pode ser feito em grupo (máximo 2 pessoas).
Um único aluno do grupo deverá publicar o trabalho no Moodle.
O trabalho será apresentado em sala para todos assistirem (se tivermos tempo hábil no cronograma)
Deverá ser entregue um relatório no formato PDF contendo:
Dados dos integrantes do grupo (nome e TIA).
Decisões relativas à implementação
Printscreen com os testes de execução de todas as opções do Menu.
O relatório deve conter ao seu final um Apêndice contendo o código fonte desenvolvido.
