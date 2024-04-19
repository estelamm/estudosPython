lista_livro = []
id_global = 0

print('Seja bem-vindo a biblioteca virtual da Estela M. Matarredona!')
# Funçao principal que itera sobre as opçoes
def menu():
    print('-------------------- MENU PRINCIPAL --------------------')
    while True:
        menu = int(input('Insira a opção desejada: 1 - Cadastrar Livro / 2 - Consultar Livro / 3 - Remover Livro / 4 - Encerrar programa: '))
        if menu == 1:
            global id_global
            cadastrar_livro(id_global)
            id_global = id_global+1
        elif menu == 2:
            consultar_livro()
        elif menu == 3:
            idremove = int(input('Informe o ID do livro que deseja remover da lista: '))
            remover_livro(idremove)
        elif menu == 4:
            break
        else:
            print('Opção do menu inválida.')

# Cadastra o input do usuario como uma copia na lista iniciada globalmente
def cadastrar_livro(id):
    livro = {'id': id,
             'nome': input('Insira o nome do livro: '),
             'autor': input('Insira o autor do livro: '),
             'editora': input('Insira a editora do livro: ')
             }
    lista_livro.append(livro.copy())

#Menu principal de consulta de livro
def consultar_livro():
    while True:
        print('------------------- MENU DE CONSULTA LIVRO -------------------')
        menuconsulta = int(input('Qual a opção de consulta? 1 - Consultar Todos / 2 - Consultar Por ID / 3 - Consultar por Autor / 4 - Retornar ao menu: '))

        if menuconsulta == 1:
            for e in lista_livro:
                print('#############################')
                for i,j in e.items():
                    print('{}: {}'.format(i,j))

            print('#############################')
            break
        elif menuconsulta == 2:
            idbusca = int(input('Informe o ID do livro que deseja procurar: '))
            consultar_livro_id(idbusca)
        elif menuconsulta == 3:
            autorbusca = input('Informe o Autor do livro que deseja procurar: ')
            consultar_livro_autor(autorbusca)
        elif menuconsulta == 4:
            break
        else:
            print('Opção de consulta inválida.')
            continue

def remover_livro(idremove):
    encontrado = False
    for e in lista_livro:
        for i, j in e.items():
            if i == 'id' and j == idremove:
                print('Livro encontrado:')
                lista_livro.remove(e)
                encontrado = True
                break

    if not encontrado:
        print('O id {} nao foi encontrado'.format(idremove))
    print('#############################')

def consultar_livro_id(idbusca):
    for e in lista_livro:
        for i, j in e.items():
            if i == 'id' and j == idbusca:
                print('Livro encontrado:')
                # Se encontrar o livro faz outro laço for para mostrar todos os dados, senao só mostra o ID
                for k, v in e.items():
                    print('{}: {}'.format(k, v))
                print('#############################')
                return

    # Se cair aqui nao encontrou nenhum livro
    print('O livro com ID "{}" nao foi encontrado.'.format(idbusca))

def consultar_livro_autor(autorbusca):
    encontrado = False
    for e in lista_livro:
        for i, j in e.items():
            if i == 'autor' and j == autorbusca:
                encontrado = True
                print('Livro encontrado:')
                # Se encontrar o livro faz outro laço for para mostrar todos os dados, senao só mostra o Autor
                for k, v in e.items():
                    print('{}: {}'.format(k, v))
                print('#############################')


    # Se cair aqui nao encontrou nenhum livro
    if not encontrado:
        print('O livro com Autor "{}" nao foi encontrado.'.format(autorbusca))

menu()