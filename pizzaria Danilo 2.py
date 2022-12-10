print('Bem vindo a SORVETERIA do Danilo Bernardi')
print('----------------------------------------Cardápio----------------------------------------')
print('| Codigo | Descrição            | Tamanho P (500ml) | Tamanho M (1000ml) | Tamanho G (2oooml)|')
print('|   TR   | Sabores Tradicionais |      R$ 6,00      |      R$ 10,00      |       R$ 18,00    |')
print('|   ES   | Sabores Especiais    |      R$ 7,00      |      R$ 12,00      |       R$ 21,00    |')
print('|   PR   | Sabores Premium      |      R$ 8,00      |      R$ 14,00      |       R$ 24,00    |')
acumulador = 0
while True:
    tamanho = input ('Escolha o tamanho do sorvete desejado (P/M/G): ')
    tamanho = tamanho.upper()
    if tamanho!= 'P' and tamanho != 'M' and tamanho !='G' :
        print('Opção Inválida. Pare de digitar tamanhos que não existem!')
        continue #se o usuário digitar algo inválido volta para o começo do while

    codigo = input('Escolha seu sabor de sorvete (TR/ES/PR): ')
    codigo = codigo.upper()
    if codigo != 'TR' and codigo != 'ES' and codigo != 'PR':
        print('Opção Inválida. Pare de digitar codigos que não existe!')
        continue  # se o usuário digitar algo inválido volta para o começo do while

    if codigo == 'TR' and tamanho =='P':
        print('Você escolheu o sorvete Tradicional tamanho P')
        acumulador = acumulador + 6 # pegue o valor que tinha no acumulador e soma com 6

    elif codigo == 'TR' and tamanho ==  'M':
        print('Você escolheu o sorvete Tradicional tamanho P')
        acumulador = acumulador + 10  # pegue o valor que tinha no acumulador e soma com 10

    elif codigo == 'TR' and tamanho ==  'G':
        print('Você escolheu o sorvete Tradicional tamanho G')
        acumulador = acumulador + 18  # pegue o valor que tinha no acumulador e soma com 18

    elif codigo == 'ES' and tamanho =='P':
        print('Você escolheu o sorvete Especial tamanho P')
        acumulador = acumulador + 7  # pegue o valor que tinha no acumulador e soma com 7

    elif codigo == 'ES' and tamanho ==  'M':
        print('Você escolheu o sorvete Especial tamanho P')
        acumulador = acumulador + 12  # pegue o valor que tinha no acumulador e soma com 12

    elif codigo == 'ES' and tamanho ==  'G':
        print('Você escolheu o sorvete Especial tamanho G')
        acumulador = acumulador + 21  # pegue o valor que tinha no acumulador e soma com 21

    elif codigo == 'PR' and tamanho =='P':
        print('Você escolheu o sorvete Premium tamanho P')
        acumulador = acumulador + 8  # pegue o valor que tinha no acumulador e soma com 8

    elif codigo == 'PR' and tamanho ==  'M':
        print('Você escolheu o sorvete Premium tamanho P')
        acumulador = acumulador + 14   # pegue o valor que tinha no acumulador e soma com 14

    elif codigo == 'PR' and tamanho ==  'G':
        print('Você escolheu o sorvete Premium tamanho G')
        acumulador = acumulador + 24  # pegue o valor que tinha no acumulador e soma com 24

    pedir_mais = input ('Gostaria de mais algum sorvete (S/Ou qualquer outra tecla)?: ')
    pedir_mais = pedir_mais.upper() #resolvo o problema de 's' e 'S'
    if pedir_mais == 'S':
        continue
    else:
        print('Valor total a ser pago: R${:.2f}'.format(acumulador))
        break
