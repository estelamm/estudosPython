print('Bem Vindo a loja de Gelados da Estela Matarredona')
print('------------- Cardápio -------------------')
print('--- TAMANHO | CUPUAÇU (CP) | AÇAI (AC) ---')
print('---     P   |   R$10,00    |   R$12,00 ---')
print('---     M   |   R$15,00    |   R$17,00 ---')
print('---     G   |   R$19,00    |   R$21,00 ---')
print('------------------------------------------')

valor = 0
#controle geral da loja
while True:
    #controle do sabor
    while True:
        sabor = input('Qual sabor deseja? (AC/CP)')
        if sabor in['AC', 'CP']:
            break
        else:
            print('sabor invalido!')
            continue
    #controle do tamanho
    while True:
        tamanho = input('qual tamnho deseja?')
        if tamanho in['P', 'M', 'G']:
            break
        else:
            print('tamanho invalido')
            continue

    if sabor == 'CP':
        if tamanho == 'P':
            valor += 10
        elif tamanho == 'M':
            valor += 15
        else:
            valor += 19
    elif sabor == 'AC':
        if tamanho == 'P':
            valor += 12
        elif tamanho == 'M':
            valor += 17
        else:
            valor += 21


    mais = input('deseha fazer mais algum pedido?')
    if mais == 'NÃO':
        print('encerrando seu pedido....')
        break



print('Valor total: R${} ' .format(valor))
