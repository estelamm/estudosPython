#começar criando um dicionário chamado cadastro
#ele é indexado e atende por palavras chaves
cadastro = {'nome':[], 'sexo':[], 'ano':[]}

while True:
    terminar = input('Deseja cadastrar uma pessoa? (S ou N?)')
    if terminar.upper() in 'N':
        print('encerrando o programa...')
        break
    if terminar.upper() not in 'S':
        print('digite S para SIM ou N para NÃO')
        continue

    nome = input('Qual seu nome??')
    sexo = input('qual seu sexo?')
    ano = int(input('qual seu ano de nascimento?'))
    cadastro['nome'].append(nome)
    cadastro['sexo'].append(sexo.upper())
    cadastro['ano'].append(ano)

print(cadastro['nome'])
print(cadastro['sexo'])
print(cadastro['ano'])

