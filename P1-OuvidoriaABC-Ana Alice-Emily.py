# Sistema de Ouvidoria desenvolvido para disciplina Programação I
# Prof. Daniel Abella
# Equipe: Ana Alice Albuquerque e Emily Gurjão

opcao = 0
manifestacoes = []

# Criando dados iniciais de teste
dadoTeste1 = '1#Alice#Elogio#banheiros limpos'
dadoTeste2 = '2#Lucas#Reclamação#não tem café'
dadoTeste3 = '3#Thiago#Sugestão#manter aulas gravadas'

# Adicionando dados testes na lista
manifestacoes.append(dadoTeste1)
manifestacoes.append(dadoTeste2)
manifestacoes.append(dadoTeste3)

while opcao != 7:
    print()
    print('Bem vindo a Ouvidoria da UniversidadeABC')
    print()
    print('1.Listar todas as manifestações')
    print('2.Listar todas as sugestões')
    print('3.Listar todas as reclamações')
    print('4.Listar todos os elogios')
    print('5.Enviar uma manifestção')
    print('6.Pesquisar protocolo por número')
    print('7.Sair')
    print()
    opcao = int(input('Qual opção deseja escolher? '))

    if opcao == 1:
        print('Listar todas as manifestações')
        for manifest in manifestacoes:
            manifestQuebrado = manifest.split('#')
            print('Código ' + manifestQuebrado[0] + ' - ' + 'Tipo ' + manifestQuebrado[2] + ' - ' + 'Requisitante ' + manifestQuebrado[1] + ' - ' + 'Descrição ' +
                manifestQuebrado[3])

    elif opcao == 2:
        print('Listar todas as sugestões')
        for manifest in manifestacoes:
            manifestQuebrado = manifest.split('#')
            if manifestQuebrado[2] == 'Sugestão':

                print('Código ' + manifestQuebrado[0] + ' - ' + 'Requisitante ' + manifestQuebrado[1] + ' - ' + 'Descrição ' + manifestQuebrado[3])

    elif opcao == 3:
        print('Listar todas as reclamações')
        for manifest in manifestacoes:
            manifestQuebrado = manifest.split('#')
            if manifestQuebrado[2] == 'Reclamação':

                print('Código ' + manifestQuebrado[0] + ' - ' + 'Requisitante ' + manifestQuebrado[1] + ' - ' + 'Descrição ' + manifestQuebrado[3])

    elif opcao == 4:
        print('Listar todos os elogios')
        for manifest in manifestacoes:
            manifestQuebrado = manifest.split('#')
            if manifestQuebrado[2] == 'Elogio':
                print('Código ' + manifestQuebrado[0] + ' - ' + 'Requisitante ' + manifestQuebrado[1] + ' - ' + 'Descrição ' + manifestQuebrado[3])

    elif opcao == 5:
        print('Enviar uma manifestação')

        nome = input('Digite o nome do requisitante:  ')
        tipo = int(input('Digite o tipo [1.Reclamação, 2.Sugestão, 3.Elogio]: '))
        tipoMani = ''
        if tipo == 1:
            tipoMani = 'Reclamação'
        elif tipo == 2:
            tipoMani = 'Sugestão'
        elif tipo == 3:
            tipoMani = 'Elogio'

        descricao = input('Digite a descrição: ')
        protocolo = len(manifestacoes) + 1

        manifest = str(protocolo) + '#' + nome + '#' + tipoMani + '#' + descricao
        manifestacoes.append(manifest)
        print()
        print('Manifestação cadastrada com sucesso!')

    elif opcao == 6:
        print('Pesquisar protocolo por número')
        pesquisar = int(input('Digite o número do protocolo: '))

        achouRegistro = 'false'
        for manifest in manifestacoes:
            manifestQuebrado = manifest.split('#')
            if manifestQuebrado[0] == str(pesquisar):
                print('Código ' + manifestQuebrado[0] + ' - ' + 'Requisitante ' + manifestQuebrado[1] + ' - ' + 'Descrição ' +
                    manifestQuebrado[3])
                achouRegistro = 'true'
        if achouRegistro == 'false':
            print('Não existe manifestação cadastrada com o código informado.')

    elif opcao == 7:
        print('Sessão encerrada. Obrigado por utilizar nossa plataforma!')
        break

    else:
        print('Entrada inválida')

    print()
    pergunta = int(input('Deseja retornar ao menu? [1-Sim, 2-Não] '))
    if pergunta == 2:
        opcao = 7
        print('Sessão encerrada. Obrigado por utilizar nossa plataforma!')
    while pergunta < 1 or pergunta > 2:
        print('Opção inválida, escolha uma opção válida.')
        pergunta = int(input('Deseja retornar ao menu? [1-Sim, 2-Não] '))
        if pergunta == 2:
            opcao = 7
            print('Sessão encerrada. Obrigado por utilizar nossa plataforma!')

