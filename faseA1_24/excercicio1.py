print('bem vindo a lojinha da gata aurora')

valor = float(input('digite o valor unitário do produto: R$'))
unidade = int(input('digite quantas unidades deseja: '))

total = valor * unidade

if total < 2500:
    x = 2500 - total
    print('faltam {} para você ser agraciado com 4% de desconto' . format(x))

elif (total >= 2500) and (total < 6000):
    x = total * 0.04
    desconto = (total - x)
    print('oba 4% de desconto')

elif (total >= 6000) and (total < 10000):
    x = total * 0.07
    desconto = (total - x)
    print('oba 7% de desconto')

elif (total >= 10000):
    x = total * 0.11
    desconto = (total - x)
    print('oba 11% de desconto')



print('Valor total: R${}.' .format(total))
print('valor com desconto: R${}' .format(desconto))

