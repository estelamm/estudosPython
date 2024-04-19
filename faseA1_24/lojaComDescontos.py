print('Bem Vindo a loja da Estela Matarredona (RU: 4649865)')


#realizando o input para que o usuário informe os valores
valor = float(input('Digite o valor unitário do produto: '))
quantidade = int(input('Digite a quantidade do produto: '))


#calculando o total aqui para definir o desconto na rotina abaixo
total = valor * quantidade


#para facilitar o cálculo transformei a porcentagem do desconto em 1 menos o valor decimal do desconto informado
if (total < 2500):
   desconto = 1


elif (total >= 2500) and (total < 6000):
# 1 - 0.04 = 0.96
   desconto = 0.96


elif ((total >= 6000) and (total < 10000)):
   desconto = 0.93


else:
   desconto = 0.89




print ('valor total sem desconto: R${}' .format(total))
print ('valor total com desconto: R${} ' .format(total * desconto))