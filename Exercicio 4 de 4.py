# ---------- Variáveis Globais ----------
listafuncionarios = []


# ---------- Início de Cadastrar Funcionários ----------

def cadastrarfuncionario(codigo):
    print('\nVocê selecionou a opção de Cadastrar funcionario')

    print('O código da funcionario é: {:0>3}'.format(codigo))

    nome = input('Entre com o nome da funcionario:')

    setor = input('Entre com o setor da funcionario:')

    salario = float(input('Entre com o salario (R$) da funcionario:'))

    dicionariofuncionarios = {
        'codigo': codigo,
        'nome': nome,
        'setor': setor,
        'salario': salario
    }

    listafuncionarios.append(dicionariofuncionarios.copy())


# ---------- Fim de Cadastrar Funcionários ----------

# ---------- Início de Consultar Funcionários ----------

def consultarfuncionario():
    while True:

        try:

            print('\nVocê Selecionou a Opção de Consultar funcionarios')

            opConsultar = int(input('\nEntre com a opção desejada\n1- '
                                    'Consultar Todas as funcionarios\n2- '
                                    'Consultar funcionarios por Código\n3- '
                                    'Consultar funcionarios por setor\n4- '
                                    'Retornar\n-->'))

            if opConsultar == 1:

                print('-' * 20)

                for funcionarios in listafuncionarios:  # funcionários vai varrer toda a lista de funcionários

                    for key, value in funcionarios.items():  # varrer todos os conjuntos chave e valor do dicionario funcionarios

                        print('{} : {}'.format(key, value))

                    print('-' * 20)

            elif opConsultar == 2:

                print('\nVocê Selecionou a Opção funcionarios por Código')

                entrada = int(input('Digite o Código: '))

                print('-' * 20)

                for funcionarios in listafuncionarios:

                    if (funcionarios['codigo'] == entrada):

                        for key, value in funcionarios.items():
                            print('{} : {}'.format(key, value))

                        print('-' * 20)

            elif opConsultar == 3:

                print('\nVocê Selecionou a Opção funcionarios por setor')

                entrada = input('Digite o setor: ')

                print('-' * 20)

                for funcionarios in listafuncionarios:

                    if (funcionarios['setor'] == entrada):

                        for key, value in funcionarios.items():
                            print('{} : {}'.format(key, value))

                        print('-' * 20)

            elif opConsultar == 4:

                break

            else:

                print('Por favor digite somente o que pede')

                continue  # volta pro início do laço

        except ValueError:

            print('Por Favor pare de digitar números que não existe...')

            continue


# ---------- Fim de Consultar Funcionários ----------

# ---------- Início de Remover Funcionários ----------

def removerfuncionario():
    print('\nVocê Selecionou o Remover funcionario')

    entrada = int(input('Digite o Código da funcionario que irá remover: '))

    for funcionarios in listafuncionarios:

        if (funcionarios['codigo'] == entrada):
            listafuncionarios.remove(funcionarios)

    else:

        print('Você removeu o código.')


# ---------- Fim de Remover Funcionários ----------

print('Bem-vindo ao Controle de Funcionários do Danilo Bernardi')

registrofuncionarios = 0

while True:

    try:

        opcao = int(input(
            '\nDigite a opção desejada:\n1- Cadastrar funcionarios\n2- Consultar funcionarios\n3- Remover funcionarios\n4- Sair\n-->'))

        if opcao == 1:

            registrofuncionarios = registrofuncionarios + 1

            cadastrarfuncionario(registrofuncionarios)

        elif opcao == 2:

            consultarfuncionario()

        elif opcao == 3:

            removerfuncionario()

        elif opcao == 4:

            print('Programa finalizado')

            break  # Encerra o laço e o programa acaba

        else:

            print('Digite somente uma das opções do MENU')

            continue  # volta para o início do laço

    except ValueError:

        print('Pare de digitar números que não existe...')
