print ('Bem vindo ao Serviço de Copiadora da Estela Mackedanz')

# Função que determina o serviço
def escolha_servico():
    while True:
        servico = input('Digite o serviço desejado (DIG para digitalização, ICO para impressão colorida, IBO para impressão preto e branco, FOT para fotocópia): ')
        if servico == 'DIG':
            return 1.10
        elif servico == 'ICO':
            return 1
        elif servico == 'IBO':
            return 0.4
        elif servico == 'FOT':
            return 0.20
        else:
            print('Serviço inválido.')


def num_pagina():
    while True:
        # O try é usado para verificar se o valor é numérico
        try:
            pagina = int(input('Digite o número de páginas (limite 20000): '))
            if pagina < 20:
                return pagina
            # Aqui novamente multiplico seguindo a logica de (1 - o desconto) para aplicar o desconto
            elif (pagina >= 20 and pagina < 200):
                return pagina * 0.85
            elif (pagina >= 200 and pagina < 2000):
                return pagina * 0.8
            elif (pagina >= 2000 and pagina < 20000):
                return pagina * 0.75
            else:
                print('Não aceitamos pedidos com mais de 20000.')
        except ValueError:
            print('O valor inserido não é numérico.')

# Definição da função do serviço extra
def servico_extra():
    while True:
        # Mais uma vez o try para garantir que o extra seja um valor numérico
        try:
            extra = int(input('Deseja adicionar algum serviço extra? Digite 1 para encadernação simples / 2 para encadernação de capa dura / 0 se não quiser serviço extra: '))
            if extra == 1:
                return 15
            elif extra == 2:
                return 40
            elif extra == 0:
                return 0
            else:
                print('Insira um valor válido para o extra.')
        except ValueError:
            print('O valor inserido não é numérico.')


# Função main que chama todas as demais funções para calcular o total
def main():
    total = escolha_servico() * num_pagina() + servico_extra()
    print('O total a pagar é: R${:.2f}'.format(total))


main()