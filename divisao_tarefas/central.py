from cadastrar_adm import cadastro_adm
from cadastrar_usuario import cadastro_usuario
from login import login_adm_user


while True:
    print(
        '___________MENU___________\n'
        '[1]Cadastrar Administrador\n'
        '[2]Login\n'
        '[3]Cadastrar usuário\n'
        '[0]Sair'
    )
    print('_'*26)
    choice = input()
    if choice == '1':
        cadastro_adm()

    elif choice == '2':
        login_adm_user()

    elif choice == '3':
        cadastro_usuario()

    elif choice == '0':
        break

    else:
        print('Não existe essa opção.')
        break
