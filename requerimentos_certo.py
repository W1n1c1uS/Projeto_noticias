adms = []
cpfADMs = []
emailADMs = []
passwordADMs = [12345]
users = []
emailUSER = []
passwordUSER = []
all_news = {}
while True:
    print('-----------MENU-----------')
    print('[1]Cadastrar Administrador')
    print('[2]Login')
    print('[3]Cadastrar usuário')
    print('[0]Sair')
    print('-'*26)
    choice = input()
    if choice == '1':
        name = input('Nome:')
        usuario = input('Crie um usuário:')
        if usuario in adms or usuario in users:
            print('Usuario existente, cadastre outro')
        else:
            adms.append(usuario)
            cpf = int(input('CPF:'))
            if len(str(cpf)) == 11:
                cpfADMs.append(cpf)
                email = input('Informe um e-mail:')
                emailADMs.append(email)
                password = int(input('Crie uma senha:'))
                if len(str(password)) > 4:
                    passwordADMs.append(password)
                    print('Cadastro concluído.')
                else:
                    print('A senha precisa possuir mais de 4 dígitos.')
            else:
                print('CPF inválido.')
    elif choice == '2':
        usuario = input('Usuário:')
        password = int(input('Senha:'))
        logged = False
        if usuario in adms and password in passwordADMs:
            logged = True
            while True:
                print('-'*26)
                print(
                    '[1]Inserir notícia\n'
                    '[2]Listar notícias\n'
                    '[3]Excluir notícia\n'
                    '[4]Editar notícia\n'
                    '[5]Buscar notícia\n'
                    '[6]Logout'
                )
                print('-'*26)
                choice = input()
                if choice == '1':
                    while True:
                        news_id = int(input('Crie um ID para a sua notícia:'))
                        for i in all_news.keys():
                            if i == news_id:
                                print('Você não pode informar o mesmo ID:')
                                news_id = int(input('Crie um outro ID:'))

                        news = input('Insira sua notícia:')
                        all_news[news_id] = [news]
                        yes_or_no = input('Ainda quer inserir notícias? sim/nao')
                        if yes_or_no == 'nao':
                            break

                elif choice == '2':
                    for i in all_news:
                        print(all_news[i])

                elif choice == '3':
                    while True:
                        question = int(input('Qual noticia deseja remover:'))
                        if question in all_news:
                            all_news.pop(question)
                        else:
                            print('Digite algo válido!!')
                        question2 = input('Ainda quer remover uma noticia? sim/nao')
                        if question2 == 'nao':
                            break
                elif choice == '4':
                    while True:
                        question3 = int(input('Qual noticia deseja editar:'))
                        if question3 in all_news:
                            all_news.pop(question3)
                            question4 = input('DIgite o que deseja:')
                            all_news[question3] = [question4]
                            yes_no = input('Deseja editar mais alguma coisa? sim/nao')
                            if yes_no =='nao':
                                break

                    print('Aguarde futuras atualizações.')
                elif choice == '5':
                    while True:
                        all_or_not = input('Notícia(N) ou Sair(S):')
                        if all_or_not =='N':
                            list_news = int(input('Qual id da notícia:'))
                            if list_news in all_news:
                                print(all_news[list_news])
                        elif all_or_not == 'S':
                            break
                        else:
                            print('Digite algo válido')
                    print('Aguarde futuras atualizações.')
                elif choice == '6':
                    break
                else:
                    print('Não existe esse opção.')
        elif usuario in users and password in passwordUSER:
            logged = True
            while True:
                print('-'*26)
                print(
                    '[1]Buscar notícia\n'
                    '[2]Comentar notícia\n'
                    '[3]Curtir notícia\n'
                    '[4]Logout\n'
                )
                print('-' * 26)
                choice = input()
                if choice == '1':
                    print('Aguarde futuras atualizações.')
                elif choice == '2':
                    print('Aguarde futuras atualizações.')
                elif choice == '3':
                    print('Aguarde futuras atualizações.')
                elif choice == '4':
                    break
                else:
                    print('Não existe essa opção.')

        else:
            print('Usuário ou senha incorretos')
    elif choice == '3':
        name = input('Nome:')
        usuario = input('Crie um usuário:')
        if usuario in adms or usuario in users:
            print('Usuário repetido, cadastre outro.')
        else:
            users.append(usuario)
            email = input('Informe seu e-mail:')
            emailUSER.append(email)
            password = int(input('Crie uma senha:'))
            if len(str(password)) > 4:
                passwordUSER.append(password)
                print('Cadastro concluído:')
            else:
                print('A senha precisa possuir mais de 4 dígitos.')
    elif choice == '0':
        break
    else:
        print('Não existe essa opção.')
        break