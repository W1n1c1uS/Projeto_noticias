from rADM import *


def menu_adm(all_news, body_news, data_news):
    while True:
        print('_' * 26)
        print(
            '[1]Inserir notícia\n'
            '[2]Listar notícias\n'
            '[3]Excluir notícia\n'
            '[4]Editar notícia\n'
            '[5]Buscar notícia\n'
            '[6]Logout'
        )
        print('_' * 26)
        choice = input()
        if choice == '1':
            adm_insert_news(all_news, body_news, data_news)

        elif choice == '2':
            adm_list_news(all_news, body_news)

        elif choice == '3':
            adm_remove_news(all_news, body_news)

        elif choice == '4':
            adm_edit_news(all_news, body_news)

        elif choice == '5':
            adm_search_news(all_news, body_news)

        elif choice == '6':
            break

        else:
            print('Não existe esse opção.')
