print ('Bem Vindo ao Atacado  Danilo Bernardi')
valor_unitario = float(input('Entre com o valor do produto: '))  # Define a variavel valor_unitario
# com o valor de cada produto
quantidade = int(input('Entre com o valor da quantidade: '))  # Define a variavel quantidade
# com a quantidade de produtos
valor_frete = 0  # Variavel que receberá o valor do frete dependendo da quantidade de
# produtos inseridos

if 0 <= quantidade < 11:
   valor_frete = 30

elif 11 <= quantidade < 101:
   valor_frete = 60

elif 101 <= quantidade < 1001:
   valor_frete = 120

else:
   valor_frete = 240


valor_parcial = float(valor_unitario * quantidade)  # Define a variavel valor_parcial com o valor
# parcial da multiplicação entre o valor_unitario * a quantidade

valor_total = float(valor_parcial + valor_frete)  # Define a variavel valor_total com o valor
# total da soma entre o valor_parcial + o valor_frete

print('O valor sem frete foi: R$ {:.2f}'.format(valor_parcial))  # imprime o valor_parcial formatado
# com duas casas decimais após o ponto

print('O valor com desconto foi: R$ {:.2f} '.format(valor_total) + '(frete de R$ {:.2f})'.format(valor_frete))
# imprime o valor_total formatado com duas casas decimais após o ponto

print('Atacado Danilo Bernardi Agradece à sua Preferência')