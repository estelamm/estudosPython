def valida_int(pergunta, min, max):
    x = int(input(pergunta))
    while ((x < min) or (x > max)):
        x = int(input(pergunta))
    return x

#função para criação do arquivo caso ele não exista
def criaArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'wt+') #o sinal de '+' serve para criar o arquivo caso não exista
        a.close()
    except:
        print('Erro na criação do arquivo!!')
    else:
        print('Arquivo {} foi criado com sucess!! \n' .format(nomeArquivo))

#função para verificar se o arquivo existe
def existeArquivo (nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt') #r = read / t = arquivo txt
        a.close()
        #se houver algum erro, tanto na abertura como no fechamento do arquivo vai acontecer uma exceção:
    except FileNotFoundError: #para saber qual exceção aplicar no caso concreto deve-se pesquisar as exceções existentes no python.org
        return False
    else: #este else é em caso o try obtenha sucesso e seja true.
        return True

def listarArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt')
    except:
        print('erro ao ler o arquivo!!!')
    else:
        print(a.read())
    finally:
        a.close()

def cadastrarJogo (nomeArquivo, nomeJogo, nomeVideoGame):
    try:
        a = open(nomeArquivo, 'at') #escrever mas caso haja conteudo não apagar conteudo existente.
    except:
        print('Erro ao abrir o arquivo')
    else:
        a.write('{} : {} \n' .format(nomeJogo, nomeVideoGame))
        # a = nome da variavel criada no try | write = cadastrar, escrever, etc.
    finally:
        a.close()


#programa principal
arquivo = 'games.txt'
if existeArquivo(arquivo): #caso resulte verdadeiro
    print('Arquivo localizado no Computador!')
else: #caso resulte falso
    print('Arquivo Inexistente')
    criaArquivo(arquivo)

while True:
    print('MENU')
    print('1 - cadastrar novo jogo')
    print('2 - listar jogos cadastrados')
    print('3 - Sair')

    op = valida_int('escolha a opção desejada: ', 1, 3)

    if op == 1:
        print('opção de cadastrar novo jogo selecionado \n')
        nomeJogo = input('Nome do Jogo: ')
        nomeVideoGame = input('Nome do Video Game: ')
        cadastrarJogo(arquivo, nomeJogo, nomeVideoGame)
    elif op == 2:
        print('opção de listar jogos cadastrados selecionada \n')
        listarArquivo(arquivo)
    elif op == 3:
        print('encerrando programa... ')
        break