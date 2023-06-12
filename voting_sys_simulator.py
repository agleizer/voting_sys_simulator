#FUNÇÕES PARA FUNCIONAMENTO DA URNA
def telaInicial(): #apresenta as opções e retorna a opção selecionada
    libera = 0
    print("\n")
    print("+++++ MENU - SIMULADOR DO SISTEMA DE VOTAÇÃO +++++")
    print("          1. Cadastrar candidatos.")
    print("          2. Cadastrar eleitores.")
    print("          3. Votar.")
    print("          4. Apurar resultados.")
    print("          5. Relatório e estatísticas.")
    print("          6. Encerrar.")
    print("\n")
    while libera == 0:
        opcao = int(input("          Selecione a opção desejada: "))
        if opcao < 1 or opcao > 6:
            print("          Opção inválida.")
        else:
            libera = 1
            return opcao
#telaInicial()

def cadastroCand(): #módulo de cadastro dos candidatos
    global cargos #a lista cargos é global e é utilizada em diversas funções
    print("\n")
    print("+++++ MÓDULO DE CADASTRO DE CANDIDATOS +++++")
    candidatos = [] #criação de lista de candidatos
    maisum = 0 #variável para o loop iterar enquanto quisermos adicionar mais um candidato
    cand = 0 #variável para podermos criar uma sublista para cada candidato
    while maisum == 0:
        candidatos.append([]) #criação de sublista para o candidato
        candidatos[cand].append(input("Nome do candidato: ")) #inserção de dados na sublista de indíce == cand
        candidatos[cand].append(input("Código do candidato: "))
        candidatos[cand].append(0) #espaço para posterior contagem de votos
        candidatos[cand].append(input("Partido do candidato: ").upper())
        cargo = input("Cargo do candidato: ").lower() #cargos é inserido na lista por intermedio de uma variavel para também podermos poular a lista global "cargos"
        candidatos[cand].append(cargo)
        if cargo not in cargos: #add cargo na lista global cargos SE JÁ NAO ESTIVER LÁ
            cargos.insert(0,cargo) #sempre adicionar o cargo mais recente no início da lista! Sem isso, contabilização de votos não funciona
        verificacaoMaisUm = 0 # variavel para loop perguntando se quer adicionar mais um candidato
        while verificacaoMaisUm == 0:
            maisum_str = input("Deseja cadastrar mais um candidato? ").lower() #deseja cadastrar retorna uma string para uso mais fácil do programa
            if maisum_str == "s" or maisum_str == "sim":
                maisum = 0 #mantemos a condição para o loop rodar
                cand += 1 # adicionamos 1 ao valor de cand, para acessar a sublista seguinte quando o loop recomeçar
                verificacaoMaisUm = 1 #sai do loop 2
            elif maisum_str == "n" or maisum_str == "não": #criação de candidatos brancos e nulos com os cargos existentes na lista global cargos
                for i in range(0,len(cargos)):
                    candidatos.append(["Branco","-1",0,"-",cargos[i]]) #cria candidato branco
                    candidatos.append(["Nulo","-2",0,"-",cargos[i]]) #cria candidato nulo
                    verificacaoMaisUm = 1 #sai do loop 2
                maisum = 1 # senão, saímos do loop 1
            else:
                print("Opção inválida.")
    #print(cargos) #print para teste
    #print(candidatos) #print para teste
    return candidatos #retorna a lista criada
#cadastroCand()

def imprimirOpcoes(listaCandidatos,cargo): #função para uso no módulo de votação. imprime em tela os candidatos a determinado cargo
    print("Candidatos a",cargo)
    for i in range(0,len(listaCandidatos)):
        if listaCandidatos[i][4] == cargo:
            print("Candidato: %s    Partido: %s    Código: %s"%(listaCandidatos[i][0],listaCandidatos[i][3],listaCandidatos[i][1]))
#imprimirOpcoes(listaCandidatos,"Presidente")

def cadastroEleitor(): #módulo de cadastro dos eleitores
    print("\n")
    print("+++++ MÓDULO DE CADASTRO DE ELEITORES +++++")
    eleitores = [] #criação de lista de eleitores
    maisum = 0 #variável para loop rodar enquanto quisermos adicionar mais um eleitor
    eleit = 0 #variável para criar uma sublista para cada eleitor
    while maisum == 0: #se maisum == 0
        eleitores.append([]) #criação de sublista para o eleitor
        eleitores[eleit].append(input("Nome do eleitor: ")) #inserção de dados na sublista de indíce == eleit
        eleitores[eleit].append(input("CPF do eleitor: "))
        verificacaoMaisUm = 0 # variavel para loop perguntando se quer adicionar mais um candidato
        while verificacaoMaisUm == 0:
            maisum_str = input("Deseja cadastrar mais um eleitor? ").lower() #deseja cadastrar retorna uma string para uso mais fácil do programa
            if maisum_str == "s" or maisum_str == "sim": #se string == sim ou s
                maisum = 0 #mantemos a condição para o loop rodar
                eleit += 1 # adicionamos 1 ao valor de eleit, para acessar a sublista seguinte quando o loop recomeçar
                verificacaoMaisUm = 1 #sai do loop 2
            elif maisum_str == "n" or maisum_str == "não": #se string == sim ou s
                maisum = 1 # senão, saímos do loop
                verificacaoMaisUm = 1 #sai do loop 2
            else:
                print("Opção inválida.")
    #print(eleitores) #print para teste
    return eleitores #retorna a lista criada
#cadastroEleitor()

def votacao(listaCandidatos): #módulo de votação
    global votosTotais
    print("\n")
    print("+++++ MÓDULO DE VOTAÇÃO +++++")
    votos = [] #criação de lista de votos
    maisum = 0 #variável para loop rodar enquanto quisermos adicionar mais um voto
    voto = 0 #variável para criar uma sublista para cada voto
    while maisum == 0: #se maisum == 0
        votos.append([]) #criação de sublista para o voto
        votos[voto].append(input("CPF do eleitor: ")) #inserção de dados na sublista de indíce == voto
        for i in cargos: #pede voto para cada cargo na lista global
            imprimirOpcoes(listaCandidatos,i)
            confirmar = 0
            while confirmar == 0:
                seuVoto = input("Seu voto (código): ")
                print("Você digitou",seuVoto)
                aceitar = input("Confirmar? ").lower()
                if aceitar == "s" or aceitar == "sim":
                    votos[voto].append(seuVoto)
                    confirmar = 1
                elif aceitar == "n" or aceitar == "não":
                    confirmar = 0
                else:
                    print("Opção inválida.")
        verificacaoMaisUm = 0 # variavel para loop perguntando se quer adicionar mais um candidato
        while verificacaoMaisUm == 0:
            maisum_str = input("Deseja cadastrar mais um voto? ").lower() #deseja cadastrar retorna uma string para uso mais fácil do programa
            votosTotais += 1
            if maisum_str == "s" or maisum_str == "sim": #se string == sim ou s
                maisum = 0 #mantemos a condição para o loop rodar
                voto += 1 # adicionamos 1 ao valor de voto, para acessar a sublista seguinte quando o loop recomeçar
                verificacaoMaisUm = 1 #sai do loop 2
            elif maisum_str == "n" or maisum_str == "não": #se string == sim ou s
                maisum = 1 # senão, saímos do loop
                verificacaoMaisUm = 1 #sai do loop 2
            else:
                print("Opção inválida.")
    #print(votos) #print para teste
    return votos #retorna a lista criada
#votacao(listaCandidatos)

def contaVotos(listaCandidatos,listaVotos): #add numero de votos na lista de candidatos. SEM GUI
    for i in range(0,len(listaCandidatos)): #percorre lista de candidatos
        for j in range(0,len(listaVotos)): #percorre lista de votos
            for k in range(0,len(cargos)): #percorre lista de cargos - 1 (placeholder)
                #print("checando se",listaCandidatos[i][1],"==",listaVotos[j][1+k],"e se",cargos[k],"==",listaCandidatos[i][4])
                if listaCandidatos[i][1] == listaVotos[j][1+k] and cargos[k] == listaCandidatos[i][4]:
                    listaCandidatos[i][2] += 1 #se for igual, contabiliza o voto
    #print(listaCandidatos)
    return listaCandidatos
#contaVotos(listaCandidatos,listaVotos)

def ordenacaoVencedores(listaCandidatosContabilizada): #funçao ordena a lista de candidatos já com votos contabilizados do maior para o menor usando selection sort
    #print("lista original: ",listaCandidatosContabilizada) #para testes apenas
    for i in range(0,len(listaCandidatosContabilizada)): #verificar todos os elementos da lista
        indiceMax = i #assumir que o elemento atual é o maior
        for j in range(i+1,len(listaCandidatosContabilizada)): #verificar todos os números DEPOIS do i atual (tudo antes disso já deveria estar ordenado)
            if listaCandidatosContabilizada[j][2] > listaCandidatosContabilizada[indiceMax][2]: #se o valor em j for menor do que o valor de menor atual
                indiceMax = j #entao o maximo = j
        #agora que sabemos o indíce do maior elemento dessa passagem, substituir de lugar com i
        listaCandidatosContabilizada[i], listaCandidatosContabilizada[indiceMax] = listaCandidatosContabilizada[indiceMax], listaCandidatosContabilizada[i] #inversão dos valores, SUBSTITUIÇÃO DE LUGAS DAS SUBLISTAS INTEIRAS!
        #print("passagem",i,"lista =",listaCandidatosContabilizada) #para testes apenas
    return listaCandidatosContabilizada
#print(ordenacaoVencedores(contaVotos(listaCandidatos,listaVotos)))

def impressaoResultados(listaCandidatosOrdenada,cargo): #impressão da lista de candidatos ORDENADA na ordem de quem ganhou
    print("\n")
    print("+++++ MÓDULO DE RESULTADOS +++++")
    print("++ Resultados para",cargo,"++")
    global partidosEleitos
    posicao = 1 #variavel para posição no ranking
    #votosTotais = 8 # !!!!!!! declaração aqui é para testes apenas. é uma variável GLOBAL, a função "votacao" PRECISA rodar para não ser = 0    !!!!!!! <<<<<<<
    votosValidos = 0
    votosBrancos = 0
    votosNulos = 0
    addPartido = 0 #só add partido do vencedor na lista dos vencedores de essa var for = a 0
    for i in range(0,len(listaCandidatosOrdenada)): #loop para analisar a lista de candidatos com votos já contabilizados e ordenada E CONTABILIZAR QTD DE VOTOS
        if listaCandidatosOrdenada[i][4] == cargo and listaCandidatosOrdenada[i][0] != "Nulo" and listaCandidatosOrdenada[i][0] != "Branco": #loop para contar votos válidos
            votosValidos += listaCandidatosOrdenada[i][2]
        if listaCandidatosOrdenada[i][4] == cargo and listaCandidatosOrdenada[i][0] == "Branco": #loop para contar votos brancos
            votosBrancos += listaCandidatosOrdenada[i][2]
        if listaCandidatosOrdenada[i][4] == cargo and listaCandidatosOrdenada[i][0] == "Nulo": #loop para contar votos nulos
            votosNulos += listaCandidatosOrdenada[i][2]
        if listaCandidatosOrdenada[i][4] == cargo and addPartido == 0 and listaCandidatosOrdenada[i][0] != "Nulo" and listaCandidatosOrdenada[i][0] != "Branco": #append partido do vencedor na lista de vencedores:
            partidosEleitos.append(listaCandidatosOrdenada[i][3])
            addPartido = 1
    #print(partidosEleitos)
    percVotosValidos = votosValidos/votosTotais*100
    percVotosNulos = votosNulos/votosTotais*100
    percVotosBrancos = votosBrancos/votosTotais*100
    tabela = [["POSIÇÃO",'NOME','PARTIDO','VOTOS TOTAIS','PERC. VOTOS VÁLIDOS']]
    for row in tabela:
        print('| {:^10} | {:^10} | {:^10} | {:^15} | {:^20} |'.format(*row))
    for i in range(0,len(listaCandidatosOrdenada)): #loop para analisar a lista de candidatos com votos já contabilizados e ordenada E IMPRIMIR RESULTADOS
        if listaCandidatosOrdenada[i][4] == cargo and listaCandidatosOrdenada[i][0] != "Nulo" and listaCandidatosOrdenada[i][0] != "Branco": #analisa e imprime infos de cada candidato do cargo correto
            tabela = [[posicao,listaCandidatosOrdenada[i][0],listaCandidatosOrdenada[i][3],listaCandidatosOrdenada[i][2],listaCandidatosOrdenada[i][2]/votosValidos*100]]
            for row in tabela:
                print('| {:^10} | {:^10} | {:^10} | {:^15} | {:^20} |'.format(*row))
            #print("Posição: %d    %s    Partido: %s    Votos totais: %d     Percentagem votos: %.2f" %(posicao,listaCandidatosOrdenada[i][0],listaCandidatosOrdenada[i][3],listaCandidatosOrdenada[i][2],listaCandidatosOrdenada[i][2]/votosValidos*100),"%")
            posicao += 1
    print("Total de votos válidos:",votosValidos,"(%.2f%%)"%percVotosValidos)
    print("Total de votos nulos:",votosNulos,"(%.2f%%)"%percVotosNulos)
    print("Total de votos brancos:",votosBrancos,"(%.2f%%)"%percVotosBrancos)
    print("Total de votos:",votosTotais)
#impressaoResultados(ordenacaoVencedores(contaVotos(listaCandidatos,listaVotos)),"presidente")

def maisGanhou(lista):
    ContNumRepeticoes = 0 #comecamos em 0, pois vai aumentar
    maisAparece = lista[0] #assim como na ordenação, vamos assumir que o elemento que mais aparece é o 0
    for i in lista:
        ContNumRepeticoesLOOP = lista.count(i)
        if ContNumRepeticoesLOOP > ContNumRepeticoes:
            ContNumRepeticoes = ContNumRepeticoesLOOP
            maisAparece = i
    #print(maisAparece)
    return maisAparece
#maisGanhou(partidosEleitos)

def menosGanhou(lista):
    ContNumRepeticoes = len(lista) #comecamon no tamanho da lista, pois é o máximo possível
    menosAparece = lista[0] #assim como na ordenação, vamos assumir que o elemento que menos aparece é o 0
    for i in lista:
        ContNumRepeticoesLOOP = lista.count(i)
        if ContNumRepeticoesLOOP < ContNumRepeticoes:
            ContNumRepeticoes = ContNumRepeticoesLOOP
            menosAparece = i
    #print(menosAparece)
    return menosAparece
#menosGanhou(partidosEleitos)

def relEstat(votos,eleitores,partidosEleitos):
    print("\n")
    print("+++++ MÓDULO DE RELATÓRIOS E ESTATÍSTICAS +++++")
    #verificação dos eleitores que votaram
    eleitoresVotaram = "" #string para guardar nomes dos eleitores que votaram
    for i in range(0,len(votos)):
        for j in range(0,len(eleitores)):
            if votos[i][0] == eleitores[j][1]:
                eleitoresVotaram += eleitores[j][0] + " "
    print("Eleitores que votaram:",eleitoresVotaram)
    #auditoria numero de votos
    print("Número de eleitores cadastrados: ",len(eleitores))
    print("Número de votos contabilizados:",votosTotais)
    if len(eleitores) == votosTotais:
        print("Nenhuma discrepância detectada.")
    elif len(eleitores) > votosTotais:
        print("Atenção: %d eleitor(es) não compareceram ou não tiveram seus votos contabilizados."%(len(eleitores)-votosTotais))
    else:
        print("POSSÍVEL FRAUDE: %d voto(s) não cadastrado(s) foram contabilizados."%(votosTotais-len(eleitores)))
    #estatísticas partidos
    print("Partido que elegeu mais políticos:",maisGanhou(partidosEleitos),"(",partidosEleitos.count(maisGanhou(partidosEleitos)),")")
    print("Partido que elegeu menos políticos:",menosGanhou(partidosEleitos),"(",partidosEleitos.count(menosGanhou(partidosEleitos)),")")
#relEstat(listaVotos,listaEleitores,partidosEleitos)

#EXECUÇÃO PROGRAMA
#variáveis globais (não é ideal, mas iremos usar algumas globais para exemplificar a passagem de parâmetros por referência)
votosTotais = 0 #contagem votos totais
cargos = [] #os diferentes cargos cadastrados no módulo de cadastro de candidatos
partidosEleitos = [] #os primeiros colocados de cada cargo

opcao = telaInicial()
while opcao != 6:
    if opcao == 1:
        candidatos = cadastroCand()
        opcao = telaInicial()
    elif opcao == 2:
        eleitores = cadastroEleitor()
        opcao = telaInicial()
    elif opcao == 3:
        votos = votacao(candidatos)
        opcao = telaInicial()
    elif opcao == 4:
        votosContabilizados = contaVotos(candidatos,votos)
        votosOrdenados = ordenacaoVencedores(votosContabilizados)
        for i in range(0,len(cargos)):
            impressaoResultados(votosOrdenados,cargos[i])
        opcao = telaInicial()
    elif opcao == 5:
        relEstat(votos,eleitores,partidosEleitos)
        opcao = telaInicial()
        
"""
#testes debug
votosTotais = 5 #contagem votos totais (1 menos que o total de eleitores)
cargos = ['prefeito', 'governador', 'presidente']  #os diferentes cargos cadastrados no módulo de cadastro de candidatos
partidosEleitos = [] #os primeiros colocados de cada cargo

opcao = telaInicial()
while opcao != 6:
    if opcao == 1:
        candidatos = [['Jose', '123', 0, 'PSD', 'presidente'], ['Maria', '124', 0, 'PST', 'presidente'], ['Mario', '256', 0, 'PST', 'governador'], ['Carla', '281', 0, 'PSD', 'governador'], ['Antonio', '456', 0, 'PEF', 'prefeito'], ['Marta', '499', 0, 'PSD', 'prefeito'], ['Branco', '-1', 0, '-', 'prefeito'], ['Nulo', '-2', 0, '-', 'prefeito'], ['Branco', '-1', 0, '-', 'governador'], ['Nulo', '-2', 0, '-', 'governador'], ['Branco', '-1', 0, '-', 'presidente'], ['Nulo', '-2', 0, '-', 'presidente']]
        opcao = telaInicial()
    elif opcao == 2:
        eleitores = [['Ariel', '1234'], ['Marcos', '5678'], ['Carla', '7654'], ['Monica', '9356'], ['Manoel', '3567'], ['Joao', '5556']]
        opcao = telaInicial()
    elif opcao == 3:
        votos = [['1234', '-2', '256', '124'], ['7654', '499', '281', '123'], ['9356', '-1', '-2', '123'], ['3567', '456', '281', '-1'], ['5556', '456', '281', '123']]
        opcao = telaInicial()
    elif opcao == 4:
        votosContabilizados = contaVotos(candidatos,votos)
        votosOrdenados = ordenacaoVencedores(votosContabilizados)
        for i in range(0,len(cargos)):
            impressaoResultados(votosOrdenados,cargos[i])
        opcao = telaInicial()
    elif opcao == 5:
        relEstat(votos,eleitores,partidosEleitos)
        opcao = telaInicial()
"""