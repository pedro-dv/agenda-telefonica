agenda = {}
while True:
    print('''--- AGENDA TELEFONICA ---
    1- adicionar contato
    2- Editar telefone
    3- Remover contato
    4- buscar contato
    5- Listar todos
    6- Sair ''')
    opcao = input('Selecione uma opcao: ')
    if opcao == '1':
        nome = input('digite seu nome:')
        if nome not in agenda:
            agenda[nome] = input(f'digite o telefone de {nome}:')
            print('Contato adicionado com sucesso!')
        else:
            print('Contato com este nome já existe!')
    elif opcao == '2':
        nome = input('qual o numero deseja editar:')
        if nome in agenda:
            agenda[nome] = input(f'Digite o novo telefone de {nome}:')
            print('contato editado com sucesso!')
        else:
            print('o contato nao existe!')
    elif opcao == '3':
        nome = input('digite o nome do contato:')
        if nome in agenda:
            del agenda[nome]
            print('Contato removido com sucesso!')
        else:
            print('o contato nao existe!')
    elif opcao == '4':
        nome = input('buscar contato :')
        if contato in agenda:
            print(f"Telefone: {agenda['nome']}")
        else:
            print('o contato nao existe!')
    elif opcao == '5':
        print('--- TODOS OS CONTATOS ---')
        for i in agenda:
            print(f'nome: {i} - telefone: {agenda[i]}')
    elif opcao == '6':
        print('voce saiu do programa!')
        break
    else:
        print('Opcao invalida!')
