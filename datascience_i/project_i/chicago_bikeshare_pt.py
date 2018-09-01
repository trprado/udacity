# coding: utf-8
""" A documentação se encontra no padrão reStructuredText, preferi utilizar essa forma
pois é a que encontrei como mais simples para ver e distinguir os parâmetros e retornos.

Github: `Thiago Udacity Fundamentos de DataScience I - Projeto I <https://github.com/trprado/udacity/tree/master/datascience_i/project_i> 
"""

# Começando com os imports
import csv
import matplotlib.pyplot as plt

# Vamos ler os dados como uma lista
print("Lendo o documento...")
with open("chicago.csv", "r") as file_read:
    reader = csv.reader(file_read)
    data_list = list(reader)
print("Ok!")

# Vamos verificar quantas linhas nós temos
print("Número de linhas:")
print(len(data_list))

# Imprimindo a primeira linha de data_list para verificar se funcionou.
print("Linha 0: ")
print(data_list[0])
# É o cabeçalho dos dados, para que possamos identificar as colunas.

# Imprimindo a segunda linha de data_list, ela deveria conter alguns dados
print("Linha 1: ")
print(data_list[1])

input("Aperte Enter para continuar...")
# TAREFA 1
# TODO: Imprima as primeiras 20 linhas usando um loop para identificar os dados.
print("\n\nTAREFA 1: Imprimindo as primeiras 20 amostras")

for index in range(1,21): # Imprimir os 20 primeiras amostras por linhas
    print(data_list[index])

# Vamos mudar o data_list para remover o cabeçalho dele.
data_list = data_list[1:]

# Nós podemos acessar as features pelo índice
# Por exemplo: sample[6] para imprimir gênero, ou sample[-2]

input("Aperte Enter para continuar...")
# TAREFA 2
# TODO: Imprima o `gênero` das primeiras 20 linhas

print("\nTAREFA 2: Imprimindo o gênero das primeiras 20 amostras")

for index in range(20): # Impressão das 20 primeiras amostras de sexo por linhas
    print(data_list[index][6])

# Ótimo! Nós podemos pegar as linhas(samples) iterando com um for, e as colunas(features) por índices.
# Mas ainda é difícil pegar uma coluna em uma lista. Exemplo: Lista com todos os gêneros

input("Aperte Enter para continuar...")
# TAREFA 3
# TODO: Crie uma função para adicionar as colunas(features) de uma lista em outra lista, na mesma ordem
def column_to_list(data, index):
    """ Transforma uma colunas em uma lista.
    A partir de uma lista de listas e de um índice de coluna, gera uma nova lista com o conteúdo da coluna requisitado.

    :param data: Lista de lista contendo linhas e colunas.
    :param index: Inteiro da posição da coluna a ser transformada em lista.

    :returns: Lista da coluna informada.
    """
    column_list = [item[index] for item in data] # usando listcomp para gerar a lista
    # Dica: Você pode usar um for para iterar sobre as amostras, pegar a feature pelo seu índice, e dar append para uma lista
    return column_list


# Vamos checar com os gêneros se isso está funcionando (apenas para os primeiros 20)
print("\nTAREFA 3: Imprimindo a lista de gêneros das primeiras 20 amostras")
print(column_to_list(data_list, -2)[:20])

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(column_to_list(data_list, -2)) is list, "TAREFA 3: Tipo incorreto retornado. Deveria ser uma lista."
assert len(column_to_list(data_list, -2)) == 1551505, "TAREFA 3: Tamanho incorreto retornado."
assert column_to_list(data_list, -2)[0] == "" and column_to_list(data_list, -2)[1] == "Male", "TAREFA 3: A lista não coincide."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Agora sabemos como acessar as features, vamos contar quantos Male (Masculinos) e Female (Femininos) o dataset tem
# TAREFA 4
# TODO: Conte cada gênero. Você não deveria usar uma função parTODO isso.
male = 0
female = 0

# O que seria parTodo? (erro na tradução?).
for i in data_list: # Calcula a quantidade de homens e mulheres que estão definidos na lista.
    if i[6] == 'Male':
        male += 1
    elif i[6] == 'Female':
        female += 1

# Verificando o resultado
print("\nTAREFA 4: Imprimindo quantos masculinos e femininos nós encontramos")
print("Masculinos: ", male, "\nFemininos: ", female)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert male == 935854 and female == 298784, "TAREFA 4: A conta não bate."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Por que nós não criamos uma função parTODO isso?
# TAREFA 5
# TODO: Crie uma função para contar os gêneros. Retorne uma lista.
# Isso deveria retornar uma lista com [count_male, count_female] (exemplo: [10, 15] significa 10 Masculinos, 15 Femininos)
def count_gender(data_list):
    """ Conta quantidades de cada gênero.
    Por meio da lista de lista, calcula a quantidade de representantes de cada gênero.

    *Informativo*: poderia ser criado uma função mais genérica caso a chamada do `print()` fosse de uma lista contendo a coluna de gêneros.

    :param data_list: Lista de listas contendo todos os dados carregados do csv.
    :returns: Lista de dois elementos contendo o número de representantes de cada gênero.
    """
    male = 0 
    female = 0
    for item in data_list:
        if item[-2] == 'Male':
            male += 1
        elif item[-2] == 'Female':
            female += 1
    return [male, female]


print("\nTAREFA 5: Imprimindo o resultado de count_gender")
print(count_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(count_gender(data_list)) is list, "TAREFA 5: Tipo incorreto retornado. Deveria retornar uma lista."
assert len(count_gender(data_list)) == 2, "TAREFA 5: Tamanho incorreto retornado."
assert count_gender(data_list)[0] == 935854 and count_gender(data_list)[1] == 298784, "TAREFA 5: Resultado incorreto no retorno!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Agora que nós podemos contar os usuários, qual gênero é mais prevalente?
# TAREFA 6
# TODO: Crie uma função que pegue o gênero mais popular, e retorne este gênero como uma string.
# Esperamos ver "Masculino", "Feminino", ou "Igual" como resposta.
def most_popular_gender(data_list):
    """ Retorna o gênero de maior presença na lista.
    Por meio do csv de lista de listas verifica o gênero de maior presença e retorna seu nome, em caso de igualdade retorna em ambos são iguais.

    *Informativo*: poderia ser criado uma função mais genérica caso a chamada do ``print()`` fosse de uma lista contendo a coluna de gênero.

    :param data_list: Lista de listas contendo o csv com o gênero.
    :returns: String contendo o gênero de maior presença (*Masculino* ou *Feminino*) ou *Igual* em caso de de mesma quantidade em ambos.
    """
    answer = ""
    genders = count_gender(data_list)
    if genders[0] > genders[1]:
        answer = 'Masculino'
    elif genders[0] < genders[1]:
        answer = 'Feminino'
    else:
        answer = 'Igual'
    return answer


print("\nTAREFA 6: Qual é o gênero mais popular na lista?")
print("O gênero mais popular na lista é: ", most_popular_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(most_popular_gender(data_list)) is str, "TAREFA 6: Tipo incorreto no retorno. Deveria retornar uma string."
assert most_popular_gender(data_list) == "Masculino", "TAREFA 6: Resultado de retorno incorreto!"
# -----------------------------------------------------

# Se tudo está rodando como esperado, verifique este gráfico!
gender_list = column_to_list(data_list, -2)
types = ["Male", "Female"]
quantity = count_gender(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Gênero')
plt.xticks(y_pos, types)
plt.title('Quantidade por Gênero')
plt.show(block=True)

input("Aperte Enter para continuar...")
# TAREFA 7
# TODO: Crie um gráfico similar para user_types. Tenha certeza que a legenda está correta.
print("\nTAREFA 7: Verifique o gráfico!")
def count_user_type(user_type_list):
    """ Calcula a quantidade de Clientes e Assinantes.
    Por meio de uma lista calcula a quantidade de clientes "Customer" e assinantes "Subscriber".

    :param data_list: Lista contendo os tipos de usuário.
    :returns: Lista de dois parâmetros contendo a quantidade de clientes e assinantes.
    """
    customer = 0
    subscriber = 0
    for user in user_type_list:
        if user == 'Customer':
            customer += 1
        elif user == 'Subscriber':
            subscriber += 1
    return [customer, subscriber]

user_type_list = column_to_list(data_list, -3)
types = ['Customer', 'Subscriber']
quantity = count_user_type(user_type_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantity')
plt.xlabel('User Type')
plt.xticks(y_pos, types)
plt.title('Quantity per User Type')
plt.show(block=True)

input("Aperte Enter para continuar...")
# TAREFA 8
# TODO: Responda a seguinte questão
male, female = count_gender(data_list)
print("\nTAREFA 8: Por que a condição a seguir é Falsa?")
print("male + female == len(data_list):", male + female == len(data_list))
answer = "Existem tuplas com o gênero não definido e deixado em branco."
print("resposta:", answer)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert answer != "Escreva sua resposta aqui.", "TAREFA 8: Escreva sua própria resposta!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Vamos trabalhar com trip_duration (duração da viagem) agora. Não conseguimos tirar alguns valores dele.
# TAREFA 9
# TODO: Ache a duração de viagem Mínima, Máxima, Média, e Mediana.
# Você não deve usar funções prontas parTODO isso, como max() e min().
trip_duration_list = column_to_list(data_list, 2)
min_trip = 0.
max_trip = 0.
mean_trip = 0.
median_trip = 0.

def my_min(data_list):
    """ Retorna o valor mínimo
    Função que emula o funcionamento da função built-in ``min()`` retornando o menor valor da lista.

    :param data_list: Lista contendo os valores para se encontrar o valor mínimo.

    :returns: Valor número representando o menor valor presente na lista.
    """
    return int(sorted(data_list, key=int)[0])

def my_max(data_list):
    """ Retorna o valor máximo
    Função que emula o funcionamento da função built-in ``max()`` retornando o maior valor da lista.

    :param data_list: Lista contendo os valores para se encontrar o valor máximo.

    :returns: Valor número representando o maior valor presente na lista.
    """
    return int(sorted(data_list, key=int)[-1])

def mean(data_list):
    """ Calcula a média dos valores da lista.
    Por meio de uma lista, calcula a soma de seus valores e divide pelo número de itens somados para se obter a média.

    :param data_lista: Lista com os valores a serem calculados.

    :returns: Inteiro que representa a média dos valores da lista.
    """
    time_sum = 0
    for val in data_list:
        time_sum += int(val)
    return round(time_sum / len(data_list)) # Arredonda para cima ou para baixo (como o valor não é exato e o exercicio parece usar um valor exatado)
                                            # foi utilizada a função built-in round para arredondamento correto, visto que caso fosse dividido utilizando
                                            # o operador '//' seu arredondamente é sempre para baixo "floored quotient".

def median(data_list): # Função baseada no que estudei no Livro Data Science do Zero
    """ Calcula a mediana dos valores de uma lista.
    Por meio de uma lista se encontra os pontos médios e retorna a mediana da lista.
    Baseado no que aprendi no Livro **Data Science do Zero: Primeiras Regras com o 
    Python**, *Alta Book*, Joel Grus 2016.

    :param data_list: Lista com os valores a serem calculados.

    :returns: Inteiro contendo o valor no ponto médio em caso de tamanho ímpar, ou a média dos pontos médios em caso de lista com tamanho par.
    """
    sorted_list = sorted(data_list, key=int)
    n = len(data_list)
    mid = n // 2

    if n % 2 == 1: # odd
        val = float(sorted_list[mid])
    else: # even
        hi = float(sorted_list[mid])
        low = float(sorted_list[mid-1])
        val = (hi+low) / 2
    return val

min_trip = my_min(trip_duration_list)
max_trip = my_max(trip_duration_list)
mean_trip = mean(trip_duration_list)
median_trip = median(trip_duration_list)

print("\nTAREFA 9: Imprimindo o mínimo, máximo, média, e mediana")
print("Min: ", min_trip, "Max: ", max_trip, "Média: ", mean_trip, "Mediana: ", median_trip)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert round(min_trip) == 60, "TAREFA 9: min_trip com resultado errado!"
assert round(max_trip) == 86338, "TAREFA 9: max_trip com resultado errado!"
assert round(mean_trip) == 940, "TAREFA 9: mean_trip com resultado errado!"
assert round(median_trip) == 670, "TAREFA 9: median_trip com resultado errado!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 10
# Gênero é fácil porque nós temos apenas algumas opções. E quanto a start_stations? Quantas opções ele tem?
# TODO: Verifique quantos tipos de start_stations nós temos, usando set()
start_station_list = column_to_list(data_list, 3)
user_types = set(item for item in start_station_list)   # Genexp para gerar de forma direta o set de com as estações de início.
                                                        # Como set() é um conjunto, caso um valor repetido seja adicionado, ele apenas
                                                        # ignora esse valor.
                                                        # o nome da variável é estranho por que diz tipo de usuário e não estações
                                                        # de início. Mantive o que já estava como padrão do exercício.

print("\nTAREFA 10: Imprimindo as start stations:")
print(len(user_types))
print(user_types)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert len(user_types) == 582, "TAREFA 10: Comprimento errado de start stations."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 11
# Volte e tenha certeza que você documenteou suas funções. Explique os parâmetros de entrada, a saída, e o que a função faz. Exemplo:
# def new_function(param1: int, param2: str) -> list:
    #   """
    #   Função de exemplo com anotações.
    #   Argumentos:
    #       param1: O primeiro parâmetro.
    #       param2: O segundo parâmetro.
    #   Retorna:
    #       Uma lista de valores x.

    #   """

input("Aperte Enter para continuar...")
# TAREFA 12 - Desafio! (Opcional)
# TODO: Crie uma função para contar tipos de usuários, sem definir os tipos
# para que nós possamos usar essa função com outra categoria de dados.
print("Você vai encarar o desafio? (yes ou no)")
answer = "yes"

def count_items(column_list):
    """ Calcula a quantidade de itens diferentes em uma coluna
    Através de uma lista que represente uma coluna, calcula a quantidade de cada tipo de item existente retornando uma tupla de
    duas listas com os itens em ordem de encontro e suas quantidades.

    **Informativo**: Se utilizar o module de coleções ``collections.Count`` podemos fazer o mesmo de forma mais rápida, visto que ele
    retorna um dicionário contendo como chave o valor do iterável e a quantidade de itens contados para aquele valor.

    :param column_list: Lista contendo a coluna com os valores que se deseja contar.
    :returns: Tupla de duas listas com a primeira contendo os itens achados em ordem, e a segunda a contagem de cada item na mesma ordem.
    """
    item_types = []
    count_items = []
    for item in column_list:
        if item in item_types:
            count_items[item_types.index(item)] += 1
        else:
            item_types.append(item)
            count_items.append(1)
    return item_types, count_items


if answer == "yes":
    # ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
    column_list = column_to_list(data_list, -2)
    types, counts = count_items(column_list)
    print("\nTAREFA 11: Imprimindo resultados para count_items()")
    print("Tipos:", types, "Counts:", counts)
    assert len(types) == 3, "TAREFA 11: Há 3 tipos de gênero!"
    assert sum(counts) == 1551505, "TAREFA 11: Resultado de retorno incorreto!"
    # -----------------------------------------------------