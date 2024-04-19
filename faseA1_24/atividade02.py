print('Bem Vindo a loja de Gelados da Estela Matarredona')
print('------------- Cardápio -------------------')
print('--- TAMANHO | CUPUAÇU (CP) | AÇAI (AC) ---')
print('---     P   |   R$10,00    |   R$12,00 ---')
print('---     M   |   R$15,00    |   R$17,00 ---')
print('---     G   |   R$19,00    |   R$21,00 ---')
print('------------------------------------------')


valor = 0
while True:
   # ao digitar sim para comprar mais, a função retorna a partir daqui
   while True:
       sabor = input('Escolha o sabor desejado (CP ou AC): ')
       if sabor in ['AC', 'CP']:
           break
       else:
           print('Sabor invalido. Insira novamente')


   while True:
       tamanho = input('Escolha o tamanho (P, M ou G): ')
       if tamanho in ['P', 'M', 'G']:
           break
       else:
           print('Tamanho invalido. Insira novamente')


   # teste para saber se é cupuaçu
   if sabor == 'CP':
       if tamanho == 'P':
           valor += 10
       elif tamanho == 'M':
           valor += 15
       else:
           valor += 19


   # como acima ja foi verificado se está dentro de CP / AC, não é necessário avaliar aqui novamente com elif
   else:
       if tamanho == 'P':
           valor += 12
       elif tamanho == 'M':
           valor += 17
       else:
           valor += 21


   comprarmais = input('Deseja pedir mais alguma coisa? (Digite SIM para comprar mais, senão seu pedido será finalizado) ')


   if comprarmais == 'SIM':
       continue
   else:
       # O continue volta o while lá do começo para pegar mais produtos
       break


print('O valor total do seu pedido é de R${}'.format(valor))