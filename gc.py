from mip import *


# estruturas de dados para manter variáveis e restrições
lambdas = []
constraints = []

# criando modelo do mestre
master = Model()
...

# criando modelo do pricing
pricing = Model()
...

new_vars = True

while new_vars:
    ##########
    # PASSO 1: resolver o mestre
    ##########

    ...

    ##########
    # PASSO 2: atualizar o pricing com os valores duais do mestre e resolvê-lo
    ##########

    # dica: o dual da restrição i pode ser facilmente obtido pelo atributo *pi*

    # exemplo: constraints[i].pi

    ...

    ##########
    # PASSO 3: inserir as novas colunas no mestre (se custo reduzido for negativo)
    ##########

    # dica: use a classe Column para gerar uma coluna; esta classe especifica os
    #       coeficientes de uma nova variável em um conjunto de restrições

    # exemplo: column = Column([constraints[0], constraints[1]], [1, 1])
    #          lambdas.append(master.add_var(obj=1, column=column))

    # importante: se não for encontrada nenhuma variável com custo reduzido negativo,
    #             lembre-se de fazer new_vars = False
